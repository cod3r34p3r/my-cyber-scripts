import socket  #here we are grabbing networking tool from pythons toolbox
target_host="google.com" #This is the terget host the castle we want to check
target_port=1234 #we choose the digital door to knock on, port 80 is the standard port for HTTP traffic
print(f"scanning target:{target_host} on port {target_port}...")
#we are creating a new socket object using the socket module, specifying the address family (AF_INET for IPv4) and the socket type (SOCK_STREAM for TCP)#
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.settimeout(2.0)
try:
    result=client.connect_ex((target_host, target_port))
    if result == 0:
        print(f"SUCCESS: Port {target_port} is OPEN! Anyone can conect")
    else:
        print(f"CLOSED: Port {target_port} is closed or protected")
    client.close()
except Exception as error:
    print(f"Something went wrong:{error}")
                