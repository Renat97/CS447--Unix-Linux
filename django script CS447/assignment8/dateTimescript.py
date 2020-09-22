# dateTime Script
# cd /usr/local/assignment8/systemTimeOne.py
# systemTimeOne is for the one implemented with the time module and systemTimeTwo.py is implemented with the datetime module
# mytimer.service systemTimeOne.sh
# prints out s.connect((TCP_IP, TCP_PORT))
# output received data: b'Tue Apr  7 21:50:50 2020\r\n
# date --set="1986-10-11 10:00:00"
# Tue Apr  7 22:18:37 2020\r\n
# received data:Tue Apr  7 22:19:41 2020\r\n
# data: extra operand '7'
# recieved data:Apr 
import datetime
import socket

print(dir(datetime))

TCP_IP = 'cs447-newellz2.ncr'
TCP_PORT = 13
BUFFER_SIZE = 1024
MESSAGE = b''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
dataNew = str(data)
dataNew2 = dataNew.translate({ord(i): None for i in "b'"})
dataNew3 = dataNew2.split()
s.close()
os.system("date --set=" + dataNew2)

print ("received data:",  dataNew2)