# Scratch
def to_Farenheit(celsius):
    return (celsius*(9/5))+32

cont ="Y"
while(cont.upper()=="Y"):
    celsius = int(input("Enter Celsius : "))

    print("That's {} Farenheit".format(to_Farenheit(celsius)))
    print()
    cont = input("Do You Want Do Another Conversion? [Y to continue]")

print("Good bye!")