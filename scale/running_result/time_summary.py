import os
import numpy as np

def Average(lst): 
    return sum(lst) / len(lst) # find average of each element neutralization

sum_path = '/home/budi/prefixHijackingPrevention/scale/running_result/time_summary.txt'
dirname = '/home/budi/prefixHijackingPrevention/scale/running_result/60_router/time_note5.txt'


# for root,dirs,files in os.walk(dirname):
#     for file in files:
#         if file in ('time_note.txt'):
#             path = os.path.abspath(file)
#             print(str(path)) 

"""Find the list of prefix hijacked sent by attacker"""
prefix_list =[]
with open (dirname,'r') as time_file:
    iter = 0
    for i,line in enumerate(time_file):
        iter = i
        if "-----" in line:
            break
        # print(str(line))
        host,asn,prefix,start,time = map(str.strip,line.split(';'))
        prefix_list.append(asn+';'+prefix+';'+time)


print(iter)
""" Find the time list based on the prefixes
    grouped it into prepend and neutralization array
"""
hijacked =[]
hijack_num = 0
neutral_list=[]
for i, item in enumerate(prefix_list):
    hijacked_p =[]
    hijacked_n =[]
    h_asn,h_prefix,h_time = map(str.strip,item.split(';'))
    hijacked_p.append(h_time)
    with open (dirname,'r') as rec_file:
        for x,line in enumerate(rec_file):
            if x > iter :
                c_asn,c_prefix,c_stat, c_time = map(str.strip,line.split(';'))
                if c_asn in h_asn and c_prefix in h_prefix  and c_stat in 'P':
                    hijacked_p.append(float(c_time))
                    hijacked_n.append(float(c_time))
                    hijack_num+=1
                if c_asn in h_asn and c_prefix in h_prefix  and c_stat in 'N':
                    hijacked_n.append(float(c_time))
                
    hijacked.append(hijacked_p)
    neutral_list.append(hijacked_n)

"""
    Summarized prepend time
    S = start time is used as refference
"""
diff_list = []
avg_list = []
for z, item in enumerate(hijacked):
    avg = 0
    item_dif=[]
    for y in item :
        item_dif.append(float(y))

    if len(item_dif) > 1:
        xitem = np.diff(item_dif)
        avg = Average(xitem)
        avg_list.append(avg)    
    else:
        xitem = 0
    diff_list.append(xitem)

# for line in diff_list:
#     print(line)

# print(avg_list)

prepend_avg = round(Average(avg_list),3)
# print(prepend_avg)

""" Summarize Neutralization time
    Substract the pair (Prepend:Neutralization) of element in the list 
"""
diffn_list=[] # list of average with 0
avg_neutral_list=[] # list of average without 0 
for line in neutral_list:
    diff_item_list = []
    if len(line) > 0:
        # print(line)
        for z, item in enumerate(line):
            if z % 2 !=0: # even substract by odd item
                diff_item = item-line[z-1] # substract event item with odd item (2-1) (N-P)
                diff_item_list.append(diff_item) # add substraction result to list
        avg_element = Average(diff_item_list) # find average of each element neutralization
        avg_neutral_list.append(avg_element)
    else:
        diff_item_list=0
    diffn_list.append(diff_item_list)
neutral_avg = round(Average(avg_neutral_list),3)

# print(diffn_list)
# print(avg_neutral_list)
# print(neutral_avg)

""" Write the summary to file"""
with open (sum_path,'a') as sum_file:
    sum_file.write (dirname+'\n')
    sum_file.write ('Prefix Sent  & Prefix Received & Attack Received & avg Prepending & Avg Neutralization \\\ \n')
    sum_file.write ('>'+str(len(prefix_list))+' & '+str(len(avg_neutral_list))+' & '+str(hijack_num)+' & '+ str(prepend_avg)+ ' & '+ str(neutral_avg)+'\\\ \n')