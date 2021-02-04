import os
import shutil

dirname = os.getcwd()
with open ('node_setup.txt','r') as node_file:
    for line in node_file:
        try:
            host_name,host_ip,router,asn = map(str.strip,line.split(';'))
            shutil.rmtree(dirname+'/'+asn+'/dispatcher')        
        except :
            pass

kill_port = 'fuser -k 8091/tcp'
os.system(kill_port)