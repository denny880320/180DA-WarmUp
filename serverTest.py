# Reminder: This is a comment. The first line imports a default library "socket" into Python.
# You don’t install this. The second line is initialization to add TCP/IP protocol to the endpoint.
#import socket

#s = socket.socket()
#host = '192.168.0.103' #ip of raspberry pi
#port = 12345
#s.bind((host, port))

#s.listen(5)
#while True:
 # c, addr = s.accept()
 # print ('Got connection from',addr)
 # c.send('Thank you for connecting')
 # c.close()
# Reminder: This is a comment. The first line imports a default library "socket" into Python.
# You don’t install this. The second line is initialization to add TCP/IP protocol to the endpoint.
import socket

s = socket.socket()
host = '192.168.0.103' #ip of raspberry pi
port = 12345
s.bind((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  c.sendall(b'Thanks')
  c.close()
