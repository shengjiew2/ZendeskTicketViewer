import requests
from viewValidTicket import viewValidTicket
import userData
#This function will take a Ticket Id AND return A ticket or print error
def chooseOneTicket(id):
    response = requests.get(userData.GET+'/api/v2/tickets/'+str(id)+'.json', auth=(userData.user, userData.pwd))
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        print('Please check your input ticket ID and try again later:)\n')
        return


    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    ticket = data['ticket']
    viewValidTicket(ticket)
    print()



