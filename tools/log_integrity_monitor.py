import os
import sys
import hashlib
import json

DB_FILE = "labs/log_integrity_db.json"

def calculate_sha256(file_path):
    """Computes the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def get_target_files(input_path):
    """Resolves single file or directory pathways."""
    target_files = []
    if os.path.isfile(input_path):
        target_files.append(os.path.abspath(input_path))
    elif os.path.isdir(input_path):
        for root, _, files in os.walk(input_path):
            for file in files:
                target_files.append(os.path.abspath(os.path.join(root, file)))
    else:
        print(f"Error: Specified path does not exist: {input_path}")
        sys.exit(1)
    return target_files

def load_baseline():
    """Loads baseline from data vault."""
    if not os.path.exists(DB_FILE):
        return {}
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def save_baseline(baseline_data):
    """Saves updated parameters."""
    try:
        os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
        with open(DB_FILE, "w") as f:
            json.dump(baseline_data, f, indent=4)
        return True
    except Exception:
        return False

def initialize_baseline(target_path):
    """Initializes and stores hashes of all targeted logs."""
    files = get_target_files(target_path)
    baseline = load_baseline()
    
    for file_path in files:
        file_hash = calculate_sha256(file_path)
        if file_hash:
            baseline[file_path] = file_hash
            
    if save_baseline(baseline):
        print("Hashes stored successfully.")
    else:
        print("Error: Could not save baseline.")

def verify_integrity(target_path):
    """Compares current state signatures to baseline."""
    stored_baseline = load_baseline()
    files = get_target_files(target_path)
    
    for file_path in files:
        file_hash = calculate_sha256(file_path)
        if not file_hash:
            continue
            
        if file_path not in stored_baseline:
            print(f"Status: Untracked File ({os.path.basename(file_path)})")
        elif stored_baseline[file_path] != file_hash:
            print(f"Status: Modified (Hash mismatch) -> {os.path.basename(file_path)}")
        else:
            print(f"Status: Unmodified -> {os.path.basename(file_path)}")

def update_file_hash(target_path):
    """Updates a single changed file hash signature manually."""
    if not os.path.isfile(target_path):
        print("Error: Update command requires a single file path target.")
        sys.exit(1)
        
    stored_baseline = load_baseline()
    abs_path = os.path.abspath(target_path)
    new_hash = calculate_sha256(abs_path)
    
    if new_hash:
        stored_baseline[abs_path] = new_hash
        if save_baseline(stored_baseline):
            print("Hash updated successfully.")
        else:
            print("Error: Could not save update.")

def main():
    if len(sys.argv) < 3:
        print("Usage: python tools/log_integrity_monitor.py [init|check|update] [path]")
        sys.exit(1)
        
    action = sys.argv[1]
    target_path = sys.argv[2]
    
    if action == "init":
        initialize_baseline(target_path)
    elif action == "check":
        verify_integrity(target_path)
    elif action == "update":
        update_file_hash(target_path)
    else:
        print(f"Unknown action command: {action}")

if __name__ == "__main__":
    main()
