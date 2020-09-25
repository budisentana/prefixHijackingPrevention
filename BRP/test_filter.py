import os
   
keeper = os.getcwd()+'/time_keeper.txt'
global last_line
last_line = ''
t_prepend = ''
with open (keeper,'r') as keeper_file:
    for num,last_line in enumerate(keeper_file):
        pass           
print('with content :'+str(last_line))
print('with NUM :'+str(num))
line_no = [num-9,num-3]
print(str(line_no))

if '>>' in last_line:
    print('test')
    t_prepend = float(last_line.lstrip(">>").rstrip("\n"))
else:
    with open(keeper) as keeper_file :
        next_attack=[]
        for nums, line in enumerate(keeper_file):
            if nums in line_no :
                next_attack.append(line.lstrip('>').rstrip('\n'))
        print('this is next '+str(next_attack))
                # t_prepend = float(next_attack.lstrip(">>").rstrip("\n"))
    # with open(keeper,'a') as keeper_file :
    #     keeper_file.write('This is next attack by \n'+str(next_attack)+'\n')
    #         # print('this is last line 1'+str(last_line))

# print('this is tprepend'+str(t_prepend))
# prepend_to_appear = t_appear - t_prepend
# identification_time = t_identified - t_appear
# neutralized_from_identified = t_neutralized - t_identified
# neutralized_from_appear = t_neutralized - t_appear