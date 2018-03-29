#!/usr/bin/expect
set pw "qq1005521"
set host [lindex $argv 0]

spawn ssh root@$host

expect {
    "Connection refused" exit
    "Name or service not known" exit
    "continue connecting" {send "yes\r";exp_continue}
    "password:" {send "$pw\r";exp_continue}
    "Last login" {send "uptime\r"}
}
expect eof
exit
~