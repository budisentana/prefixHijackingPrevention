import requests
import json
import timeit
import time
import os


def verifPrefixRequest(pref,asN):
    url = 'http://localhost:8093/api/querypref'
    headers = {'content-type': 'application/json',
        'accept-encoding': 'application/json',
        'charsets': 'utf-8'}
    payload = {'ip_prefix':pref,'ASN':asN}
    response = requests.post(url=url,headers=headers,data=json.dumps(payload))
    print(response.status_code)
    print('Vefifying '+str(pref)+ ' to Blockchain whith ASN'+str(asN))


dataset = os.getcwd()+'/data_to_test.txt'
time_record = os.getcwd()+'/record_data_ver.txt'
exe_time = []
with open (dataset,'r') as myfile:
    prev_time = 0
    for line in myfile:
        prefix,asNumber = map(str.strip,line.split(';'))
        startTime = timeit.default_timer()
        verifPrefixRequest(prefix,asNumber)
        stopTime = timeit.default_timer()       
        delta = (stopTime-startTime)+prev_time
        exe_time.append(delta)
        prev_time = delta
        time.sleep(1)
with open(time_record,'w') as rec_time:
    for num,line in enumerate(exe_time):
        rec_time.write(str(num+1)+';'+str(line)+'\n')
        
        
