import datetime
import requests
import json


##now=datetime.datetime.now().time().strftime("%H:%M:%S")
##scan_time=5
##while(1):
##    
##    now=time.time()
####    print("time slot",t1-now)
##    if((now-prev)>scan_time):
##        print("5 mins")
##        prev=time.time()
##        
        
##print(now)
payload = {
   "Time_stamp":"2020-10-17 17:03:04.470871",
   "Name":"POCO",
   "Sr_no":"28",
   "Mac_id":"20:A6:0C:38:AB:22"
}

r=requests.post('''http://demo.bridgestonechallenge.in/getMacData''',json=(payload))
print('''Status Code:''', r.status_code)
print(r.reason)
print(r.ok)
print(r.content)
print(r.json())

##json_object = json.dumps(payload, indent = 4)   
##print(json_object) 
