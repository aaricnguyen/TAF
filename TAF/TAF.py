import pandas as pd
from datetime import datetime
from Management.TC_TS_TB.tc_ts_tb import connect_db, data_mag,ts_management
import Testlib.Weblib.browserlib

#---------------------class enviroment-------------------------------
class env():
    enviroment=None

#---------------------class run_TAF-------------------------------
class run_TAF():
    data=data_mag.data                                      #get data from script tc_ts_tb.py
    data_tc=None

    def ts_run():      
        for idx, val in enumerate(data_mag.data):
            run_TAF.data_tc=val                             #from data_mag.data get data for a TC (because data have many tc)
            test_execution.id=test_execution.id_exe[idx]    #get id in execution for a TC
            run_TAF.tc_run()                                #run TC

    def tc_run():
        data=run_TAF.data_tc                                #get data_tc
        test_execution.start_run_exe()                      #update start_time
        try:    
            for key in data.keys():
                x = pd.read_sql_query('select path from test_lib where name=%s',connect_db(),params=[key])   
                x=x['path'][0]                              #get path from DB
                args=data[key]                              #get arguments of keywword
                x=eval(x)                                   #convert from str to class function
                path=getattr(x,key)                         #get path.keyword()
                if key=='open':
                    env.enviroment=path(*args)                      #run keyword func with arguments got before
                    Testlib.Weblib.browserlib.temp=env.enviroment   #save enviroment to temp
                else:
                    path(*args)
        except AssertionError:
            test_batch.result.append('Failed')
            test_execution.result='Failed'
            test_execution.error='AssertionError'
            env.enviroment.close()
        else:
            test_batch.result.append('Pass')
            test_execution.result='Pass'
            test_execution.error=None
        test_execution.end_run_exe()                          #update endtime, result to execution table
#----------------------class test_batch------------------------------
class test_batch():
    id=None
    result=[]
    kq=''
    def time():                                 #get time now 
        time=datetime.now()
        time1=time.strftime('%Y-%m-%d %H:%M:%S')
        time2=datetime.strptime(time1,'%Y-%m-%d %H:%M:%S')
        return time2

    def testbatch_start():                      #create testbatch, insert start_time and name tc or ts
        name=data_mag.value                     
        timestart=test_batch.time()
        db=connect_db()
        mycursor=db.cursor()
        sql= "INSERT INTO testbatch (start_time, ts_tc_name) VALUES (%s, %s)"
        val=[(timestart,name)]
        mycursor.executemany(sql, val)
        test_batch.id=mycursor.lastrowid
        db.commit()

    def testbatch_end():                        #update testbatch (end_time, result) after run tc
        timeend=test_batch.time()
        db=connect_db()
        mycursor=db.cursor()
        id=test_batch.id
        sql= "UPDATE testbatch SET end_time=%s where id=%s"
        sql1= "UPDATE testbatch SET result=%s where id=%s"
        value=[(timeend,id)]
        if 'Failed' in test_batch.result:
            kq='Failed'
        else:
            kq='Pass'
        value1=[(kq,id)]
        mycursor.executemany(sql,value)
        mycursor.executemany(sql1,value1)
        db.commit()

#----------------------class execution------------------------------
class test_execution():
    value=data_mag.value                #get value that want run
    id_exe=[]                           #this variable containt total id of tc run in exe table 
    id=None
    result=''
    error=''
    def nametc():                       #get nametc cua tc or ts ---> insert to execution table
        nametc=[]
        if len(data_mag.data)==1:
            nametc.append(test_execution.value)
        else:
            nametc=ts_management.ts_steps(test_execution.value)
        return nametc

    def create_execution():             #create total tc to exe table
        nametc=test_execution.nametc()
        db=connect_db()
        mycursor=db.cursor()
        for idx,value in enumerate(nametc):
            sql= "INSERT INTO execution (tc_name, tb_id) VALUES (%s, %s)"
            val=[(value,str(test_batch.id))]
            mycursor.executemany(sql, val)
            test_execution.id_exe.append(mycursor.lastrowid)
        db.commit()

    def start_run_exe():                #update start_time for TC in execution table when tc run
        start=test_batch.time()
        db=connect_db()
        mycursor=db.cursor()
        sql= "UPDATE execution SET start_time=%s where id=%s"
        val=[(start,test_execution.id)]
        mycursor.executemany(sql, val)
        db.commit()

    def end_run_exe():                  #update end_time,result for TC in execution table when tc run
        end=test_batch.time()
        db=connect_db()
        mycursor=db.cursor()
        sql= "UPDATE execution SET end_time=%s where id=%s"
        val=[(end,test_execution.id)]
        mycursor.executemany(sql, val)
        sql1= "UPDATE execution SET result=%s where id=%s"
        val1=[(test_execution.result,test_execution.id)]
        mycursor.executemany(sql1, val1)
        sql2= "UPDATE execution SET error=%s where id=%s"
        val2=[(test_execution.error,test_execution.id)]
        mycursor.executemany(sql2, val2)
        db.commit()
    
#-----------------------main-----------------------------
if __name__ == "__main__":
    env()                                   #setup enviroment
    data_mag()                              #get data from script Management.TC_TS_TB.tc_ts_tb  
    if data_mag.data!=None:
        test_batch.testbatch_start()        #insert time-start and name to DB
        test_execution.create_execution()
        run_TAF.ts_run()                    #run tc
        test_batch.testbatch_end()          #update time_end and result to DB
    else:
        print('TestCase or TestSuite does not exist')
    

         


        
