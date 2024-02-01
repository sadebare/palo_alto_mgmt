# Palo Alto Mgmt - Menu-Driven CLI Utility

This repository provides a menu-driven interface to execute Ansible playbooks, automating common system configuration tasks. The utility allows users to conveniently select and execute specific playbooks for tasks such as system information retrieval, system configuration backup, and more.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
- [Menu Options](#menu-options)
- [Logging](#logging)

## Getting Started

### Prerequisites

1. **Python 3**: Ensure you have Python 3 installed on your environment.
2. **Ansible**: Install Ansible using the following command:

   ```bash
   pip install ansible
### usage

1. **Clone the repository:** 

   ```bash
   git clone <github repo>
   cd <repo_name>
2. **Run the script:** 
   ```bash
   python3 scripts/menu_driven_utility.py
3. Follow the on-screen menu to select and execute specific Ansible playbooks.

## Menu Options

1. **Get system info and config:**\
    Executes the playbook for retrieving system information and configuration.

2. **Backup system config:**\
    Executes the playbook for backing up the system configuration.

3. **Update system config with new XML file:**\
    Executes the playbook for updating the system configuration with a new XML file.

4. **Apply PAN-OS Update:**\
    Executes the playbook for applying PAN-OS updates.

5. **Apply AV definition update**\
    Executes the playbook for applying antivirus definition updates.

6. **Exit / Cancel**\
    Exits the menu-driven utility.

##  Logging

 -   Execution details, including timestamp, playbook path, exit code, and output, are logged to **logs/execution_log.txt**.