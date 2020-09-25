import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('Sending Data Analysis.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\t')
    for row in plots:
        x.append(int(float(row[0])))
        y.append(int(float(row[1])))

plt.plot(x,y, label='Authorization Time')
plt.xlabel('Number of Prefix')
plt.ylabel('Time in second')
plt.title('Prefix Authorization Time')
plt.legend()
plt.show()