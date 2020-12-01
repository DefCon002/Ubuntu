# sourcery skip
# Scratch
#!/usr/bin/env python3
import os
req_path = input("Enter Directory [Path should end with \]: ")

if os.path.isfile(req_path):
    print(f"\nThe Entered Path {req_path} is a File")
else:
    all_f_dir = os.listdir(req_path)
    if len(all_f_dir) == 0:
        print(f"Nothing to show in {req_path}")
    else:
        while True:
            req_ex = input('\nEnter the Extension [.py/.TXT/.csv] [E to End] : ')
            req_file = []
            if req_ex == 'E':
                print("\nClosing...")
                break
            else:
                for file_ex in all_f_dir:
                    if file_ex.endswith(req_ex):
                        req_file.append(file_ex)
                if len(req_file) == 0:
                    print(f"\nThere are no {req_ex} files")
                else:
                    print(f"\nRequired Files\n{req_file}")
                    handle=input("[To open file enter Y]\n")
                    if handle.upper() == "Y":
                        handle_name = input("\nEnter file name: ")
                        exe_handle = open(req_path+handle_name+req_ex,'r')
                        read = exe_handle.read()
                        print(read)
                    else:
                        continue