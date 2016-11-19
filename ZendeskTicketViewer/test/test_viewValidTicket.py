import datetime
import json
from pprint import pprint

with open('page1.txt') as data_file:
    data = json.load(data_file)
pprint(data)

def viewValidTicket(ticket):
    update_date = ticket['updated_at']
    out = datetime.datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%SZ")
    print('Ticket with Subject:', ticket['subject'], 'Subject Id', ticket['id'], 'opened by',
          ticket['assignee_id'], 'on', out)

def test_answer(capsys):
    viewValidTicket(data['tickets'][0])
    out,err = capsys.readouterr()
    assert out == 'Ticket with Subject: Sample ticket: Meet the ticket Subject Id 1 opened by 15063870387 on 2016-11-16 06:11:51\n'