# Goals:

The work in this repository was designed as an app prototype for 
the Columbia design challenge on MTA transit improvements

## Credits & Sources
This is worth noting at the outset
A lot of the initial layout of this app (aside from most of the database processing functionality),
was adapted from Miguel Grinberg's website at blog.miguelgrinberg.com.

He is a great resource on getting started with Python Flask.

## Description
This is basically a Dashboard prototype that MTA workers could use at their stations to track the flow of 
passengers at their stationsi as well as the working of their turnstiles and so better allocate resources.

We use a SQL database (currently modelled with SQLite for prototyping) but we again employ a tool by Miguel Grinberg (flask-migrate) to help with migrating the database later on if necessary.

This database is currently just to track users but can later be used to track which turnstiles have caused problems and who fixed them.

## Methodology
Start up the flask server, a login page appears. currently login can be done with tester and test credentials respectively.
The main index page is where the action happens:
There is a table where we currently display all the turnstiles that we have data for.
This will later be changed to initially just show the groups which can be clicked to show the
individual turnstiles.
We use javascript to simulate real-live data coming in (which I believe the MTA could have) but
is currently just drawing from historical data spreadsheet, making request for data every 5 seconds
(which takes the next minute's data as a simulation).
Turn counts were calculated by assuming uniform distribution over the minutes throughout the duration.
This is definitely not representative, but since it's meant to take from live data, it is useful
for a demo.

## Future Work
As mentioned, we would like to display *groups* when we land on the index page rather than scrolling
through pages of turnstiles.
We would also like to add functionality where depending on how quickly the turn-rate for a particular 
turnstile changes over a certain period of time, it can be flagged for review in case broken
by the use of a button next to its name, and a worker would be sent a notification.

### Notes
There was some debate on whether to try and make this using angular, but we all
had more experience using Python.
There is a migration database file provided by flask-migrate that we can use 
to adapt our db at a later time.

There was no profile page used though this could be changed in case MTA wants it eg: to track which turnstiles they fixed

