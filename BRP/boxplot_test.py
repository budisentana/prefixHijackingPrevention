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
box_plot_data=[t1,t2,t4]
plt.boxplot(box_plot_data,notch=True,labels=['Prepending','Identifying','Neutralizing'],showfliers=False)
plt.ylabel('Time (second)')
# fig.savefig("/home/budi/prefixHijackingPrevention/BRP/myplot.pdf", bbox_inches='tight')
plt.show()

# sumary_data= os.getcwd()+'/sumary.txt'
# with open(sumary_data,'a') as sum_data:
#     sum_data.write('Neutralization time in 4 router\n')
#     sum_data.write('Prepending  & Identifying  & Neutralizing \\\ \n')
#     sum_data.write('(Second(*100))  & (Second)  & (Second) \\\ \n')
#     for i,line in enumerate(t1) :
#         sum_data.write(str(t1[i])+ ' & '+ str(t2[i])+ ' & '+ str(t4[i])+ '\\\ \n')