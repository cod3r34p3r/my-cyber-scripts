import socket
target_host="google.com"
target_port=22
print(f"--cyber guard scanner v2.0--")
print(f"checking{target_host} on port {target_port}...\n")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(2.0)

try:
    result=client.connect_ex((target_host, target_port))
    if result==0:
        print(f"[+] SUCCESS: Port{target_port} is OPEN.")
        
        if target_port==21:
            print("WARNING: FTP port detected! Files could be stolen!")
        elif target_port==21:
            print("CRITICAL WARNING: Remote access portal open! Wath out for password bruteforcng")
        elif target_port==80 or target_port==443:
            print("SAFE: Standard website traffic port. This is normal.")
        else:
            print("Notice: Port is open, but its an uncommon service. Investigate further")   
    else:
        print(f"[-] CLOSED: Port {target_port} is locked tightly.")
        
    client.close()
    
except Exception as error:
    print(f"Error scanning:{error}")
    