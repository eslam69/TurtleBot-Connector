import re
import subprocess
import os
import sys



def get_ip(mac_address: str, ip_range: str = "10.10.100.*",verbose=True) -> None:
    
    output = os.popen(f"sudo nmap -sn {ip_range}").read()
    ip_address = None

    lines = output.split("\n")

    for i in range(len(lines)):
        if "MAC Address" in lines[i] and mac_address in lines[i]:
            for j in range(i-2, -1, -1):
                if "Nmap scan report" in lines[j]:
                    ip_address = lines[j].split()[-1]
                    break
    if verbose:
        print("IP_Address is: ",ip_address)
    return ip_address

def update_bashrc_ip(new_ip_address:str)->None: 

    # Replace this with the new IP address you want to set

    # Open the ~/.bashrc file for editing
    with open(os.path.expanduser("~/.bashrc"), "r+") as bashrc_file:
        # Read the contents of the file into a list of lines
        lines = bashrc_file.readlines()
        # Iterate through each line and replace the old IP address with the new one
        for i, line in enumerate(lines):
            if "export ROS_IP=" in line:
                lines[i] = f"export ROS_IP={new_ip_address}\n"
            elif "export ROS_MASTER_URI=" in line:
                lines[i] = f"export ROS_MASTER_URI=http://{new_ip_address}:11311\n"
            elif "export ROS_HOSTNAME=" in line:
                lines[i] = f"export ROS_HOSTNAME={new_ip_address}\n"
        # Move the file pointer to the beginning of the file and overwrite the contents
        bashrc_file.seek(0)
        bashrc_file.writelines(lines)

    # Source the ~/.bashrc file to apply the changes
    os.system("source ~/.bashrc")


if __name__ == "__main__":
    if len(sys.argv)>1:
        mac_address = str(sys.argv[1])
    else:
        mac_address = "9C:93:4E:73:E7:AD" #For Example
    
    target_ip = get_ip(mac_address)
    if get_ip is None:
        print("Could not find That MAC address")
    else:
        update_bashrc_ip(target_ip)
        print("IP UPDATED!")