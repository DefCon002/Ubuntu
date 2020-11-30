# Scratch
def to_MPH(KPH):
    return KPH*0.621371

def to_KPH(MPH):
    return MPH*1.60934


while True:
    cont = "Y"
    convert = input("\nWhat to Convert [KPH to MPH: M or MPH to KPH: K]  [Enter 'E' to Exit]\n")
    if convert == "E":
        break
    try:
        if (convert.upper() == "M"):
            while(cont.upper()=="Y"):
                KPH = int(input("\nEnter KPH : "))
                print("Thats's {} MPH".format(to_MPH(KPH)))
                print()
                cont = input("Do you want to do another conversion?\n[Y to Continue N to Main menu]\n")
                if cont == "N":
                    break
        elif (convert.upper() == "K"):
            while(cont.upper()=="Y"):
                MPH = int(input("\nEnter MPH : "))
                print("That's {} KPH".format(to_KPH(MPH)))
                print()
                cont = input("Do you want to do another conversion?\n[Y to continue N to Main menu]\n")
                if cont =="N":
                    break
        else:
            print("Err_input")
            continue
    except:
        print("Invalid input. Please try again.")
        continue
print("Good bye!")