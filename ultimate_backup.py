from netmiko import ConnectHandler
from datetime import datetime
import getpass
import os
import logging

# ===== SETUP =====
# 1. Create a 'backups' and 'logs' folder (if they don't exist)
os.makedirs("backups", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# 2. Configure error logging
logging.basicConfig(
    filename="logs/backup_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(message)s"
)

# ===== DEVICES =====
# Replace with your devices (or use environment variables)
devices = [
    {
        "device_type": "cisco_ios",
        "host": "devnetsandboxiosxe.cisco.com",
        "username": "admin",
        "password": os.getenv("NET_PASSWORD") or getpass.getpass("Enter password for devnetsandboxiosxe.cisco.com: "),
        "port": 22,
    },
    # Add more devices here...
]

# ===== BACKUP FUNCTION =====
def backup_config(device):
    try:
        print(f"\n🔌 Connecting to {device['host']}...")
        connection = ConnectHandler(**device)
        
        # Get config and save with timestamp
        config = connection.send_command("show run")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"backups/config_backup_{device['host']}_{timestamp}.txt"
        
        with open(filename, "w") as f:
            f.write(config)
        print(f"✅ Backup saved to '{filename}'!")
        
        connection.disconnect()
    
    except Exception as e:
        error_msg = f"❌ Failed on {device['host']}: {str(e)}"
        print(error_msg)
        logging.error(error_msg)

# ===== RUN BACKUPS =====
if __name__ == "__main__":
    print("🚀 Starting config backups...")
    for device in devices:
        backup_config(device)
    print("\nAll tasks completed! Check the 'backups' folder and 'logs/backup_errors.log'.")