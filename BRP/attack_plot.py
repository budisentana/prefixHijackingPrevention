import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

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


# index = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10']
         
# df = pd.DataFrame({'prepend_appear (/100)': t1,
#                    'appear_identified': t2,
#                    'appear_neutralized': t3, 
#                    'identified_neutralized': t4}, index=index)
# ax = df.plot.bar(rot=0)
# ax.set_xlabel('Running #')
# ax.set_ylabel('Time (second)')
# ax.set_title('Blockjack Time using 4 Router')

# plt.show()


index2 = ['Prepending', 'Identifying', 'Neutralizing(1)', 'Neutralizing(2)']
minimum = [min(t1),min(t2),min(t3),min(t4)]
maximum =[max(t1),max(t2),max(t3),max(t4)]
average = [round((sum(t1)/len(t1)),2),round((sum(t2)/len(t2)),2),round((sum(t3)/len(t3)),2),round((sum(t4)/len(t4)),2)]
print(str(minimum))
print(str(maximum))
print(str(average))

       

df2 = pd.DataFrame({'Minimum': minimum,
                   'Average': average,
                   'Maximum': maximum}, index=index2)
ax2 = df2.plot.bar(rot=0)
ax2.set_xlabel('Category of Action')
ax2.set_ylabel('Time (second)')
ax2.set_title('Blockjack Time Min, Max and Avg of 4 Router')

plt.show()

sumary_data= os.getcwd()+'/sumary.txt'
with open(sumary_data,'w+') as sum_data:
    sum_data.write('Sumary of Neutralization time in 4 router\n')
    sum_data.write('T1 = Prepending to Disruption, T2= Disruption to Identify,\n T3 = Disruption to Neutralized, T4= Identify to Neutralized\n')
    sum_data.write('Minimum & Maximum & Average\\\ \n')
    for i, line in enumerate(minimum):
        sum_data.write(str(minimum[i])+ ' & ')
        sum_data.write(str(maximum[i])+ ' & ')
        sum_data.write(str(average[i])+ '\\\ \n')
    sum_data.write('-------------------------------------------\n')

with open(sumary_data,'a') as sum_data:
    sum_data.write('Neutralization time in 4 router\n')
    sum_data.write('T1 = Prepending to Disruption, T2= Disruption to Identify,\n T3 = Disruption to Neutralized, T4= Identify to Neutralized\n')
    sum_data.write('T1  & T2  & T3  & T4\\\ \n')
    for i,line in enumerate(t1) :
        sum_data.write(str(t1[i])+ ' & '+ str(t2[i])+ ' & '+ str(t3[i])+ ' & '+ str(t4[i])+ '\\\ \n')


