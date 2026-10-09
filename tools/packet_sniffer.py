import sys
print("--Network Packet sniffer v1.0--")
print("[*] Initializng packet interceptors")

try:
    #we start by attempting to open our nw heavy duty packet library
    from scapy.all import sniff
except ImportError:
    print("Error:Scapy lbrary not found, run pip install scapy first")
    sys.exit()
#then define our custom analysis function
#every single packet that flies ny will get caught and tossed into this function
def process_captured_packet(packet):
    #then we check whether the packet has a summary description to show us
    if packet.summary():
        print(f"[STREAM] Intercepted Packet:{packet.summary()}")
print("[+] sniffer engine running live, press ctrl+c to terminate scan\n")
try:
    #we start the sniffing loop
    #count=5 meaning it will stop compltely after grabbing exactly 5 packets
    sniff(prn=process_captured_packet, count=5, timeout=10.0)
except Exception as network_error:
    print(f"[!]Sniffing interrupted: {network_error}")
    print("Reading raw packets usually requires Administrators permissions on windows")
print("\n--sniffer sequence terminated--")