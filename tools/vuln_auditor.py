import sys
import urllib.request
import re #for searching inside text patterns

print("--Elite Web Vulnerability Auditor v1.0--")
if len(sys.argv)<2:
    print("Error:Missing target url")
    print("Usage: Python vuln_auditor.py http://cod3r34p3r.com")
    sys.exit()
    
target_url=sys.argv[1]
print(f"[*]commencing automated audit on {target_url}\n")
try:
    #so we download the fullwebpage source code
    headers={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req=urllib.request.Request(target_url, headers=headers)
    with urllib.request.urlopen(req, timeout=3.0) as response:
        html_content=response.read().decode('utf-8')
    print(f"[+]Webpage content successfully retrieved. Analyzing code structural flaws....")
    #so here we llok for web inputs or forms that do not protect data entry points
    #we search for '<form' tag inside the webpage source
    forms_found=re.findall(r'<form', html_content, re.IGNORECASE)
    print(f"\n--Audit Findings--")           
    if forms_found:
        print(f"[RISK] detected{len(forms_found)}interactive web forms")
        print("Vulnerablity Note: Unprotected inputs are high-risk targets for SQL Injections and xss attacks")
    else:
        print("[secure] No standard input forms exposed on the landing page code layout")
except Exception as error:
    print(f"[!] Critical Audit Failure{error}")
print("\n--Audit Execution Complete--")
    
 