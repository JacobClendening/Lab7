import datetime
import pathlib
import os
import netmiko
from netmiko import ConnectHandler
from getpass import getpass
from pathlib import Path

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

c = ConnectHandler(**router)

output = c.send_command('show run')

openFile.write(output)

openFile.close()
