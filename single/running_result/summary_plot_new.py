import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import csv


plot_source = '/home/budi/prefixHijackingPrevention/single/running_result/time_summary_new.txt'
write_file =  '/home/budi/prefixHijackingPrevention/single/running_result/table_sum.txt'
write_csv =  '/home/budi/prefixHijackingPrevention/single/running_result/single.csv'
prep = []
neutral =[]

pd_source = pd.read_table(plot_source,delimiter = '&')
pd_source['std_prep'] = pd_source.groupby('Router')['Prep'].transform(np.std)
pd_source['std_neu'] = pd_source.groupby('Router')['Neutral '].transform(np.std)
group_by_router = pd_source.groupby('Router').mean().round(3).reset_index()
print(group_by_router.round(3))
# print(pd_source)

group_by_router.to_csv(write_file,sep='&',index=None)
group_by_router.to_csv(write_csv,sep='&',index=None)


label = group_by_router['Router']
prepend = group_by_router['Prep'].div(10)
neutral = group_by_router['Neutral ']
std_prep = group_by_router['std_prep'].div(10)
std_neu = group_by_router['std_neu']
N = len(prepend)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence
plt.figure(figsize=(5,4))
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(5, 3.8)

p1 = plt.bar(ind, prepend, width,yerr=std_prep)
p2 = plt.bar(ind, neutral, width,yerr=std_neu,bottom=prepend)
plt.ylabel('Time (second)')
plt.xlabel('Number of Router ')
plt.xticks(ind, label)
plt.yticks(np.arange(0, 11, 1))
plt.legend((p1[0], p2[0]), ('prepending', 'neutralization'))

plt.savefig('/home/budi/prefixHijackingPrevention/single/running_result/single_path_attack.pdf')
# plt.show()