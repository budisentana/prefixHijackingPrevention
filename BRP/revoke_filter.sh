#!/usr/bin/expect -f
set router_ip [lindex $argv 0]
set asn [lindex $argv 1]
set hop [lindex $argv 2]


spawn telnet $router_ip " 2605"
expect "Password:"
send -- "test\n"
expect ">"
send -- "enable\n"
expect "#"
send -- "conf t\n"
expect "(config)#"
send -- "router bgp $asn\n"
expect "(config-router)#"
send -- "no ip as-path access-list 120 \n"
expect "#"
send -- "router bgp $asn\n"
expect "(config-router)#"
send -- "no neighbor $hop filter-list 120 in \n"
expect "#"
send -- "no neighbor $hop route-map in_prepend in \n"
expect "#"
send -- "end\n"
expect "#"
send -- "end\n"
expect "#"
send -- "show ip bgp\n"
expect "#"
send -- "exit\n"
