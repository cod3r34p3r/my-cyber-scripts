import socket
import argparse #Hii ni tool of handling flag like t for target and p for port
print("--Command-line scanner v1.0--")
parser=argparse.ArgumentParser(
    description="Professional flag-driven vulnerability scanner"
) #This is the engine for argument parsing
#then we define our custom flags
parser.add_argument("-t","--target", help="The domain name or ip address to evaluate", required=True)
parser.add_argument("-p","--port", type=int, help="The target door number to scan", default=80)
args=parser.parse_args() #we parse the inputs typed into the terminal
target_host=args.target
target_port=args.port
print(f"[*]Target locked:{target_host}")
print(f"[*]Probing port:{target_port}")
#then we execute network hook
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(2.0)
try:
    result=client.connect_ex((target_host,target_port))
    if result==0:
        print(f"[Alert] Port{target_port} is open on {target_host}")
    else:
        print(f"[-]Secure:port{target_port} is closed or filtering traffic.")
    client.close()
except Exception as error:
    print(f"[!]Evaluation blocked.{error}")
print("--Scan Sequence Terminated--")