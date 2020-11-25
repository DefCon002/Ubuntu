# sourcery skip: hoist-statement-from-if, remove-unreachable-code
#Scratch
while True:
    Name = input("Enter ID :")
    if Name == 'Ashfaque':
        Pass = input('Enter Password :')
        if Pass == '12345':
            print('Welcome Boss!!!')
            handle = open('Ash.txt')
            inp = handle.read()
            print(inp)
            continue
        else:
            print('Enter Correct Password')
            continue
        break
    elif Name == 'Rukaiya':
        Pass = input('Enter Password :')
        if Pass == 'meow':
            print('Welcome Maam!')
            handle = open('rukki.txt')
            inp = handle.read()
            print(inp)
        else:
            print('Enter Correct Password')
            continue
        break
    elif Name == 'Done!':
        break
    else:
        print('Error_Intruder Alert!!!')
        continue