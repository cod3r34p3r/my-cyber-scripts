import socket
target_host="google.com"
#first we create a list of multiple parts we want to investigate all at once
#port 21 which is the file transfer protocal, port 22 which is the secure shell, port 80 which is web and port 443 for https or the secure web
ports_to_scan=[21,22,80,443] 
print(f"--cyber loop scanner v3.0--")
print(f"Target:{target_host}")
print(f"Starting automated scan on ports: {ports_to_scan}")
#This is now the loop, and its says, for every single item inside our ports list...
for port in ports_to_scan:
    #create a fresh network tool for this exactly specific knock
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1.5)
    
    try:
        #knock on the currency port from the loop
        result=client.connect_exx((target_host, port))
        if result==0:
            print(f"[+]port{port}:OPEN!")
        else:
            print(f"[-]port{port}:CLOSED!")
        client.close()    
    except Exception as error:
        print(f"[!] Error scanning port{port}:{error}")
print("\n--Scan Complete! All ports checked.--")