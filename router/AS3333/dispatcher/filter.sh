#!/usr/bin/expect -f
set router_ip [lindex $argv 0]
set bgp_port [lindex $argv 1]
# set password [lindex $argv 2]
set password "test"
set hop [lindex $argv 3]
set path [lindex $argv 4]
set asn [lindex $argv 5]

spawn telnet $router_ip $bgp_port
expect "Password:"
send -- "$password\n"
expect ">"
send -- "enable\n"
expect "#"
send -- "conf t\n"
expect "(config)#"
send -- "router bgp $asn\n"
expect "(config-router)#"
send -- "neighbor $hop route-map in_prepend in\n"
expect "(config-router)#"
send -- "neighbor $hop filter-list 120 in\n"
expect "#"
send -- "ip as-path access-list 120 deny $path\n"
expect "#"
send -- "end\n"
expect "#"
send -- "end\n"
expect "#"
send -- "clear ip bgp $hop\n"
expect "#"
send -- "exit\n"
