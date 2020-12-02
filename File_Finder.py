# sourcery skip
# Scratch
#!/usr/bin/env python3
import os
while True:
    req_path = input("\nEnter Directory [Path should end with \ ]: ")
    os.chdir(req_path)
    lst_of_Files = os.listdir(req_path)
    lst_len = len(os.listdir(req_path))
    print(lst_of_Files)
    print(f"No. of Files in {req_path} : {lst_len}")

    if os.path.isfile(req_path):
        print(f"\nThe Entered Path {req_path} is a File")
    else:
        all_f_dir = os.listdir(req_path)
        if len(all_f_dir) == 0:
            print(f"Nothing to show in {req_path}")
        else:
            while True:
                req_ex = input("\nEnter the Extension [.py/.TXT/.csv] [B to Go back | Q to Quit] [Press ENTER for All Files] : ")
                req_file = []
                if req_ex == 'B':
                    break
                elif req_ex == 'Q':
                    print("\nClosing...")
                    quit()
                else:
                    for file_ex in all_f_dir:
                        if file_ex.endswith(req_ex):
                            req_file.append(file_ex)
                    if len(req_file) == 0:
                        print(f"\nThere are no {req_ex} files")
                    else:
                        len_F = len(req_file)
                        print(f"\nRequired Files\n{req_file}")
                        print("No.of Files: ", len_F,"\n")
                        for each_file in req_file:
                            print(each_file)

                        handle=input("[To Open File 'Y'| Main Menu 'M'| ENTER to Go Back | To Exit 'Q']\n")
                        if handle.upper() == "Y":
                            handle_name = input("\nEnter file name: ")
                            if req_ex == ".py":
                                while True:
                                    comnd = input("[To Open/Run File Enter O/R] [To go back enter B]\n")
                                    if comnd.upper() == "O":
                                        print(open(handle_name+req_ex).read())
                                    elif comnd.upper() == "R":
                                        exec(open(handle_name+req_ex).read())
                                    elif comnd.upper() == "B":
                                        break
                                    else:
                                        print("Invalid Input!")
                                        break
                            else:
                                handler = open(req_path+handle_name+req_ex,'r')
                                read = handler.read()
                                file_size = os.path.getsize(handle_name+req_ex)
                                print("File_Size:",file_size,"Bytes")
                                print(read)

                        elif handle.upper() == "Q":
                            print("\nClosing...")
                            quit()

                        elif handle.upper() == "M":
                            break
                        else:
                            continue
                    continue