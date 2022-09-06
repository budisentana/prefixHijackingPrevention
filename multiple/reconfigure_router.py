import os 
import random
import time
import timeit

""" Use to revoke the hijacking from the attacker router"""


print('Find The Attacker list and revoke hijacking')
dirname = os.getcwd()
attacker_list = dirname+'/attacker_list.txt'
with open(attacker_list,'r') as dlist:
    for line in dlist:
        host,asn,prefix = map(str.strip,line.split(';'))
        # prefix_dict.append(prefix)
        print(prefix)
        shell_path = os.getcwd()+'/revoke_network.sh'
        os.system(shell_path + ' '+ host +' '+asn + ' '+prefix)


"""Restore the routing table in the dispatcher """ 
print('Clear the Inbound filtering from the BGP')
""""Find the first node or root"""
node_l = []
node_list = dirname+'/node_setup.txt'
print(node_list)
with open (node_list) as dlist:
    for item in dlist:
        print(item)
        host,ip,asn,prefix = map(str.strip,item.split(';'))
        node_l.append (host)
"""Find the root"""
root = node_l[0].strip('host')
print(root)

"""Open the list of the pairs"""
peer_setup = dirname+'/peer_setup.txt'
root_edge =[]
with open (peer_setup,'r') as peer:
    for item in peer:
        src,s_ip,dest,d_ip = map(str.strip,item.split(';'))
        if src in root:
            no_neighbor = os.getcwd()+'/no_peer.sh'
            os.system(no_neighbor + ' '+ s_ip +' '+src + ' '+d_ip+ ' '+dest)
            print ("Sleep 3 second before reconfigure peering")
            time.sleep(3)
            neighbor1 = os.getcwd()+'/peer_conf.sh'
            os.system(neighbor1 + ' '+ s_ip +' '+src + ' '+d_ip+ ' '+dest)
            print ("Sleep 3 second before reconfigure peering")
            time.sleep(3)
            neighbor2 = os.getcwd()+'/peer_conf.sh'
            os.system(neighbor2 + ' '+ d_ip +' '+dest + ' '+s_ip+ ' '+src)
