element=int(input('Атомный номер хим.элемента: '))
if element:
    z=int(element)
    if z==3:
        print('Литий(Li)')
    elif z==17:
        print('Хлор(Cl)')
    elif z==25:
        print('Марганец(Mn)')
    elif z==80:
        print('Ртуть(Hg)')
    else:
        print('Что-то другое')
