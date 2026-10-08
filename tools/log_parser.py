log_file_name="server_logs.txt" #So here we are basically telling python the name of the log diary file we want to read
print("--Cyber Logg Inspector v1.0--")
print(f"Opening file: {log_file_name} to search for attacks..\n")
#then we open the file safely as if we are detonating a granade, r means we areading it not writing in it.
with open(log_file_name, "r") as file:
    #then we proceed to read the diary line by line "Bottom-up"
    for line in file:
        #if we get the wire on our granade or what we call harker keyword, trigger an alert
        if"FAILED_LOGIN" in line:
            #we use our  special "cutter".strip() to clean up the invisible spaces at the end of the line
            print(f"ALERT! Malicious activity spotted: {line.strip()}")
print("\n--inspection complete!--")