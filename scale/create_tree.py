import logging
import networkx as nx
import matplotlib.pyplot as plt 

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
    for x in list_tree:
        D,L,R = map(str.strip,x.split(','))
        D = (D.lstrip('(D:'))
        L = (L.lstrip('L:'))
        R = (R.lstrip('R:').rstrip(')'))
        print(D,L,R)
        if (L and R) not in ('None'):
            pairs.append('('+str(D)+';'+str(L)+')')
            pairs.append('('+str(D)+';'+str(R)+')')
        elif R in ('None') and L not in ('None'):
            pairs.append('('+str(D)+';'+str(L)+')')

    print(str(pairs))

def main():
    data = range(1,20)
    list_tree = build_tree_breadth_first(data)
    create_pairs(list_tree)
    # print ('Root is:', root)

if __name__ == '__main__':
    main()