import os
import numpy as np

sum_path = '/home/budi/prefixHijackingPrevention/multiple/running_result/time_summary_new.txt'
dirname = '/home/budi/prefixHijackingPrevention/multiple/running_result/'

def Average(lst): 
    return sum(lst) / len(lst) # find average of each element neutralization

"""summarized result"""
def sum_per_file(file_path,router_num_item):
    """Find the list of prefix hijacked sent by attacker"""
    prefix_list =[]
    with open (file_path,'r') as time_file:
        iter = 0
        for i,line in enumerate(time_file):
            iter = i
            if "-----" in line:
                break
            # print(str(line))
            host,asn,prefix,start,time = map(str.strip,line.split(';'))
            prefix_list.append(asn+';'+prefix+';'+time)

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
        hijacked_p.append(h_time) # take the first attack time
        with open (file_path,'r') as rec_file:
            for x,line in enumerate(rec_file): 
                if x > iter :    # get the line until --- 
                    c_asn,c_prefix,c_stat, c_time = map(str.strip,line.split(';'))
                    if c_asn in h_asn and c_prefix in h_prefix  and c_stat in 'P':
                        hijacked_p.append(float(c_time))
                        hijacked_n.append(float(c_time)) # need it to sum (N-P)
                        hijack_num+=1
                    if c_asn in h_asn and c_prefix in h_prefix  and c_stat in 'N':
                        hijacked_n.append(float(c_time))
        #array of prepending and neutralization            
        if len(hijacked_p)>1:
            hijacked.append(hijacked_p) # remove the time that only appear in Start time
        if len (hijacked_n)>1:
            neutral_list.append(hijacked_n)
    """
        Summarized prepend time
        S = start time is used as refference
    """
    diff_list = []
    avg_list = []
    # std_list=[]
    for z, item in enumerate(hijacked):
        avg = 0
        item_dif=[]
        for y in item :
            item_dif.append(float(y)) # need it to create float value for each item in the list
        
        prep_time_per_item = np.diff(item_dif)
        # print(len(prep_time_per_item))
        """This part is use if the each element of attack sequence are count in average"""
        # avg = Average(prep_time_per_item)
        # avg_list.append(avg) # append the average prepend on each item (same prefix same asn with different path attack)    
        """This part is use if the each element of attack sequence are count in addition"""
        add = np.sum(prep_time_per_item)
        avg_list.append(add) # append the average prepend on each item (same prefix same asn with different path attack)    
        # std_per_item = np.std(prep_time_per_item) # just prepare for per item std
        # if std_per_item !=0:
        # std_list.append(std_per_item)
        
    # print(std_list)
    # print(avg_list)

    prepend_avg = round(Average(avg_list),3)
    # prepend_std = round(Average(std_list),3)
    # print(prepend_avg)
    # print(prepend_std)

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
            add_elemen = np.sum(diff_item_list) # adding the time for each elmeent item neutralization
            avg_neutral_list.append(add_elemen)
            # avg_element = Average(diff_item_list) # find average of each element neutralization
            # avg_neutral_list.append(avg_element)
        else:
            diff_item_list=0
        diffn_list.append(diff_item_list)
    neutral_avg = round(Average(avg_neutral_list),3)
    neutral_std = round((np.std(avg_neutral_list)),3)

    # print(diffn_list)
    # print(avg_neutral_list)
    # print(neutral_avg)

    res = (str(router_num_item)+'&'+str(len(prefix_list))+'&'+str(len(avg_neutral_list))+'&'+str(hijack_num)+ \
        '&'+ str(prepend_avg)+ '&'+ str(neutral_avg)) #+ ' & ' + str(prepend_std)+ ' & ' + str(neutral_std)+ '\\\ \n')
    return res



"""Find  all the result directory"""
def find_dir(dir_path):
    dir_list=[]
    router_num =[]
    for root,dirs,files in os.walk(dirname):
        for dir in dirs:
            dir_item = os.path.join(root,dir)
            router_num_item = dir_item[-9:].strip('_router')
            dir_list.append(dir_item)
            router_num.append(router_num_item)
    return dir_list,router_num

""""Retrieve the file in the result list directory"""
def sum_result(dir_list,router_num):
    res_list=[]
    for i,dir_item in enumerate(dir_list):
        router_num_item = router_num[i]
        for root,dirs,files in os.walk(dir_item):
            for file in files:
                file_path = os.path.join(root,file)
                if file_path[-4:] in '.txt':
                    # print(file_path)
                    result = sum_per_file(file_path,router_num_item)
                    res_list.append(result)
    """ Write the summary to file"""
    with open (sum_path,'w') as sum_file:
        sum_file.write ('Router&Send&Receive&impact&Prep&Neutral \n')
        for line in res_list:
            sum_file.write(line+'\n')


def main():
    dir_list,router_num = find_dir(dirname)
    sum_result(dir_list,router_num)

if __name__ == '__main__':
    main()