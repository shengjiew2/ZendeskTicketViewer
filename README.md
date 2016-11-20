# ZendeskTicketViewer

Zendesk Ticket Viewer is a small application which has 2 different features:

    1.display all tickets in a list (page through when more than 25 tickets returned)
    2.display individual ticket details

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install them

To run this app, you need to download Python3 in your local machine.   
   [Python3 for windows](https://www.python.org/downloads/release/python-352/) - where you can download python3 in your local windows machine


### Installing
Open command window and run the following code
```
python -m ensurepip
pip install requests
pip install pytest
```

## Running the tests

go to the test folder and run pytest

### Tests and usage

test_viewValidTicket 
```
it will test method viewValidTicket(ticket) 
it will take a ticket as input and check if it gives expected output(a string with ticket info)
```
test_disp
```
it will test the helping method disp(page_num, data)
it is a helping method which helps viewAll method. It takes the data from a specific page and call viewValidTicket to print the tickets on the page
```
test_chooseTicket
```
it will test method chooseTicket(id)
it will take a ticket id and use the id to find a ticket and pass the ticket to viewValidTicket method
```
test_viewAll
```
it will test method viewAll
it will indecate user how many pages it has and ask for page number(which page do you want to view)

```


## Built With

* [pytest](http://doc.pytest.org/en/latest/) - The pytest doc, where I learned pytest from
* [ZendeskTicket](https://developer.zendesk.com/rest_api/docs/core/tickets) - Concept of zendesk ticket and usage
* [StackOverFlow](http://stackoverflow.com/) - Used to learn some other stuff
* [ReadmeFormat](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) -The readme format



## Authors

* **Shengjie Wang(Jessie)** - *Initial work* - [Zendesk](https://www.zendesk.com/)


## Acknowledgments

* A very simple app with simple features.

