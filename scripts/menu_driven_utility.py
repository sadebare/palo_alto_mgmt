import subprocess
import os
import datetime

def execute_playbook(playbook_path):
    try:
        result = subprocess.run(['ansible-playbook', playbook_path], capture_output=True, text=True)
        log_execution(playbook_path, result)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        log_execution(playbook_path, e)
        print(e.stderr)

def log_execution(playbook_path, result):
    log_file_path = os.path.join(os.getcwd(), 'logs', 'execution_log.txt')
    with open(log_file_path, 'a') as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"\n\nTimestamp: {timestamp}\nPlaybook: {playbook_path}\n")
        log_file.write(f"Exit Code: {result.returncode}\n\n")
        log_file.write(result.stdout)

def main():
    while True:
        print("\nMenu:")
        print("1. Get system info and config")
        print("2. Backup system config")
        print("3. Update system config with new XML file")
        print("4. Apply PAN-OS Update")
        print("5. Apply AV definition update")
        print("6. Exit / Cancel")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            execute_playbook('playbooks/get_system_info.yml')
        elif choice == '2':
            execute_playbook('playbooks/backup_system_config.yml')
        elif choice == '3':
            execute_playbook('playbooks/update_system_config.yml')
        elif choice == '4':
            execute_playbook('playbooks/apply_pan_os_update.yml')
        elif choice == '5':
            execute_playbook('playbooks/apply_av_definition_update.yml')
        elif choice == '6':
            print("Exiting the menu-driven utility.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
