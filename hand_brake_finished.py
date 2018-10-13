#!/usr/bin/python
import subprocess
import csv
import time
from paramiko import SSHClient, AutoAddPolicy

def check_handbrake():
    open1 = False
    tasklist = subprocess.Popen('tasklist.exe /fo csv',
                                  stdout=subprocess.PIPE,
                                  universal_newlines=True)

    for p in csv.DictReader(tasklist.stdout):
        if p["Image Name"] == "HandBrake.exe":
            open1 = True
            break
    if open1: return True
    else: return False

running = check_handbrake()
if not running:
    print("Starting HandBrake...")
    subprocess.call(["C:\\Program Files\\HandBrake\\HandBrake.exe"])

time.sleep(10)
running = check_handbrake()
print("HandBrake is running")
while running:
    print("Checking...", end=' ')
    running = check_handbrake()
    print("HandBrake is running.")
    time.sleep(120)

print("HandBrake is not running.")
print("Shutting Down RPI OSMC...")

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy)
client.connect("OSMC-MJREDD", username="osmc",password="TomHanks14")
stdin, stdout, stderr = client.exec_command('sudo /sbin/shutdown -h now &')
#print "stderr: ", stderr.readlines()
#print "pwd: ", stdout.readlines()
client.close()

print("Shutting down computer...")
subprocess.call(["shutdown", "/s"])
