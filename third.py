import requests
import datetime

#Start Method will show user at the first stage, and collect user's choice
def start():
    start_point = input('Type \"menu\" to view options or \"quit\" to exit\n')

    if (start_point== 'menu'):
        print('MENU')
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
    elif (select == 'quit'):
        quit_viewer()
    elif (select == '2'):
        ticket_id = input('Please enter Ticket ID:')
        viewOneTicket(ticket_id)
    else:
        print('Invaild input')
        option()
    return option()

def quit_viewer():
    print('Thank you for using the viewer. Goodbye:)')
    exit()

def viewOneTicket(id):
    response = requests.get(GET+'/api/v2/tickets/'+id+'.json', auth=(user, pwd))
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.\n')
        option()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    ticket = data['ticket']
    view(ticket)

def viewAll():
    response = requests.get(url, auth=(user, pwd))
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()

    ticket_list = data['tickets']
    total_tickets = data['count']
    print('total number of tickets = ',total_tickets)
    #if __name__ == '__main__':
    for ticket in ticket_list[:25]:
        view(ticket)
        #print(ticket['id'])
    if total_tickets > 25:
        print('hahhaha')


        #day 1: Now it will give me how many tickets in total and display them in a list
        # Now What I will do next will be scan input and react

def view(ticket):
    if __name__ == '__main__':

        update_date = ticket['updated_at']
        # out = datetime.strptime(update_date, '%Y-%m-%dT%H:%M:%S.%Z').strftime("%m/%d/%y")
        out = datetime.datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%SZ")
        print('Ticket with Subject:', ticket['subject'], 'Subject Id', ticket['id'], 'opened by',
            ticket['assignee_id'], 'on', out)

# Set the request parameters
GET = 'https://shengjie.zendesk.com'
url = 'https://shengjie.zendesk.com/api/v2/tickets.json'
user = 'shengjiew2@student.unimelb.edu.au'
pwd = 'duiBUqi520/'

# Do the HTTP get request

#response = requests.get(url, auth=(user, pwd))
#response = requests.get(GET+'/api/v2/tickets.json', auth=(user, pwd))

# Check for HTTP codes other than 200

#This is the main
header = 'Welcome to the ticket viewer'
print(header)
start()







