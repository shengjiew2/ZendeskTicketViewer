import datetime


#View Valid Tidcket function will take a valid ticket and then print out the information of the ticket
def viewValidTicket(ticket):
    update_date = ticket['updated_at']
    out = datetime.datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%SZ")
    print('Ticket with Subject:', ticket['subject'], 'Subject Id', ticket['id'], 'opened by',
          ticket['assignee_id'], 'on', out)
