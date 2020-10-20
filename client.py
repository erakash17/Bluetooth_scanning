import sqlite3
import time
import json
import datetime
import requests
import global_test_var as GV
##def timetoupload():
##    while True:
##        Upload_Time=datetime.time(15, 50, 0, 121320).strftime("%H:%M:%S")
##        if(datetime.datetime.now().time().strftime("%H:%M:%S")==Upload_Time):
##            GV.flag=1
##            print("match",GV.flag)
##            client()
##        
        
    
def client():
##    while True:
##        time.sleep(0.01)
##    if(GV.flag==1):
    try:
        conn= sqlite3.connect('database.db')
        cursor= conn.cursor()
        print ("Successfully Connect to SQLite")

        query=cursor.execute('''select * FROM blue''')
        payload = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]

##        print("payload",payload)
        conn.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite",error)

        
        

    for i in range(0,len(payload)):
     payload[i]['Sr_no']=str(payload[i].get('Sr_no'))
     payload[i]['Name']=str(payload[i].get('Name'))
     payload[i]['Time_stamp']=str(payload[i].get('Time_stamp'))
     payload[i]['Mac_id']=str(payload[i].get('Mac_id'))
     r=requests.post('''http://demo.bridgestonechallenge.in/getMacData''',json=payload[i])
     print('''Status Code:''', r.status_code)
##     print(r.reason)
##     print(r.ok)
     print(r.text)
##     print("Payload",payload[i])
##     print(r.json())
    ##http://demo.bridgestonechallenge.in/getMacData
##            return()

if __name__ == '__main__':
    client()
    
