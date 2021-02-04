import os
import numpy as np

def Average(lst): 
    return sum(lst) / len(lst) # find average of each element neutralization

man_path = '/home/budi/prefixHijackingPrevention/scale/running_result/manual summary.txt'
sum_table = '/home/budi/prefixHijackingPrevention/scale/running_result/sum_table.txt'
plot_source = '/home/budi/prefixHijackingPrevention/scale/running_result/plot_source.txt'



"""Find the list of router grouped by number of router"""
router_list =[]
with open (man_path,'r') as man_file:
    for i,line in enumerate(man_file):
        if i > 1 and not line.isspace(): # skip the header
            line_s = line.strip().rstrip('\\')
            router, sent,rec,attack,prep,neut = map(str.strip,line_s.split(' & '))
            if router not in router_list:
                router_list.append(router)

# print(router_list)

"""Summarize aggregate value of the table"""
sum_sent = []
sum_rec = []
sum_att = []
sum_p = []
sum_n = []
for item in router_list:
    x_sent = []
    x_rec = []
    x_att = []
    x_p = []
    x_n = []
    avg_sent=[]
    avg_rec=[]
    avg_att=[]
    avg_p =[]
    avg_n = []
    with open (man_path) as man_file:
        for i,line in enumerate(man_file):
            if i >= 1 and not line.isspace():
                line_s = line.strip().rstrip('\\')
                router,sent,rec,attack,prep,neut = map(str.strip,line_s.split(' & '))
                if item == router :
                    # print(sent)
                    x_sent.append(sent)
                    x_rec.append(rec)
                    x_att.append(attack)
                    x_p.append(prep)
                    x_n.append(neut)
        # print(x_n)
        # xxx = np.array(x_n).astype(float).tolist()       
        # # xxx = map(float,x_sent)
        # print(xxx)
        # avg_sent=Average(xxx)
        avg_sent=Average(np.array(x_sent).astype(float).tolist())
        avg_rec=Average(np.array(x_rec).astype(float).tolist())
        avg_att =Average(np.array(x_att).astype(float).tolist())
        avg_p = Average(np.array(x_p).astype(float).tolist())
        avg_n = Average(np.array(x_n).astype(float).tolist())
    sum_sent.append(avg_sent)
    sum_rec.append(avg_rec)
    sum_att.append(avg_att)
    sum_p.append(round(avg_p,3))
    sum_n.append(round(avg_n,3))

with open(plot_source,'w') as source:
    source.write ('Router & Sent & Receive & Attack & Prepend & Neutralize \\\ \n')
    for i, item in enumerate(router_list):
        source.write (str(item) + ' & ' + str(sum_sent[i])+ ' & ' + str(sum_rec[i])+ ' & ' + str(sum_att[i])+ ' & ' + str(sum_p[i])+ \
             ' & ' + str(sum_n[i])+'\\\ \n')
        print (str(item) + ' & ' + str(sum_sent[i])+ ' & ' + str(sum_rec[i])+ ' & ' + str(sum_att[i])+ ' & ' + str(sum_p[i])+ ' & ' + str(sum_n[i]))

