echo "--Linux System configuration Account Auditor v1.0--"
echo "Target Resource Evaluation: Labs/mock_passwd.txt--"
target_file="labs/mock_passwd.txt"

if [ ! -f "$target_file" ]; then
    echo "Error: Traget simulation lab configuration file not found!"
    exit 1
fi

echo "[*] scanning database records for authorized superuser account.."
echo ""

#we read theh file line by line
while IFS= read -r line || [ -n "$line" ]; do
#linux account logs separate values usng colons(:)
#we cut out the first field (username) and third field (user id number)
    username=$(echo "$line" | cut -d: -f1)
    uid=$(echo "$line" | cut -d: -f3)
#in linux, user id 0 means absoute root administartor power
    if [ "$uid" = "0" ]; then
        echo "[Privilege alert]Account possessing root permissions:'$username'(uid:$uid)"

    #if the account is named anything other than the official system 'root', flag the anomaly
        if [ "$username" != "root" ]; then
            echo "Critical anomaly:Unauthorized rogue root user detected!"
        fi
    fi
done < "$target_file"

echo ""
echo "--system audit assesment concluded--"
