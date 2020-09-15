import requests
import json
import timeit
import os
import schedule
from sendingPrefix import compare_roa
from verifPrefix import compare_rov

def run_dispatcher():
    capture_file = os.getcwd()+'/capture.txt' 
    # startTime = timeit.default_timer()
    with open (capture_file,"r") as myfile:
        buffer_rov=[]
        buffer_roa=[]
        for line in myfile:
            # prefix,path = map(str.strip,line.split(';'))
            if ';' in line:
                prefix,path = map(str.strip,line.split(';'))
                if path not in ['i']:
                    word = path.split(" ")
                    word_length = len(word)
                    as_origin = word[word_length-2]
                    # print('prefix :'+str(prefix)+ ' is the originate by  : '+str(as_origin))
                    buffer_rov.append(prefix+';'+as_origin)
                else:
                    # print(str(prefix)+' is internal prefix')
                    buffer_roa.append(prefix)
                    # sendPrefixRequest(prefix,asNumber)
                    # stopTime = timeit.default_timer()
                    # exeTime = str(stopTime-startTime)
                    # with open ("verifTime.txt","a") as sendingTime:
                    #     sendingTime.write(exeTime + '\n')        
    compare_roa(buffer_roa)        
    compare_rov(buffer_rov)

schedule.every().second.do(run_dispatcher)

while True:
    schedule.run_pending()
