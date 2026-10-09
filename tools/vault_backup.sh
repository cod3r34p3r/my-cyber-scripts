echo "--Automated Cyber Toolkit archiever v1.0--"
echo "initializing security backup process.."
#first we define the destination archive house name
backup_dir="labs/backups"
#we check if the backup house does not exist yet
if [ ! -d "$backup_dir" ]; then
    echo  "[*] creating secure destination vault: backup_dir"
    mkdir -p "$backup_dir"
else
    echo "[+] secure destination vault verified"
fi
#then we copy all python scripts  from tools into secure backup room
echo "[*]Copying security automation tools.."
cp tools/*.py "$backup_dir/" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "[ALERT]Backup operation succesful"
    echo "All python assets successfully secured in $backup_dir"
else
    echo "[ERROR] Backup operation failed. No scripts discovered to copy"
fi

echo "- Archive Process Terminated -"
