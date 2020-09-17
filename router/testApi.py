import requests
import json
import timeit

# url = 'http://localhost:8091/api/addpref'
# headers = {'content-type': 'application/json',
#         'accept-encoding': 'application/json',
#         'charsets': 'utf-8'}
# payload = {'ip_prefix':'1.1.1.1/24','ASN':'22','exp_stat':'1'}
# response = requests.post(url=url,headers=headers,data=json.dumps(payload))
# print(response.content)


url = 'http://localhost:8093/api/querypref'
headers = {'content-type': 'application/json',
        'accept-encoding': 'application/json',
        'charsets': 'utf-8'}
payload = {'ip_prefix':'192.11.11.0','ASN':'1111'}
response = requests.post(url=url,headers=headers,data=json.dumps(payload))
print(response.status_code)