import sys
import urllib.request #this is our new army kniife that enable opening web browser tool inside python.
print("--Cyber Web Bug Hunter v1.0--")
if len(sys.argv)<2:
    print("Error: You forgot to specify a target website URL!")
    print("Usage: python web_hunter.py http//cod3r34p3r.com")
    sys.exit()
#so here we grab the main website link from the terminal input
target_url=sys.argv[1]
#so here we create a list of secret hodden doors we want to guess
secret_doors=["/admin","/login","/secret","/backup.zip","/robots.txt"]
print(f"Target URL:{target_url}")
print("Checking for exposed pages...\n")
for door in secret_doors:
    #here we glue the target website link and the secret door path together
    full_link=target_url + door
    try:
        #so we try to open the full web page link
        response=urllib.request.urlopen(full_link, timeout=2.0)
        #if it loads well the code status should b200
        if response.status==200:
            print(f"[exposed] found a live page:{full_link}")
    except urllib.error.HTTPError as error:
        #so if the server says 404, it means its doesnt exist(secure!)
        if error.code==404:
            print(f"[-]Secure: {door} was not found(404)")
        else:
            print(f"[Notice]checked{door} but got server code:{error.code}")
    except Exception as general_error:
        print(f"[!]could not check{door}:{general_error}")
print("\n--Web scan complete--")