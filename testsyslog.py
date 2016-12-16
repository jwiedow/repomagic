import socket as sock
import os
from datetime import datetime

socktype=sock.SOCK_DGRAM
socket=sock.socket(sock.AF_INET,socktype)
address=('localhost',514)
socket.connect(address)
socket.getsockname()

pri_local7info=23*8+6
pri_local7warn=23*8+4
version=1
time_s=datetime.utcnow().isoformat()+'Z'
host_s=sock.gethostname()
program_s='python'
pid_s=os.getpid()
msgid_s='testsyslogng'

msg1024="<%i>%i %s %s %s %s %s %s\n" % (
pri_local7info,
version,
time_s,
host_s,
program_s,
pid_s,
msgid_s,
'1024'*256
) #'1024'*256

msg2048="<%i>%i %s %s %s %s %s %s\n" % (
pri_local7info,
version,
time_s,
host_s,
program_s,
pid_s,
msgid_s,
'2048'*512
) #'2048'*512

msg4096="<%i>%i %s %s %s %s %s %s\n" % (
pri_local7info,
version,
time_s,
host_s,
program_s,
pid_s,
msgid_s,
'4096'*1024
) #'4096'*1024

msg8192="<%i>%i %s %s %s %s %s %s\n" % (
pri_local7info,
version,
time_s,
host_s,
program_s,
pid_s,
msgid_s,
'8192'*1024
) #'8192'*1024

msg10240="<%i>%i %s %s %s %s %s %s\n" % (
pri_local7info,
version,
time_s,
host_s,
program_s,
pid_s,
msgid_s,
'10240'*2048
) #'10240'*2048

socket.send(msg1024.encode('utf-8'))
socket.send(msg2048.encode('utf-8'))
socket.send(msg4096.encode('utf-8'))
socket.send(msg8192.encode('utf-8'))
socket.send(msg10240.encode('utf-8'))

socket.close()
