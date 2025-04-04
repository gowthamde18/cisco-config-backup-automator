# Cisco Config Backup Automator 🚀

Automatically backup Cisco device configurations using Python and Netmiko. Supports standalone and multi-device backups with error logging.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Netmiko](https://img.shields.io/badge/Netmiko-4.1.2-green)
![License](https://img.shields.io/badge/License-MIT-orange)

## 📦 Scripts

### 1. `backup_configuration.py`
- **Basic single-device backup**
- Features:
  - Saves running config to timestamped file
  - Minimal error handling

### 2. `ultimate_backup.py`
- **Advanced multi-device backup**
- Features:
  - Supports multiple devices
  - Error logging to `logs/backup_errors.log`
  - Secure password handling (environment variables/getpass)
  - Organized backup folder structure

## 🛠 Setup

### Prerequisites
- Python 3.8+
- Required packages:
  ```bash
  pip install netmiko getpass4
