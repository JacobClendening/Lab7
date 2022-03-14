import datetime
import pathlib
import os
import netmiko
from netmiko import ConnectHandler
from getpass import getpass
from pathlib import Path
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException

username = input("Username: ")
password=getpass("Enter your password: ")

currentPath = Path.cwd()

fileName = "csrBackup.txt"
write = "w"
openFile = open(fileName, write)
routerIP = "192.168.108.11"


router = {
    'device_type': 'cisco_ios',
    'ip': routerIP,
    'username': username,
    'password': password
}

try:
    c = ConnectHandler(**router)
    output = c.send_command('show run')
    openFile.write(output)
    openFile.close()
except (AuthenticationException):
    print("An authentication error occured while connecting to: " + routerIP)
except (SSHException):
    print("An error occured while connecting to device " + routerIP + " via ssh. Is it enabled?")
except (NetMikoTimeoutException):
    print("The device " + routerIP + "timed out when attempting to connect. Is the device online?")
