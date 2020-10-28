import numpy as np
import matplotlib.pyplot as plt
import os

dirname = os.getcwd()+'/time_keeper 4 router.txt'
with open(dirname,'r') as time_file:
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    for line in time_file:
        if 'prepend --> appear' in line:
            next_line = next(time_file)
            t1.append(round(float(next_line.lstrip('>').rstrip('\n'))/100,3))
        elif 'appear --> identified' in line:
            next_line = next(time_file)
            t2.append(round(float(next_line.lstrip('*>').rstrip('\n')),3))
        elif 'appear --> neutralized' in line:
            next_line = next(time_file)
            t3.append(round(float(next_line.lstrip('**>').rstrip('\n')),3))
        elif 'identified --> neutralized' in line:
            next_line = next(time_file)
            t4.append(round(float(next_line.lstrip('***>').rstrip('\n')),3))

            
print(str(t1)+'\n')
print(str(t2)+'\n')
print(str(t3)+'\n')
print(str(t4)+'\n')


fig=plt.figure(figsize=(5,2.5))
box_plot_data=[t1,t2]
plt.boxplot(box_plot_data,notch=True,labels=['Prepend','Neutralization'],showfliers=False)
plt.ylabel('Time (second)')
# fig.savefig("/home/budi/prefixHijackingPrevention/BRP/myplot.pdf", bbox_inches='tight')
plt.show()

sumary_data= os.getcwd()+'/sumary.txt'
with open(sumary_data,'w+') as sum_data:
    sum_data.write('Neutralization time in 4 router\n')
    sum_data.write('Prepending  & Identifying  & Neutralizing \\\ \n')
    sum_data.write('(Second(*100))  & (Second)  & (Second) \\\ \n')
    for i,line in enumerate(t1) :
        sum_data.write(str(round(t1[i]*100,2))+ ' & '+ str(t2[i])+ ' & '+ str(t4[i])+ '\\\ \n')

P_avg = round(np.mean(t1)*100,3)
P_std = round(np.std(t1)*100,3)
I_avg = round(np.mean(t2),3)
I_std = round(np.std(t2),3)
with open(sumary_data,'a') as avg_data:
    avg_data.write('------------------------------------------------\\\n')
    avg_data.write('P Mean + std &  I Mean + std \n')
    avg_data.write(str(P_avg)+'+-'+str(P_std)+' & '+str(I_avg)+'+-'+str(I_std)+'\\\n')
    avg_data.write('------------------------------------------------\\\n')

P_median = round(np.median(t1)*100,3)
P_max = round(np.max(t1)*100,3)
P_min = round(np.min(t1)*100,3)
P_IQR = round((P_max-P_min),3)
I_median = round(np.median(t2),3)
I_max = round(np.max(t2),3)
I_min = round(np.min(t2),3)
I_IQR = round((I_max-I_min),3)

with open(sumary_data,'a') as avg_data:
    avg_data.write('------------------------------------------------\\\n')
    avg_data.write('Mean &  Median & std & Min & Max & IQR \n')
    avg_data.write(str(P_avg)+'&'+str(P_median)+' & '+str(P_std)+' & '+str(P_min)+' & '+str(P_max) +' & '+str(P_IQR)+'\\ \n')
    avg_data.write(str(I_avg)+'&'+str(I_median)+' & '+str(I_std)+' & '+str(I_min)+' & '+str(I_max) +' & '+str(I_IQR)+'\\ \n')
    avg_data.write('------------------------------------------------\\\n')


# fig=plt.figure(figsize=(5,2.5))
# box_plot_data=[t1,t2,t4]
# plt.boxplot(box_plot_data,notch=True,labels=['Prepending','Identifying','Neutralizing'],showfliers=False)
# plt.ylabel('Time (second)')
# # fig.savefig("/home/budi/prefixHijackingPrevention/BRP/myplot.pdf", bbox_inches='tight')
# plt.show()


# sumary_data= os.getcwd()+'/sumary.txt'
# with open(sumary_data,'w+') as sum_data:
#     sum_data.write('Neutralization time in 4 router\n')
#     sum_data.write('Prepending  & Identifying  & Neutralizing \\\ \n')
#     sum_data.write('(Second(*100))  & (Second)  & (Second) \\\ \n')
#     for i,line in enumerate(t1) :
#         sum_data.write(str(round(t1[i]*100,2))+ ' & '+ str(t2[i])+ ' & '+ str(t4[i])+ '\\\ \n')

# P_avg = round(np.mean(t1)*100,3)
# P_std = round(np.std(t1)*100,3)
# I_avg = round(np.mean(t2),3)
# I_std = round(np.std(t2),3)
# with open(sumary_data,'a') as avg_data:
#     avg_data.write('------------------------------------------------\\\n')
#     avg_data.write('P Mean + std &  I Mean + std \n')
#     avg_data.write(str(P_avg)+'+-'+str(P_std)+' & '+str(I_avg)+'+-'+str(I_std))