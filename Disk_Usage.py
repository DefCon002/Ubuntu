#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("Error")
else:
    print("Everything is Ok")

U = shutil.disk_usage("/")
F = U.free/U.total*100
print('Free Disk :',F)

cp = psutil.cpu_percent(1)
print("CPU Usage", cp)