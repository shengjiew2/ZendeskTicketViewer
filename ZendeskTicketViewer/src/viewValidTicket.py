import datetime


#View Valid Tidcket function will take a valid ticket and then print out the information of the ticket
def viewValidTicket(ticket):
    update_date = ticket['updated_at']
    out = datetime.datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%SZ")
    part1 = ' '.join(('Ticket with Subject:', ticket['subject']))
    part2 = ' '.join(('Subject Id', str(ticket['id']).ljust(3,' '), 'opened by',str(ticket['assignee_id'])))
    part3 = ' '.join(('on', str(out)))
    print('  '+part1.ljust(60,' ')+part2[0:35].ljust(35,' ')+part3[0:22].ljust(22,' '))