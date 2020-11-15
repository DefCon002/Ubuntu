#Scratch
import os
dir = "git"
for name in os.listdir(dir):
    fullname = os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} is a dir".format(fullname))
    else:
        print("{} is a file".format(fullname))