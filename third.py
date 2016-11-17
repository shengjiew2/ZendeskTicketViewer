import requests
import datetime
import math
MAX_WEB_TICKETS = 100
PAGE_SIZE = 25
WEB_TO_PAGE = 4

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
        print()
    else:
        print('Invaild input')
        option()
    return option()

#exit method, quit with nice goodbye words
def quit_viewer():
    print('Thank you for using the viewer. Goodbye:)')
    exit()

#view one specific ticket by its ticket ID
def viewOneTicket(id):
    response = requests.get(GET+'/api/v2/tickets/'+id+'.json', auth=(user, pwd))
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        print('Please check your input ticket ID and try again later:)\n\n')
        option()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    ticket = data['ticket']
    view(ticket)

#view all tickets
def viewAll():
    response = requests.get(url, auth=(user, pwd))
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()

    total_tickets = data['count']
    print('total number of tickets = ',total_tickets)
    total_page = math.ceil(total_tickets/PAGE_SIZE)
    print('Each page will display 25 tickets, total ',total_page,'pages')


    page_opt = input('Please enter which page you want to view or type \'option\' back to option menu\n')
    if page_opt.isdigit():
        page_number = int(page_opt)
        if  page_number in range (1,total_page+1):
            web_page = math.floor(page_number/WEB_TO_PAGE) + math.ceil((page_number%WEB_TO_PAGE)/WEB_TO_PAGE)
            response = requests.get(url+'?page='+str(web_page),auth=(user, pwd))
            data = response.json()
            disp(page_number%WEB_TO_PAGE,data)
            print()
        else:
            print('Please enter a valid page number\n')
            viewAll()
    elif page_opt == 'option':
        option()
    else:
        print('Invalid input. Please check your input and try it later\n')
        option()


        #day 1: Now it will give me how many tickets in total and display them in a list
        # Now What I will do next will be scan input and react

#Disp method is a helping method for viewAll Method,
#it will disp a certain page of tickets
def disp(page_number,data):
    ticket_list = data['tickets']
    if page_number != 0:
        cur = (page_number-1)*PAGE_SIZE
    else:
        cur = (WEB_TO_PAGE-1) * PAGE_SIZE
    for ticket in ticket_list[cur:cur+PAGE_SIZE]:
        view(ticket)

#View method will take one ticket as input and disp its deets
def view(ticket):
    if __name__ == '__main__':

        update_date = ticket['updated_at']
        # out = datetime.strptime(update_date, '%Y-%m-%dT%H:%M:%S.%Z').strftime("%m/%d/%y")
        out = datetime.datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%SZ")
        print('Ticket with Subject:', ticket['subject'], 'Subject Id', ticket['id'], 'opened by',
            ticket['assignee_id'], 'on', out)





# This is the main
# Set the request parameters
GET = 'https://shengjie.zendesk.com'
url = 'https://shengjie.zendesk.com/api/v2/tickets.json'
user = 'shengjiew2@student.unimelb.edu.au'
pwd = 'duiBUqi520/'

header = 'Welcome to the ticket viewer'
print(header)
start()







