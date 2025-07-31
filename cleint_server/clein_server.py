import  socket  

host =socket.gethostbyname(socket.gethostname()) #  Finde the  local addresse  automaticly  and you can give the ip  addresse manualy 
PORT =9090 #  port  number 
sever =socket.socket(socket.AF_INET,socket.SOCK_STREAM) #  AF_INET for ipv4 packet   and  SOCK_STREAM for TCP protocole  and for UDP use SOCK_DATAGRAM, this socket is for accept not for communication  
sever.bind((host,PORT)) 
#  listen for incomming connection  
sever.listen(5)     # 5 mean  how many  unaccepted connection do we allow before  reject new ones  if more than 5 we reject 

while True : 
    communication_socket ,address = sever.accept()  #  this accept socket  and waiting for  address  
    print(f"Connect to {address}") 
    message =  communication_socket.recv(1024).decode("utf-8") # 1024 how many  byt  
    print(f"massage from cleint is {message} and adrres  is {address} ") 
    communication_socket.send(f"i got your message thanks!  ".encode('utf-8')) 
    communication_socket.close 
    