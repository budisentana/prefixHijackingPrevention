#!/usr/bin/expect -f
set timeout -1
set my_prefix [lindex $argv 0]
spawn /bin/bash  

send -- "docker exec -it router1 telnet localhost 2605\n"
expect "Password:"
send -- "test\n"
expect ">"
send -- "enable\n"
expect "#"
send -- "show ip bgp\r"
expect "#"

#Prefix=$( awk '{print $2}' | head -n -2 | tail -n +7)
#Path=$( 'show ip bgp' | awk '{print $6}' | head -n -2 | tail  -n +7)
#LIST=$(paste -d';' <(echo "$Prefix")  <(echo "$Path")>result.txt)
#send -- "end\n"
#expect "#"
#send -- "exit\n"
