import sys
import argparse
print("--Network Packet Crafter v1.0--")
try:
    #grab the layering and sending tools from scapy
    from scapy.all import IP, ICMP, sr1
except ImportError:
    print("Error: Scapy library missing, run pip install scapy")
    sys.exit()
    
parser = argparse.ArgumentParser(description="Forge and launch custom ICMP packets.")
parser.add_argument("-t", "--target", help="The destination IP address to probe", required=True)
args = parser.parse_args()

target_ip = args.target
print(f"[*] Constructing custom network layers for: {target_ip}")  

ip_layer = IP(dst=target_ip)
icmp_layer = ICMP()
custom_packet = ip_layer / icmp_layer
print("[+] Packet successfully forged. Injecting into raw network stream...")
try:
    response = sr1(custom_packet, timeout=3.0, verbose=False)
    
    print(f"\n=== Network Response Evaluation ===")
    if response:
        print(f"[ALERT] Target Host {target_ip} is ALIVE!")
        print(f"[STREAM] Received Reply Metadata: {response.summary()}")
    else:
        print(f"[-] Silent: No response received from {target_ip} within the timeout window.")

except Exception as network_error:
    print(f"[!] Transmission failed: {network_error}")
    print("Operational Note: Custom packet forgery requires full administrator terminal execution on Windows.")

print("--Injection Sequence Complete--")
