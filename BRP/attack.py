import os
import time
import sys
import timeit

def attack(router_ip,asn,prefix):
    attack = os.getcwd()+'/attack.sh'
    print(str(attack))
    print(router_ip+asn+prefix)
    os.system (attack +' '+ router_ip +' '+ asn +' ' + prefix)
    t_prepend = timeit.default_timer()
    with open('time_keeper.txt','a') as prepend_time:
        prepend_time.write('This is prepend time  by '+str(asn)+'\n'+ '>>'+ str(t_prepend)+'\n')


router_ip = str(sys.argv[1])
asn = str(sys.argv[2])
prefix = str(sys.argv[3])
attack(router_ip,asn,prefix)
