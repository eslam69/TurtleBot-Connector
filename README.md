# TurtleBot Connector
The TurtleBot Connector is a Python script that retrieves the IP address of a device on the same network given its MAC address. It uses the nmap tool to scan the IP range and identify the device, then updates the ~/.bashrc file with the new IP address to configure the SSH connection with TurtleBots.

## Requirements
To run the script, you need to have the following dependencies installed:

* Python 3.x
* nmap

You can install the nmap tool using your system's package manager, or by running:
```console
sudo apt-get install nmap
```
## Installation
To use the Remote-IP-Getter system, you can either clone the repository or download the script file manually. If you choose to clone the repository, you can run:
```console
git clone https://github.com/eslam69/TurtleBot-Connector.git
```
## Usage
To use the TurtleBot Connector system, you need to provide the MAC address of the device you want to connect to. You can do this by passing the MAC address as an argument to the script, like this:
```python
python remote-ip-getter.py 9C:93:4E:73:E7:AD
```
If the script finds the device on the network, it will update the **~/.bashrc** file with the new IP address and print IP UPDATED! to the console. If it cannot find the device, it will print Could not find That MAC address.

