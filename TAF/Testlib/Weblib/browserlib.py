from selenium import webdriver
import time
import re
from selenium.webdriver.common.keys import Keys
import sys
sys.path.append('/home/diep.nguyen/Desktop/TAF')
import TAF

temp=None

def setup():
    user=''
    password=''

class browserlib():

    def __init__(self):
        self.enviroment=temp
    
    def open(self,URL,browsers):
        if browsers=="ff":
            self.driver = webdriver.Firefox()
        elif browsers=="gc":
            self.driver = webdriver.Chrome()
        self.driver.get(URL)
        return self.driver

    def login(self, user, password):
        setup.user=user
        setup.password=str(password)
        usernamefield = self.enviroment.find_element_by_xpath("//*[@id='username']")
        usernamefield.send_keys(user)
        passwordfield = self.enviroment.find_element_by_xpath("//*[@id='password']")
        passwordfield.send_keys(password)
        signin = self.enviroment.find_element_by_xpath("//*[@id='signin']")
        signin.click()
        time.sleep(1)
     
    def kiemtra(self):
        if setup.user == "":
            noemail = self.enviroment.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/div[1]/div/small[1]")
            assert noemail.text == "Company email can't be empty"
        elif setup.password == "":
            nopass = self.enviroment.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/div[2]/div/small[1]")
            assert nopass.text == "he password is required and can't be empty"
        elif len(str(setup.password))<4:
            nopass = self.enviroment.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/div[2]/div/small[2]")
            assert nopass.text == "The password must be more than 4 characters long"
        elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", setup.user):
            noemail = self.enviroment.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/div[1]/div/small[2]")
            assert noemail.text == "Please enter a valid email address"
        else:
            message = self.enviroment.find_element_by_id("showMessage")
            assert message.text == "Invalid Username/Password"
        
    def close(self):
        time.sleep(1)
        self.enviroment.close()


        
        
        