import json
from pprint import pprint
from test_viewValidTicket import viewValidTicket

with open('page1.txt') as data_file:
    data = json.load(data_file)
pprint(data)

#This only test the existing ticket reaction
def chooseTicket(id):
    ticket = data['tickets'][id]
    viewValidTicket(ticket)




def test_answer(capsys):
    viewValidTicket(data['tickets'][0])
    out,err = capsys.readouterr()
    assert out == 'Ticket with Subject: Sample ticket: Meet the ticket Subject Id 1 opened by 15063870387 on 2016-11-16 06:11:51\n'

