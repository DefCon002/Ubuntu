#Scratch
import os
D = os.path.exists("Dir_Ubuntu.TXT")
if D is True:
    os.path.getsize("Dir_Ubuntu.TXT")
    os.path.getmtime("Dir_Ubuntu.TXT")
    os.path.abspath("Dir_Ubuntu.TXT")
    print(os.path.abspath("Dir_Ubuntu.TXT"))
    print("Size:",os.path.getsize("Dir_Ubuntu.TXT"), "    Unix_Time:",os.path.getmtime("Dir_Ubuntu.TXT"))
