"""
    - Find the root router from the node_setup.txt
    - Copy dispatcher folder to the corresponding router folder
    - Update dispatcher configuration file  
    - Activate Blockchain module (deploy blockchain, deploy node js, create admin and user credential)
    - Send prefix to the blockchain

"""
import os
import random
import time
import json
import subprocess
import requests

# """Set number of dispatcher to deploy"""
# dispatcher_number = 1


dirname = os.getcwd()
rand_list=[]
file_path = dirname+'/node_setup.txt'
print ('Find the root router')
router_number = open(file_path).readlines()
root = router_number[0].strip()
print((root))
# while len(rand_list) < dispatcher_number:
#     random_pos = random.randint(0,router_number-1)
#     if random_pos not in rand_list:
#         rand_list.append(random_pos)

# print('Copying Dispatcher to selected router folder')
# dispatcher_list=[]
# with open (file_path,'r') as node_file:
#     for i,line in enumerate(node_file):
#         if i in rand_list:
#             host_name, host_ip, router_name, asn = map(str.strip,line.split(';'))
#             # asn_no = asn.lstrip('ASN')
#             dispatcher_list.append(host_ip+';'+asn)
#             mkdir_com = 'mkdir '+dirname+'/'+asn+'/dispatcher'
#             os.system(mkdir_com)
#             copy_com = 'cp -r '+dirname+'/dispatcher/* '+dirname+'/'+asn+'/dispatcher/'
#             print(copy_com)
#             os.system(copy_com)

print('Copying Dispatcher to selected router folder')
dispatcher_list=[]
host_name, host_ip, router_name, asn = map(str.strip,root.split(';'))
dispatcher_list.append(host_ip+';'+asn)
mkdir_com = 'mkdir '+dirname+'/'+asn+'/dispatcher'
os.system(mkdir_com)
copy_com = 'cp -r '+dirname+'/dispatcher/* '+dirname+'/'+asn+'/dispatcher/'
print(copy_com)
os.system(copy_com)

print('Write the selected router and dispatcher position to file')
with open ('dispatcher_position.txt','w') as dis_pos:
    for item in dispatcher_list:
        dis_pos.write(item+'\n')

print('Sleep 5 second befor configuring Dispatcher')
time.sleep(5)
for item in dispatcher_list:
    host_ip,asn = map(str.strip,item.split(';'))
    dis_path = dirname+'/'+asn+'/dispatcher/config.json'
    print('Updating '+dis_path)
    with open(dis_path,'r') as json_file:
        new_data = json.load(json_file)
        asn_new = asn.lstrip('AS')
        new_data["router_ip"] = " "+host_ip+" "
        new_data["asn"] = " "+asn_new+" "
    
    with open(dis_path,'w') as json_file:
        json.dump(new_data,json_file)

print('Sleep 5 second before Activating Blockchain module')
time.sleep(5)
"""
    This part is used to activate blockchain module and send the prefix to the blockchain.
    This part also bypassing the prefix authentication process conduct by dispatcher
"""
root = os.path.dirname(os.getcwd())
server_path = root+'/server/'

print('Deploying Blockchain module')
os.chdir(server_path)
os.system('./startbsbri.sh')

# Installing node js module (npm install)
print('Installing node js to server')
os.chdir(server_path+'/server1/')
os.system('npm install')


# Create admin and router credential
print ('Create admin and router credential')
os.system('node enrollAdmin.js')
os.system('node registerRouter.js')

print('Activating REST API server')
"""This process runing indefinitely user kill $(lsof -t -it:8091) to stop it"""
api_server = os.getcwd()+'/apiServer.js'
subprocess.Popen(["node",api_server])

print('Sleep 5 second before Sending prefix to the Blockchain')
time.sleep(5)

print('Checking master dispatcher configuration of server, port')
"""
    Default server will be directed to port 8091 
"""
os.chdir(root+'/single')
conf_path = root+'/single/dispatcher/config.json'
with open (conf_path,'r') as conf_path:
    json_data=json.load(conf_path)
    server_id = json_data["server"]

print('sending prefix to the blockchain')
prefix_list = root+'/single/prefix_list.txt'
with open(prefix_list,'r') as prefix_list:
    for line in prefix_list:
        router_ip,asn,prefix = map(str.strip,line.split(';'))
        url_set = server_id+'/api/addpref'
        headers = {'content-type': 'application/json',
            'accept-encoding': 'application/json',
            'charsets': 'utf-8'}
        payload = {'ip_prefix':prefix,'ASN':asn,'exp_stat':'1'}

        response = requests.post(url=url_set,headers=headers,data=json.dumps(payload))

# # print('Sleep 5 second before Executing Monitor')
# # time.sleep(5)
# # scale_path = root+'/scale/'
# # for item in dispatcher_list:
# #     host_ip,asn = map(str.strip,item.split(';'))
# #     change_dir = scale_path+'/'+asn+'/dispatcher/'
# #     os.chdir(change_dir)
# #     print ('Executing Monitor in Router '+str(asn))
# #     subprocess.Popen(["python3",change_dir+'/monitor.py'])
# #     print ('Executing Dispatcher in Router '+str(asn))
# #     subprocess.Popen(["python3",change_dir+'/dispatcher.py'])
