import mysql.connector
import pandas as pd
import json
import ast

def connect_db():
    db = mysql.connector.connect(host = "10.20.14.181",user = "root",passwd = "sa",database = "TAF1")
    return db

def name_tc():
    testcase=[]
    name_tc=pd.read_sql_query("select name from test_case",connect_db())
    for i in range(len(name_tc['name'])):
        testcase.append(name_tc['name'][i])
    return testcase
    
def name_ts():
    testsuite=[]
    name_ts=pd.read_sql_query("select name from test_suite",connect_db())
    for i in range(len(name_ts['name'])):
        testsuite.append(name_ts['name'][i])
    return testsuite

class tc_management():
    def tc_steps(nametc):
        tc_steps=''
        tc=''
        tc=pd.read_sql_query('select steps from test_case where name=%s',connect_db(),params=[nametc])
        tc_steps=tc['steps'][0]
        tc=json.loads(tc_steps)     #convert str to json
        return tc

class ts_management():
    def ts_steps(namets):
        ts_steps=''
        ts=''
        ts=pd.read_sql_query('select list_tc from test_suite where name=%s',connect_db(),params=[namets])
        ts_steps=ts['list_tc'][0]
        ts_steps=ast.literal_eval(ts_steps)  #convert str to list
        return ts_steps

class data_mag(): 
    value = input('Please input testcase or testsuite: ') #input testcase or testsuite to excutor
    if value in name_tc():
        data=[]
        data.append(tc_management.tc_steps(value))
    elif value in name_ts():
        data=[]
        num_tc = ts_management.ts_steps(value)
        for i in range(len(num_tc)):
            data.append(tc_management.tc_steps(num_tc[i]))
    else:
        data=None
    print(data)


