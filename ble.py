import os
import time
##import xlsxwriter
##import xlrd
import sys
import datetime
import bluetooth
from bluetooth import *
import sqlite3
from client import *
import global_test_var as GV

##import threading
##Upload_thread = threading.Thread(target = timetoupload, args = ())
##Upload_thread.start()

def bluet():
##    GV.flag=1
    print ("Searching for nearby devices..... ")
    nearby_devices = bluetooth.discover_devices(lookup_names= True, flush_cache=True)
    print ("found %d devices " %len(nearby_devices))
    devices =[]
    addr=0
    name=None
    for addr, name in nearby_devices:

        try:
                      
            print ("%s -%s " %(addr,name))
            devices.append((addr,name))
            print("devices",devices)

        except:

            print ("%s -%s " %(addr, name.encode('utf-8' , 'replace')))

    try:
        conn= sqlite3.connect('database.db')
        c= conn.cursor()
        print ("Successfully Connect to SQLite")

        for i in devices:
            ct = datetime.datetime.now()
            macid_query='''select Mac_id from blue'''
            c.execute(macid_query)
            macid=[str(i) for i in c.fetchall()]
            macid=list(map(lambda x:x[2:-3], macid))
##            print("macid",macid)
            if (str(i[0]) in macid):
                print("Query executed Data stored in Database.")
                continue
            sql_query= '''INSERT INTO blue(Name,Mac_id,Time_stamp) VALUES ('{}','{}','{}')'''.format(str(i[1]),str(i[0]),str(ct))
            
            c.execute(sql_query)
        conn.commit()


        c.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite",error)
    return()


##def main():
##    bluet()


if __name__ == '__main__':
    prev=time.time()
    scan_time=6
    while(1):
        now=time.time()
        if((now-prev)>scan_time):
##            print(" minuts")
            prev=time.time()
            bluet()
            
    
    

