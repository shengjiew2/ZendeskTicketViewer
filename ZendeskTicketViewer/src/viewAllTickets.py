import requests
import math
from viewValidTicket import viewValidTicket
import userData

#Disp method is a helping method for viewAll Method,
#it will disp a certain page of tickets
def disp(page_number,data):
    ticket_list = data['tickets']
    if page_number != 0:
        cur = (page_number-1)*userData.PAGE_SIZE
    else:
        cur = (userData.WEB_TO_PAGE-1) * userData.PAGE_SIZE
    for ticket in ticket_list[cur:cur+userData.PAGE_SIZE]:
        viewValidTicket(ticket)

#viewall method use to view all tickets
def viewAll():
    response = requests.get(userData.url, auth=(userData.user, userData.pwd))
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    total_tickets = data['count']
    print('total number of tickets = ',total_tickets)
    total_page = math.ceil(total_tickets/userData.PAGE_SIZE)
    print('Each page will display 25 tickets, total ',total_page,'pages')

    page_opt = input('Please enter which page you want to view or type \'option\' back to option menu\n')
    if page_opt.isdigit():
        page_number = int(page_opt)
        #page checking and go to required page

        #Since we already in page 1, no need to reload
        if page_number == 1:
            print("Zendesk Ticket Viewer: Multiple Ticket Viewer".center(120, '='))
            disp(page_number % userData.WEB_TO_PAGE, data)
            print(''.center(120, '='))

        elif  page_number in range (2,total_page+1):
            print("Zendesk Ticket Viewer: Multiple Ticket Viewer".center(120, '='))
            web_page = math.floor(page_number/userData.WEB_TO_PAGE) +\
                       math.ceil((page_number%userData.WEB_TO_PAGE)/userData.WEB_TO_PAGE)
            response = requests.get(userData.url+'?page='+str(web_page),auth=(userData.user, userData.pwd))
            data = response.json()
            disp(page_number%userData.WEB_TO_PAGE,data)
            print(''.center(120, '='))
            print()
        else:
            print('Please enter a valid page number\n')
            viewAll()
    elif page_opt == 'option':
        return

    #invaild input handling
    else:
        print('Invaild input. Please check your input and try it later\n')
        return