import requests
import json
import timeit
import time
import os
import schedule
from sendingPrefix import compare_roa
from verifPrefix import compare_rov

def run_dispatcher():
    status = 'normal'
    capture_file = os.getcwd()+'/capture.txt' 
    # startTime = timeit.default_timer()
    with open (capture_file,"r") as myfile:
        buffer_rov=[]
        buffer_roa=[]
        for line in myfile:
            # prefix,path = map(str.strip,line.split(';'))
            if ';' in line:
                prefix,hop,path = map(str.strip,line.split(';'))
                # print(prefix+hop+path)
                if hop not in ['0.0.0.0','0'] and prefix:
                    as_origin = path
                    # print('prefix :'+str(prefix)+ ' is the originate by  : '+str(as_origin))
                    buffer_rov.append(prefix+';'+hop+';'+as_origin)
                elif hop in ['0.0.0.0']:
                    # print(str(prefix)+' is internal prefix')
                    buffer_roa.append(prefix)
    compare_roa(buffer_roa)        
    compare_rov(buffer_rov)
    print(status)

schedule.every().second.do(run_dispatcher)

while True:
    schedule.run_pending()
    time.sleep(1)
