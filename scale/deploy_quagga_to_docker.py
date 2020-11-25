import plotly.graph_objects as go
import networkx as nx
import random
import os

print('Creating Docker container Network ')
docker_net = 'docker network create --subnet=99.0.0.0/8 blockjack-bgp-net'
print(str(docker_net))
os.system(docker_net)

with open('node_setup.txt','r') as node_conf:
    for node in node_conf:
        host_name,host_ip,router_name,as_name = map(str.strip,node.split(';'))

        print(host_name,host_ip,router_name,as_name)
        print('Creating Directory of '+as_name )
        mk_dir = 'mkdir '+as_name
        os.system(mk_dir)
        print('Copying quagga configuration file to '+as_name)
        cp_conf = 'cp quagga.conf `pwd`/'+as_name+'/quagga.conf'
        os.system(cp_conf)

        print('Run '+router_name+ ' on Docker Container in Detach mode')
        print('Assigning IP Address ' +host_ip + ' to the Router')
        print('Attaching router to the network')
        docker_run = 'docker run --name '+ router_name+' --net blockjack-bgp-net --ip '+ host_ip+' --hostname='+host_name+' -d -v `pwd`/'+as_name+':/etc/quagga:rw pierky/quagga'
        print(docker_run)
        os.system(docker_run)

        print('Configure routername, BGP ASN, BGP ID for '+str(router_name))
        as_no = as_name.lstrip('AS').rstrip('\n')
        print(as_no)
        shell_path = os.getcwd()+'/conf_node.sh '
        os.system(shell_path + host_ip + ' '+router_name+ ' '+as_no)

with open('peer_setup.txt','r') as peer_conf:
    for peer in peer_conf:
        peer_x, ip_x, peer_y, ip_y = map(str.strip,peer.split(';'))

        print('Peering AS '+peer_x+ ' with AS  '+peer_y)
        shell_path = os.getcwd()+'/peer_conf.sh'
        os.system(shell_path + ' '+ ip_x +' '+peer_x + ' '+ip_y+  ' '+peer_y)
        print('Peering AS '+peer_y+ ' with AS  '+peer_x)
        os.system(shell_path + ' '+ ip_y + ' '+peer_y + ' '+ip_x+ ' '+peer_x)



