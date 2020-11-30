# Scratch
def to_feet(cm):
    return cm*0.0328084

print("Welcome to this Feet coverter!")

cont = "Y"

while(cont.upper()=="Y"):
    cm = int(input("Enter cm : "))

    print("That's {} Feet".format(to_feet(cm)))
    print()
    cont = input("Do you want to do another conversion [Y to continue]")

print("Good bye!")