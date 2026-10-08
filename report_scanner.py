import socket
import sys
print("--cyber report scanner v6.0--")
if len(sys.argv)<2:
    print("Error: you forgot to specify a target website!")
    print("Usage: python report_scanner.py <website_name>")
    sys.exit()
target_host=sys.argv[1]
ports_to_scan=[21,22,80,443]
#heere we choose a name for our official cyber report file,
report_file_name="scan_report.txt"
print(f"Target:{target_host}")
print(f"Scanning and saving results directly to'{report_file_name}'..\n")
#so we pen the file with the w flag meaning it should create a blank file, "W" MEANS WRITE
with open(report_file_name, "w") as report:
    #lets make it abit formal with a nice header
    report.write(f"--CYBER SECURITY SCAN REPORT--\n")
    report.write(f"Target Host Evaluated:{target_host}\n")
    report.write(f"-----------------------------------\n\n")
    for port in ports_to_scan:
        client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1.5)
        try:
            result=client.connect_ex((target_host, port))
            if result==0:
                #so hapa instead of printing to the screen, we write directly to the file file that we had ealier created
                report.write(f"[+]Port{port}:OPEN(High Risk Alert)\n")
                print(f"[+]Found Open Port:{port}")#small hint on the screen
            else:
                report.write(f"[-]Port{port}: CLOSED(secure)\n")
            client.close()
        except Exception as error:
            report.write(f"[!] Error checking port{port}: {error}:\n")
    report.write(f"\n--End Report--")
print(f"\nDone! Open '{report_file_name}' it will open in the IDE that you are using, for me its VS Code")