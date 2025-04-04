from netmiko import ConnectHandler
from datetime import datetime
import getpass
import os

# Device details (replace with your sandbox credentials)
device = {
    "device_type": "cisco_ios",
    "host": "devnetsandboxiosxe.cisco.com",  # Sandbox hostname
    "username": "admin",                     # Sandbox username
    "password": "C1sco12345",                # Sandbox password (or use getpass)
    "port": 22,                              # SSH port
}

# Create a backups directory if it doesn't exist
backup_dir = "backups"
os.makedirs(backup_dir, exist_ok=True)

def backup_config():
    try:
        print(f"\n🔌 Connecting to {device['host']}...")
        
        # Establish SSH connection
        connection = ConnectHandler(**device)
        
        # Get running config
        config = connection.send_command("show running-config")
        
        # Generate timestamp and filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{backup_dir}/config_backup_{device['host']}_{timestamp}.txt"
        
        # Save config to file
        with open(filename, "w") as f:
            f.write(config)
        print(f"✅ Backup saved to '{filename}'!")
        
        # Close connection
        connection.disconnect()
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    backup_config()