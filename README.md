# ZendeskTicketViewer

Zendesk Ticket Viewer is a small application which has 2 different features:

    1.display all tickets in a list (page through when more than 25 tickets returned)
    2.display individual ticket details

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install them
```
To run this app, you need to download Python3 in your local machine.   [Python3 for windows](https://www.python.org/downloads/release/python-352/) - where you can download python3 in your local windows machine
```

### Installing
```
python -m ensurepip
pip install requests
pip install pytest
```

## Running the tests

go to the test folder and run pytest

### Break down into end to end tests

Explain what these tests test and why

```
test_viewValidTicket it will test method viewValidTicket(ticket) it will take a ticket as input and check wether it gives expected output(a string with ticket info)
test_disp
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
