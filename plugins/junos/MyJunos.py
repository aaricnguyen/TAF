import sys
import yaml
import jinja2
import json
from lxml import etree
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import LockError
from jnpr.junos.exception import UnlockError
from jnpr.junos.exception import ConfigLoadError
from jnpr.junos.exception import CommitError
from jnpr.junos.exception import RpcError


class MyJunos(object):

    def __init__(self, *args, **kwargs):
        self.device = Device(*args, **kwargs)
       
        self.__create_and_binding_the_config_utility()
    
    def __create_and_binding_the_config_utility(self):
        self.device.bind(cu=Config)
        
    def connect_to_device(self):
        try:
            self.device.open()
            print ("Connection successfully...")
        except ConnectError as err:
            print ("ConnectError: Cannot connect to device: {0}".format(err))
            sys.exit(1)
        except Exception as err:
            print (err)
            sys.exit(1)
    
    def disconnect_to_device(self):
        try:
            self.device.close()
            print("Connection closed...")
        except Exception as err:
            print (err)
            sys.exit(1)
    
    def get_facts(self):
        return self.device.facts
    
    def lock(self):
        print ("Locking the configuration")
        try:
            self.device.cu.lock()
        except LockError as err:
            print ("Unable to lock configuration: {0}".format(err))
            self.disconnect_to_device()
            sys.exit(1)
    
    def unlock(self):
        print ("Unlocking the configuration")
        try:
            self.device.cu.unlock()
        except UnlockError as err:
            print ("Unable to unlock configuration: {0}".format(err))
            sys.exit(1)
    
    def load_config_text(self, conf_text, merge=False, overwrite=False, update=False):
        try:
            print ("Loading configuration changes...")
            self.device.cu.load(conf_text, format="set", merge=merge, overwrite=overwrite, update=update)
        except (ConfigLoadError, Exception) as err:
            print ("Unable to load configuration changes: {0}".format(err))
            print ("Unlocking the configuration...")
            try:
                self.unlock()
            except UnlockError:
                print ("Unable to unlock configuration: {0}".format(err))
            self.disconnect_to_device()
            sys.exit(1)
    
    def load_config_file(self, conf_file, merge=False, overwrite=False, update=False, format="text"):
        try:
            print ("Loading configuration changes...")
            self.device.cu.load(path=conf_file, merge=merge, overwrite=overwrite, update=update, format=format)
        except (ConfigLoadError, Exception) as err:
            print ("Unable to load configuration changes: {0}".format(err))
            print ("Unlocking the configuration...")
            try:
                self.unlock()
            except UnlockError:
                print ("Unable to unlock configuration: {0}".format(err))
            self.disconnect_to_device()
            sys.exit(1)
    
    def load_config_jinja_template(self, jinja_template_path, yaml_data_path, merge=False, overwrite=False, update=False):
        try:
            # Open and read yaml file to template_vars as dictionary
            with open(yaml_data_path, 'r') as fh:
                template_vars = yaml.load(fh.read())
            print ("Loading configuration changes...")
            self.device.cu.load(template_path=jinja_template_path, template_vars=template_vars, merge=merge, overwrite=overwrite, update=update, format='text')
        except (ConfigLoadError, Exception) as err:
            print ("Unable to load configuration changes: {0}".format(err))
            print ("Unlocking the configuration...")
            try:
                self.unlock()
            except UnlockError:
                print ("Unable to unlock configuration: {0}".format(err))
            self.disconnect_to_device()
            sys.exit(1)
    
    def commit(self):
        try:
            print ("Checking difference...")
            if self.device.cu.diff() is None:
                print ("There are not configuration changes")
            else:
                print ("Committing the configuration...")
                self.device.cu.pdiff()
                self.device.cu.commit()
                print ("Committing successfully...")
        except CommitError as err:
            print ("Unable to commit configuration: {0}".format(err))
            print ("Unlocking the configuration")
            try:
                self.device.cu.unlock()
            except UnlockError as err:
                print ("Unable to unlock configuration: {0}".format(err))
            self.disconnect_to_device()
            sys.exit(1)
    
    def roll_back(self, rb_id=0):
        try:
            print ("Rolling back the configuration...")
            self.device.cu.rollback(rb_id)
        except RpcError as err:
            print ("Unable to rollback configuration changes: {0}".format(err))
            print ("Unlocking the configuration...")
            try:
                self.device.cu.unlock()
            except UnlockError as err:
                print ("Unable to unlock configuration: {0}".format(err))
            self.disconnect_to_device()
            sys.exit(1)
    
    def put_file_from_local_to_device(self, local_file, remote_path, progress=True):
        from jnpr.junos.utils.scp import SCP 
        with SCP(self.device, progress=progress) as scp:
            scp.put(local_file, remote_path=remote_path)
    
    def get_file_from_device_to_local(self, remote_file, local_path, progress=True):
        from jnpr.junos.utils.scp import SCP
        with SCP(self.device, progress=progress) as scp:
            scp.get(remote_file, local_path=local_path)
    
    def reboot(self):
        try:
            from jnpr.junos.utils.sw import SW
            sw = SW(self.device)
            print ("Rebooting...")
            print (sw.reboot())
            print ("The system reboot successfully")
        except RpcError as err:
            print ("Unable to reboot the system: {0}".format(err))
            sys.exit(1)

    def execute_cli(self, command, format='text', warning=True):
        try:
            return self.device.cli(command, format, warning)
        except Exception as err:
            print ("Unable to execute the cli command: {0}".format(err))
            sys.exit(1)
            
if __name__ == "__main__":
    pass

