import requests
import datetime


# Set the request parameters
GET = 'https://shengjie.zendesk.com'
url = 'https://shengjie.zendesk.com/api/v2/tickets.json'
user = 'shengjiew2@student.unimelb.edu.au'
pwd = 'duiBUqi520/'

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))
#response = requests.get(GET+'/api/v2/tickets.json', auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()

# Example 1: Print the name of the first group in the list
# print( 'First group = ', data['groups'][0]['name'] )

# Example 2: Print the name of each group in the list
ticket_list = data['tickets']
print('total number of tickets = ',len(ticket_list))
if __name__ == '__main__':
    for ticket in ticket_list:
        update_date = ticket['updated_at']
        #out = datetime.strptime(update_date, '%Y-%m-%dT%H:%M:%S.%Z').strftime("%m/%d/%y")
        out = datetime.datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%SZ")
        print('Ticket with Subject ',ticket['subject'],'opened by',ticket['assignee_id'] ,'on',out)

        #print(ticket['id'])


        #day 1: Now it will give me how many tickets in total and display them in a list
        # Now What I will do next will be scan input and react
