#!/usr/bin/expect -f
set router_ip [lindex $argv 0]
set router_port [lindex $argv 1]
set password [lindex $argv 2]

spawn telnet $router_ip $router_port
expect "Password:"
send -- "$password\n"
expect ">"
send -- "enable\n"
expect "#"
log_file monitor.log
send -- "show ip bgp\n"
expect "#"
send -- "exit\n"


