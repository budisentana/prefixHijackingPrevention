import numpy as np
import matplotlib.pyplot as plt
import matplotlib



plot_source = '/home/budi/prefixHijackingPrevention/scale/running_result/plot_source.txt'
prep = []
neutral =[]
with open (plot_source,'r') as source:
    for i,line in enumerate(source):
        if i >=1 and not line.isspace():
            router,sent,receive,impact,pre,neu = map(str.strip,line.split('&'))
            print(pre)
            neu = neu.rstrip('\\')
            print(neu)
            prep.append(float(pre))
            neutral.append(float(neu))

N = len(prep)
prepend = []
for item in prep:
    prepend.append(item/10)
print(prepend)
print(neutral)
# menStd = (2, 3, 4, 1, 2)
# womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence
plt.figure(figsize=(5,4))
# fig = matplotlib.pyplot.gcf()
# fig.set_size_inches(5, 4)

p1 = plt.bar(ind, prepend, width)
p2 = plt.bar(ind, neutral, width,
             bottom=prepend)
plt.ylabel('Time (second)')
plt.xlabel('Number of Router ')
plt.xticks(ind, ('20', '30', '40', '50', '60'))
plt.yticks(np.arange(0, 4, 0.5))
plt.legend((p1[0], p2[0]), ('prepending', 'neutralization'))

plt.show()