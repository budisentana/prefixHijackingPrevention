#!/usr/bin/expect -f
set timeout -1
set my_prefix [lindex $argv 0]
spawn vtysh -d bgpd
expect "#"
send -- "enable\n"
expect "#"
send -- "configure terminal\n"
expect "(config)#"
send -- "router bgp 7675\n"
expect "(config-router)"
send -- "network $my_prefix\r"
expect "#"
send -- "end\n"
expect "#"
send -- "end\n"
expect "#"
send -- "exit\n"
