# EVENT MAILER

## About
A Flask Rest API application to create event, register event audiences, and create scheduled email to send to group of event audiences email

## Project Description
## - ```app```
The parent project folder that contains all of the python source code

### - ```api```
The python module that contains the Rest Api endpoints
### - ```config```
The python module that contains application config such as database config, and any environment variables for the application
### - ```controllers```
The python module that contains the Rest Api Endpoint Controllers
### - ```database```
The python module that contains the database connection with Pony orm
### - ```models```
The python module that contains the data models thas used by Rest Api for the request and response data
### - ```repositories```
The python module that contains the database tables definition with Pony orm and functions to do transaction with tables
### - ```services```
The python module that contains the extra services for this application. There are two extra service are in the services moduel :
1. Queue Entry Service, the service that run with cron job for every minutes to check date and time of which email should sent. This service will add email to queue to send one by one to every event audience email.
2. Queue Executor Service, the scheduled service that run  every 5 second to send email that has been stored to queue with 'PENDING' status. 
### - ```usecases```
The python module that contains the usecase function for every usecase the need by this flask application. Such as usecase for crate event, get event, create audience, get audiences, create scheduled email and etc.
### - ```utils```
The python module that contains the some helper function such as loger and etc.

# Quick Start
## Development
To start develop this application, follow steps bellow:
1. Create python virtual environment by exute Makefile command
    ```make env```
2. Install the required python library by execute Makefile command
    ```make init```
3. Start coding...

## Run application with docker
To run this application with docker, make sure you have install docker engine first, and fill out the ```.env``` file as like the ```.env.example``` file.

Specialy for ```queue_entry_service``` make sure that the ```.env``` file exist under the service folder as like ```.env.example``` file. There are unknown reason caused the service did not read the env variable that was declared in docker-compose file.

Then run Makefile command 
```make run```


## Postman Collection
This is the [postman collection](https://api.postman.com/collections/6659073-5636e8b2-65ca-468e-9897-84c88ad92d49?access_key=PMAT-01GR8XHZ09C2GE6AWTX4PF0AW4) for the Rest Api

## Notes
For email sender, use gmail email and create thirdparty app password from your gmail account.
You can follow [this](https://support.google.com/mail/answer/185833?hl=en) instruction to setup the thirdparty app password
 
