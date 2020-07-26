import requests
import json
import timeit

url = 'http://localhost:8091/api/addpref'
headers = {'content-type': 'application/json',
        'accept-encoding': 'application/json',
        'charsets': 'utf-8'}
payload = {'ip_prefix':'22.22.22.0/22','ASN':'22','exp_stat':'0'}
response = requests.post(url=url,headers=headers,data=json.dumps(payload))
print(response)
s = response.session(config={'keep_alive': False})
