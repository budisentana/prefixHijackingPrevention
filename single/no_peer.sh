#!/usr/bin/expect -f
set router_ip [lindex $argv 0]
set bgp_port "2605"
set password "test"
set asn [lindex $argv 1]
set peer_ip [lindex $argv 2]
set peer_asn [lindex $argv 3]

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
send -- "no neighbor $peer_ip remote-as $peer_asn\n"
expect "#"
send -- "end\n"
expect "#"
send -- "end\n"
expect "#"
send -- "wr me\n"
expect "#"
send -- "exit\n"

