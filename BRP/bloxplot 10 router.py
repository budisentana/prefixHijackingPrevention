import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

dirname = os.getcwd()+'/time_keeper 10 router.txt'
with open(dirname,'r') as time_file:
    P1=[]
    P2=[]
    P3=[]
    I1=[]
    I2=[]
    I3=[]
    N1=[]
    N2=[]
    N3=[]
    P = I = N = 1
    for line in time_file:
        if 'prepend --> appear' in line and P==1:
            next_line = next(time_file)
            P1.append(round(float(next_line.lstrip('>').rstrip('\n'))/100,3))
            P=P+1
        elif 'prepend --> appear' in line and P==2:
            next_line = next(time_file)
            P2.append(round(float(next_line.lstrip('>').rstrip('\n'))/100,3))
            P=P+1
        elif 'prepend --> appear' in line and P==3:
            next_line = next(time_file)
            P3.append(round(float(next_line.lstrip('>').rstrip('\n'))/100,3))
            P=1
        elif 'appear --> identified' in line and I == 1:
            next_line = next(time_file)
            I1.append(round(float(next_line.lstrip('*>').rstrip('\n')),3))
            I = I+1
        elif 'appear --> identified' in line and I == 2:
            next_line = next(time_file)
            I2.append(round(float(next_line.lstrip('*>').rstrip('\n')),3))
            I = I+1
        elif 'appear --> identified' in line and I == 3:
            next_line = next(time_file)
            I3.append(round(float(next_line.lstrip('*>').rstrip('\n')),3))
            I = 1
        elif 'identified --> neutralized' in line and N==1:
            next_line = next(time_file)
            N1.append(round(float(next_line.lstrip('***>').rstrip('\n')),3))
            N=N+1
        elif 'identified --> neutralized' in line and N==2:
            next_line = next(time_file)
            N2.append(round(float(next_line.lstrip('***>').rstrip('\n')),3))
            N=N+1
        elif 'identified --> neutralized' in line and N==3:
            next_line = next(time_file)
            N3.append(round(float(next_line.lstrip('***>').rstrip('\n')),3))
            N=1


# print(str(P1)+'\n')
# print(str(P2)+'\n')
# print(str(P3)+'\n')
sumary_data= os.getcwd()+'/sumary 10 router.txt'
with open(sumary_data,'w+') as sum_data:
    sum_data.write('Sumary of Neutralization time in 10 router\n')
    sum_data.write('P1 & I1 & N1 & P2 & I2 & N2 & P3 & I3 & N3 \\\ \n')
    for i, line in enumerate(P1):
        sum_data.write(str(P1[i])+ ' & '+str(I1[i])+ ' & '+str(N1[i])+ ' & '+str(P2[i])+ ' & '+str(I2[i])+ ' & '+str(N2[i])+ ' & '+
        str(P3[i])+ ' & '+str(I3[i])+ ' & '+str(N3[i])+ ' & '+ '\\\ \n')
    sum_data.write('-------------------------------------------\n')

with open(sumary_data,'a') as sum_data:
    stat_all = [P1,I1,N1,P2,I2,N2,P3,I3,N3]
    sum_data.write('Mean & Median & std & Max & Min & IQR \\\ \n')
    for num,data in enumerate(stat_all):
        mean_all = round(np.mean(stat_all[num]),3)
        media_all = round(np.median(stat_all[num]),3)
        std_all = round(np.std(stat_all[num]),3)
        max_all = round(np.max(stat_all[num]),3)
        min_all = round(np.min(stat_all[num]),3)
        IQR_all = max_all-min_all
        print(str(mean_all)+' & '+ str(media_all)+' & '+str(std_all)+' & '+str(max_all)+' & '+str(min_all)+' & '+str(IQR_all)+'\n')
        sum_data.write(str(mean_all)+' & '+ str(media_all)+' & '+str(std_all)+' & '+str(max_all)+' & '+str(min_all)+' & '+str(IQR_all)+' \\\ \n')
    



fig=plt.figure(figsize=(5,2.5))
box_plot_data=[P1,I1,N1,P2,I2,N2,P3,I3,N3]
plt.boxplot(box_plot_data,notch=True,labels=['P1','I1','N1','P2','I2','N2','P3','I3','N3'],showfliers=False)
plt.ylabel('Time (second)')
# fig.savefig("/home/budi/prefixHijackingPrevention/BRP/myplot.pdf", bbox_inches='tight')
plt.show()

