import  socket 

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        
        s.connect(('8.8.8.8', 80))  # Google DNS
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

local_ip = get_local_ip()
host =local_ip 
port =9090
server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
server.connect((host,port)) 
server.send(f"hello this messafe is from {local_ip}".encode('utf-8'))  
server.recv().decode('utf-8') 


 
