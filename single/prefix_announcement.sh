#!/usr/bin/expect -f
set router_ip [lindex $argv 0]
set bgp_port "2605"
set password "test"
set asn [lindex $argv 1]
set prefix [lindex $argv 2]

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
send -- "network $prefix\n"
expect "#"
send -- "end\n"
expect "#"
send -- "end\n"
expect "#"
send -- "wr me\n"
expect "#"
send -- "exit\n"

