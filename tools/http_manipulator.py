import sys
import urllib.request
print("--Elite Http Protocol Manipulator v1.0--")
if len(sys.argv)<2:
    print("Error: Target url endpoint not specified.")
    print("Usage: Python tools/http_manipulator.py http://cod3r34p3r.com")
    sys.exit()
target_url=sys.argv[1]
print(f"[*]Tageting application path:{target_url}")
try:
    #so here we forge a custom identity profile header mapping
    #then we cahnge the identity to look like legacy custom terminal instead of chrome
    custom_identity="CyberReaperScanner/SecureAuditEngine1.0"
    header_stack={'User_Agent':custom_identity}
    print(f"[*]Injecting custom User-Agent signature: '{custom_identity}'")
    #teh we package the request container parameters
    request_packet=urllib.request.Request(target_url, headers=header_stack)
    #fire the request payload down the line
    print("[+]Transmission dispatched. Intercepting remote server response headers..")
    with urllib.request.urlopen(request_packet, timeout=4.0) as server_response:
        print("\n--Remote Server Header Meatdat pack--")
        for key, value in server_response.getheaders():
            print(f"{key}:{value}")
except Exception as connection_error:
    print(f"\n[!]connection sequence faulted:{connection_error}")
    print("Note: Verify the endpoint target has an active, reachable web server online")
print("\n--Manipulation Sequence Complete--")
    