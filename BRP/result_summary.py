import os

auth_path = os.getcwd()+'/record_data_auth.txt'
find_line=['50','100','150','200','300','500','1000']
number_of_prefix=[]
execution_time=[]
line_avg=[]

with open(auth_path,'r') as auth_file:
    for line in auth_file:
        num,record = map(str.strip,line.split(';'))
        if  num in find_line:
            number_of_prefix.append(num)
            execution_time.append(round(float(record),2))
            line_avg.append(round((float(record)/int(num)),2))

total_avg = sum(line_avg)/len(line_avg)
print(total_avg)
for num,line in enumerate(number_of_prefix):
    print(str(number_of_prefix[num]+' & '+str(execution_time[num])+' & '+str(line_avg[num])+' \n'))