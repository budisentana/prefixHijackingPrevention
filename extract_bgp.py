import os
# import unidecode

log_table = '/home/budi/prefixHijackingPrevention/monitor.log'

sub_pref = ' '
header = 6
with open(log_table,'r') as table:
    for i,line in enumerate(table):
        if line[0] in ('*') :
            # x,y,z,f,g,h,i = map(str.strip,line.split(' '))
            # print(x)
            # source = line.split("          ")[0].split("      ")[0]#.split("  ")[1]
            stat = line[0:2]
            prefix = line[3:20]
            hope = line[20:35]
            path = str(line [55:]).strip()
            x_path = path.split(' ')
            path_lenght = len(x_path)
            prefix.strip()
            if  not prefix.isspace():
                sub_pref = prefix
            else:
                prefix = sub_pref
            
            prefix = prefix.strip()
            x_path = path.split(' ')
            print(stat+';'+prefix+';'+hope+';'+str(x_path[path_lenght-2])+';'+path)
            # print(len(x_path))
            
            # print(line[20:35])