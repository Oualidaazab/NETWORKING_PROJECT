import socket  
host ='127.0.1.1'
PORT =9090 #  port  number 
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
socket.connect((host,PORT)) 
socket.send("hello my niga  ".encode('utf-8')) 
print(socket.recv(1024))