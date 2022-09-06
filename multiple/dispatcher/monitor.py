import os
import json
import re
import schedule
import time

dirname = os.getcwd()
router_ip =''
bgp_port = ''
asn = ''
password = ''
def check_config():
    try:
        json_conf = dirname + "/config.json"
        global bgp_port,asn,password,router_ip
        with open(json_conf,"r") as json_conf:          
            jc = json.load(json_conf)
            asn = jc["asn"]
            router_ip = jc["router_ip"]
            bgp_port = jc["bgp_port"]
            password = jc["password"]
    except Exception as error:
        print(error)

def run_monitor():
    file = dirname+'/monitor.log'
    get_prefix = dirname+'/getPrefix.sh'
    capture_file = dirname+'/capture.txt'
    # monitor_sh = dirname+'/monitor.sh'
    # print(file)
    with open(file,'w'):
        pass
    os.system (get_prefix + router_ip +bgp_port + password)
    # os.system (monitor_sh)
    line_list=[]
    with open(file,'r') as table:
        for i,line in enumerate(table):
            if line[0] in ('*') :
                stat = line[0:2]
                prefix = line[3:20]
                hope = line[20:35]
                path = str(line [55:]).strip()
                x_path = path.split(' ')
                path_lenght = len(x_path)
                prefix.strip()
                if  not prefix.isspace():
                    sub_pref = prefix
                else:
                    prefix = sub_pref
                
                prefix = prefix.strip()
                hope = hope.strip()
                x_path = path.split(' ')
                # print(stat+';'+prefix+';'+hope+';'+str(x_path[path_lenght-2])+';'+path)
                line_list.append(stat+';'+prefix+';'+hope+';'+str(x_path[path_lenght-2]))

    with open (capture_file,'w+') as capture:
        for line in line_list:
            capture.write(line+'\n')
# def run_monitor():
#     file = dirname+'/monitor.log'
#     get_prefix = dirname+'/getPrefix.sh'
#     monitor_sh = dirname+'/monitor.sh'
#     print(file)
#     with open(file,'w'):
#         pass
#     os.system (get_prefix + router_ip +bgp_port + password)
#     os.system (monitor_sh)


check_config()
schedule.every().second.do(run_monitor)

while True:
    schedule.run_pending()
    time.sleep(1)