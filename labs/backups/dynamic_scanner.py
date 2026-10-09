import socket    
import sys # we introduce a new word sys stands for system to read terminal inputs directly
print("--cyber dynamic scanner v5.0--")
#so we check if the user forgot to type a website name
#sys.argv is a list of all words typed in the termina command.
#sys.argv[0] is the script name("dynamic_scanner.py")
#sys.argv[1] should be the website name

if len(sys.argv)<2:
    print("Error: You forgot to specify the target website")
    print("Usage: Python dynamic_scanner.py<website_name>")
    sys.exit() #stop the script here because we dont have a target
#so we grab the target name from the terminal input slot
target_host=sys.argv[1]
ports_to_scan=[80,443]
for port in ports_to_scan:
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.settimeout(1.5)
    
    try:
        result=client.connect_ex((target_host, port))
        if result==0:
            print(f"[+]port{port}:OPEN")
        else:    
            print(f"[-]port{port}:OPEN")
        client.close()
    except Exception as error:
        print(f"[!]Error on port{port}: {error}")
print("\n--Scan complete")