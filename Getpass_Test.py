# Scratch
#!/usr/bin/env python3
import getpass
import os

p = os.environ.get('M_PASS')
pswd = getpass.getpass('Enter Passwd: ')
if pswd == p:
    print('hi how are you')
    i = input("To quit enter q")
    if i == "q":
        quit()