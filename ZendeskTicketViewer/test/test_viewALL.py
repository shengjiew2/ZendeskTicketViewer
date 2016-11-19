import datetime
import json
import math
from test_disp import disp
from pprint import pprint
MAX_WEB_TICKETS = 100
PAGE_SIZE = 25
WEB_TO_PAGE = 4
with open('page1.txt') as data_file:
    data = json.load(data_file)
pprint(data)

def viewAll(data,page_opt):

    total_tickets = data['count']
    print('total number of tickets = ',total_tickets)
    total_page = math.ceil(total_tickets/PAGE_SIZE)
    print('Each page will display 25 tickets, total ',total_page,'pages')
    print('Please enter which page you want to view or type \'option\' back to option menu\n')
    if page_opt.isdigit():
        page_number = int(page_opt)
        #Since we already in page 1, no need to reload
        if page_number == 1:
            disp(page_number % WEB_TO_PAGE, data)

        elif  page_number in range (2,total_page+1):
            web_page = math.floor(page_number/WEB_TO_PAGE) +\
                       math.ceil((page_number%WEB_TO_PAGE)/WEB_TO_PAGE)
            print('web_page:',web_page)
        else:
            print('Please enter a valid page number\n')
    elif page_opt == 'option':
        return
    else:
        print('Invalid input. Please check your input and try it later\n')
        return
def test_answer(capsys):
    viewAll(data,'1')
    out,err = capsys.readouterr()
    assert out == 'total number of tickets =  102\nEach page will display 25 tickets, total  5 pages\n' \
                  'Please enter which page you want to view or type \'option\' back to option menu\n\n' \
                  'Ticket with Subject: Sample ticket: Meet the ticket Subject Id 1 opened by 15063870387 on 2016-11-16 06:11:51\n' \
                  'Ticket with Subject: My radio model number d4030 is broken! Subject Id 3 opened by None on 2016-11-16 19:42:04\n' \
                  'Ticket with Subject: My radio model number a7335 is broken! Subject Id 4 opened by None on 2016-11-16 20:40:41\n' \
                  'Ticket with Subject: My radio model number o166 is broken! Subject Id 5 opened by None on 2016-11-16 20:40:41\n' \
                  'Ticket with Subject: My radio model number w3969 is broken! Subject Id 6 opened by None on 2016-11-16 20:40:41\n' \
                  'Ticket with Subject: My radio model number p4997 is broken! Subject Id 7 opened by None on 2016-11-16 20:40:42\n' \
                  'Ticket with Subject: My radio model number e9347 is broken! Subject Id 8 opened by None on 2016-11-16 20:40:42\n' \
                  'Ticket with Subject: My radio model number h6175 is broken! Subject Id 9 opened by None on 2016-11-16 20:40:43\n' \
                  'Ticket with Subject: My radio model number l644 is broken! Subject Id 10 opened by None on 2016-11-16 20:40:43\n' \
                  'Ticket with Subject: My radio model number b6143 is broken! Subject Id 11 opened by None on 2016-11-16 20:40:43\n' \
                  'Ticket with Subject: My radio model number u763 is broken! Subject Id 12 opened by None on 2016-11-16 20:40:44\n' \
                  'Ticket with Subject: My radio model number f5865 is broken! Subject Id 13 opened by None on 2016-11-16 20:40:44\n' \
                  'Ticket with Subject: My radio model number n7931 is broken! Subject Id 14 opened by None on 2016-11-16 20:40:45\n' \
                  'Ticket with Subject: My radio model number t9509 is broken! Subject Id 15 opened by None on 2016-11-16 20:40:45\n' \
                  'Ticket with Subject: My radio model number g4201 is broken! Subject Id 16 opened by None on 2016-11-16 20:40:45\n' \
                  'Ticket with Subject: My radio model number z8946 is broken! Subject Id 17 opened by None on 2016-11-16 20:40:45\n' \
                  'Ticket with Subject: My radio model number m1439 is broken! Subject Id 18 opened by None on 2016-11-16 20:40:46\n' \
                  'Ticket with Subject: My radio model number l9962 is broken! Subject Id 19 opened by None on 2016-11-16 20:40:46\n' \
                  'Ticket with Subject: My radio model number h8924 is broken! Subject Id 20 opened by None on 2016-11-16 20:40:46\n' \
                  'Ticket with Subject: My radio model number c4212 is broken! Subject Id 21 opened by None on 2016-11-16 20:40:47\n' \
                  'Ticket with Subject: My radio model number b2235 is broken! Subject Id 22 opened by None on 2016-11-16 20:40:47\n' \
                  'Ticket with Subject: My radio model number p2785 is broken! Subject Id 23 opened by None on 2016-11-16 20:40:47\n' \
                  'Ticket with Subject: My radio model number u7189 is broken! Subject Id 24 opened by None on 2016-11-16 20:40:48\n' \
                  'Ticket with Subject: My radio model number g8166 is broken! Subject Id 25 opened by None on 2016-11-16 20:40:48\n' \
                  'Ticket with Subject: My radio model number x2162 is broken! Subject Id 26 opened by None on 2016-11-16 20:40:48\n'