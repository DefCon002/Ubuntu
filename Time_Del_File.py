# Scratch
#!/usr/bin/env python3
import os
import datetime
req_path = input("Enter path : ")

if os.path.exists(req_path):
    lst_files = os.listdir(req_path)
    for files in lst_files:
        if os.path.isfile(files):
            print(files)

        elif os.path.isdir(files):
            print("\n",files,"is a directory\n")
else:
    print("Invalid path!")
while True:

    Ex = input('\nFile name for time : ')
    if Ex == "Q":
        break
    elif os.path.isfile(Ex):
        print(os.path.getatime(Ex))
        print(os.path.getmtime(Ex))
        print(os.path.getctime(Ex))
        print("\nFile Size: ",os.path.getsize(Ex),"Bytes")
        print(datetime.datetime.fromtimestamp(os.path.getctime(Ex)))
        print("\nQ to quit")
    else:
        print("Invalid Input!")