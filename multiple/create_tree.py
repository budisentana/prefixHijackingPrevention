import logging
import networkx as nx
import matplotlib.pyplot as plt 
import random

node_setup = '/home/budi/prefixHijackingPrevention/multiple/node_setup.txt'
peer_setup = '/home/budi/prefixHijackingPrevention/multiple/peer_setup.txt'
branch = '/home/budi/prefixHijackingPrevention/multiple/branch_list.txt'


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Tree(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        left = None if self.left is None else self.left.data
        right = None if self.right is None else self.right.data
        return '(D:{}, L:{}, R:{})'.format(self.data, left, right)

def build_tree_breadth_first(sequence):
    # Create a list of trees
    forest = [Tree(x) for x in sequence]

    # Fix up the left- and right links
    count = len(forest)
    for index, tree in enumerate(forest):
        left_index = 2 * index + 1
        if left_index < count:
            tree.left = forest[left_index]

        right_index = 2 * index + 2
        if right_index < count:
            tree.right = forest[right_index]

    list_tree=[]
    for index, tree in enumerate(forest):
        list_tree.append('{}'.format(tree))
    # print(str(pairs))
        # logger.debug('[{}]: {}'.format(index, tree))
    return list_tree  # root
    # return forest[0]  # root

def create_pairs(list_tree):
    pairs=[]
    branch_list=[]
    for x in list_tree:
        D,L,R = map(str.strip,x.split(','))
        D = (D.lstrip('(D:'))
        L = (L.lstrip('L:'))
        R = (R.lstrip('R:').rstrip(')'))
        print(D,L,R)
        if (L and R) not in ('None'):
            pairs.append('('+str(D)+';'+str(L)+')')
            pairs.append('('+str(D)+';'+str(R)+')')
            branch_list.append(D)
        elif R in ('None') and L not in ('None'):
            pairs.append('('+str(D)+';'+str(L)+')')
            branch_list.append(D)

    """Connecting the branch to create multiple path"""
    addition =[]
    for i,k in zip(branch_list[0::2], branch_list[1::2]):
        addition.append(i)
        pairs.append ('('+str(int(i)+1)+';'+str(int(k)+1)+')')
        if len(addition)>2:
            break

    with open (branch,'w') as branch_file:
        for item in branch_list:
            branch_file.write(item+'\n')
    print(str(pairs))
    return pairs

def create_random_ip(n):
    ip_list =[]
    print('Creating '+str(n)+' random IP address for the node')
    while len(ip_list) < n:
        x1 = 99
        x2 = random.randint(0,255)
        x3 = random.randint(0,255)        
        x4 = random.randint(0,255)
        result = ".".join(map(str,([x1,x2,x3,x4])))
        if result not in ip_list:    
            ip_list.append(result)
    # print(ip_list)
    return ip_list

def node_config(data,ip_list):
    # preparing for node configuration
    node_att =[]
    for i,node in enumerate(data):
        host_name = 'host'+str(node)
        host_ip = ip_list[i]
        as_name = 'AS'+str(node)
        router_name = 'router'+str(node)
        node_att.append(host_name+';'+host_ip+';'+router_name+';'+as_name)

    #write node configuration to file
    print('Writing the node configuration to the file ')
    with open(node_setup,'w') as node_seed:
        for row in node_att :
            node_seed.write(row+'\n')
    return node_att

def peer_config(list_pair,ip_list):
    #Preparing for Peer configuration
    peer_att=[]
    for x,edge in enumerate(list_pair):
        # print(edge)
        peer = str(edge)
        peer_x, peer_y = map(str.strip,peer.split(';'))
        peer_x = int(peer_x.lstrip('(').rstrip('\n'))
        peer_y = int(peer_y.rstrip(')'))
        ip_x = ip_list[peer_x-1]
        ip_y = ip_list[peer_y-1]
        peer_att.append(str(peer_x)+';'+str(ip_x)+';'+str(peer_y)+';'+str(ip_y))
        peer_att.append(str(peer_y)+';'+str(ip_y)+';'+str(peer_x)+';'+str(ip_x))
        # print('this is peer x :' +str(peer_x) +'and peer y :' + str(peer_y)+ 'this is x' +ip_x+'this is ip y'+ip_y)

    print('Writing the Peer Configuration to the file')
    with open(peer_setup,'w') as peer_seed:
        for peer in peer_att:
            peer_seed.write(peer+'\n')


def main():
    data = range(1,21)   
    list_tree = build_tree_breadth_first(data)
    list_pair = create_pairs(list_tree)
    ip_list=create_random_ip(len(data))
    node_config(data,ip_list)
    peer_config(list_pair,ip_list)
    # print ('Root is:', root)

if __name__ == '__main__':
    main()