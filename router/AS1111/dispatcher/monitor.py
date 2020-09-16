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
    monitor_sh = dirname+'/monitor.sh'
    print(file)
    with open(file,'w'):
        pass
    os.system (get_prefix + router_ip +bgp_port + password)
    os.system (monitor_sh)


check_config()
schedule.every().second.do(run_monitor)

while True:
    schedule.run_pending()
    time.sleep(3)