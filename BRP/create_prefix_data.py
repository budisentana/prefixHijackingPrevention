import random
import timeit
import os


randomlist = []
for i in range(0,1000):
    n = random.randint(10,80000)
    randomlist.append(n)

source = os.getcwd()+'/caida prefix2as.txt'
data_set = os.getcwd()+'/data_to_test.txt'
data_to_print=[]
with open (source,'r') as myfile:
    for num,line in enumerate(myfile):
        if num in randomlist:
            prefix,max_long,asNumber = map(str.strip,line.split('	'))
            row = str(prefix)+'/'+max_long+';'+asNumber
            print(row)
            with open (data_set,'a') as data_s:
                data_s.write(row+'\n')
        

