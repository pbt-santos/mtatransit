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
passengers at their stations and so better allocate resources.

We will use a SQL database (currently modelled with SQLite for prototyping) but we again employ a tool by Miguel Grinberg (flask-migrate) to help with migrating the database later on if necessary.

### Notes
There was some debate on whether to try and make this using angular, but we all
had more experience using Python.
There is a migration database file provided by flask-migrate that we can use 
to adapt our db at a later time.
