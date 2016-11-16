#Start Method will show user at the first stage, and collect user's choice
def start():
    login = input('Type \"menu\" to view options or \"quit\" to exit\n')

    if (login== 'menu'):
        print('MENU')
        option()
    elif (login == 'quit'):
        exit()
    else:
        print('Invaild input')
        start()
    return

#Option Method will show user the options we have and them
def option():
    select= input('Select View Options\n1.Press 1 to view all tickets\n2.Press'
               ' 2 to view a ticket\n3.Type \"quit\" to exit\n')

    if (select == '1'):
        print('MENU')
    elif (select == 'quit'):
        exit()
    elif (select == '2'):
        print('2')
    else:
        print('Invaild input')
        option()
    return option()



#This is the main
header = 'Welcome to the ticket viewer'
print(header)
start()