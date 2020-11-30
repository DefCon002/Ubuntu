# Scratch
def to_seconds(hours, min, sec):
    return hours*3600+min*60+sec

cont = "Y"
while(cont.upper()=="Y"):
    hours = int(input("Enter Hours : "))
    min = int(input("Enter Min : "))
    sec = int(input("Enter Sec : "))

    print("That's {} Second's".format(to_seconds(hours, min, sec)))
    print()
    cont = input("Do You Want To Continue? [Y to continue]")

print("Good bye!")