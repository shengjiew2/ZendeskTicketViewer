import unittest
import requests

from third import view


class TestCase(unittest.TestCase):


    def test_is_ticket_a_ticket(self):
        user = 'shengjiew2@student.unimelb.edu.au'
        pwd = 'duiBUqi520/'
        response = requests.get('https://shengjie.zendesk.com/api/v2/tickets/1.json', auth=(user, pwd))
        data = response.json()
        ticket = data['ticket']
        self.assertEqual(view(ticket),'Ticket with Subject: Sample ticket: Meet the ticket Subject Id 1 opened by 15063870387 on 2016-11-16 06:11:51')


if __name__ == '__main__':
    unittest.main()