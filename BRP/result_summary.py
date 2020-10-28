import os
import matplotlib.pyplot as plt

auth_path = os.getcwd()+'/record_data_auth.txt'
verif_path = os.getcwd()+'/record_data_ver.txt'
find_line=['50','100','150','200','300','500','1000']
number_of_prefix=[]
exe_time_auth=[]
exe_time_ver=[]
avg_auth=[]
avg_ver=[]

with open(auth_path,'r') as auth_file:
    for line in auth_file:
        num,record = map(str.strip,line.split(';'))
        if  num in find_line:
            number_of_prefix.append(num)
            exe_time_auth.append(round(float(record),2))
            avg_auth.append(round((float(record)/int(num)),2))

with open(verif_path,'r') as ver_file:
    for line in ver_file:
        num,record = map(str.strip,line.split(';'))
        if  num in find_line:
            exe_time_ver.append(round(float(record),2))
            avg_ver.append(round((float(record)/int(num)),2))


res_path = os.getcwd()+'/sum_auth_ver.txt'
with open (res_path,'w+') as res:
    for num,line in enumerate(number_of_prefix):
        res.write(str(number_of_prefix[num])+' & '+ str(avg_auth[num])+' & '+ str(exe_time_auth[num])+' & '+ str(avg_ver[num])+' & '+ str(exe_time_ver[num])+'\\\ \n')


print(exe_time_ver)
# plt.plot(number_of_prefix,exe_time_ver)
# plt.show()