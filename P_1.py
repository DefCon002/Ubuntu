#!/usr/bin/env python3
numblist = list()
while True:
    inp = input('Enter_Code :')
    if inp == 'done' : break
    try :
        value = float(inp)
        numblist.append(value)
        code = sum(numblist)
        if sum(numblist) == 41203995:
            lst = list()
            lst.append('Age :')
            lst.append(24)
            lst.append(20)
            print(lst)
            ddd = dict()
            ddd['My Age'] = '19/08/1996'
            ddd['Rukaiya Age'] = '22/12/1999'
            #ddd['Rukki'] = 'meow'
            print(ddd)
            Age = dict()
            Age['Add'] = lst[1] + lst[2]
            #print(Age)
            break
        if value != 19081996:
            print('Err_Imposter')
            break
            if value != 22121999:
                print('Error_Imposter')
                break
    except :
        print('Err')
    continue
quit()
