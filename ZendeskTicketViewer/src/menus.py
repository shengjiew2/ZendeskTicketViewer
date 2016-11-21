from viewAllTickets import viewAll
from chooseTicket import chooseOneTicket
#Start Method will show user at the first stage, and collect user's choice
def start():
    start_point = input('\tType \"menu\" to view options or \"quit\" to exit\n')

    if (start_point== 'menu'):
        print('\t\tOption Menu')
        option()
    elif (start_point == 'quit'):
        quit_viewer()
    else:
        print('Invaild input')
        start()
    return

#Option Method will show user the options we have and them
def option():
    select= input('\tSelect View Options\n\t1.Press 1 to view all tickets\n\t2.Press'
               ' 2 to view a ticket\n\t3.Type \"quit\" to exit\n')

    if (select == '1'):
        viewAll()
    elif (select == '2'):
        ticket_id = input('Please enter Ticket ID:')
        chooseOneTicket(ticket_id)
    elif (select == 'quit'):
        quit_viewer()
    else:
        print('Invaild input')
        option()
    return option()

#exit method, quit with nice goodbye words
def quit_viewer():
    print('Thank You For Using Zendesk Viewer. Looking Forward to See You Again:)'.center(120,' '))
    exit()

