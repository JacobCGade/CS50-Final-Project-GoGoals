# My CS50 Final Project - GoGoals

GoGoals is a goal setting and tracking webapplication developed by Jacob Carsten Gade. GoGoals was made with the purpose and mission of
making it easier to achieve your goals. With GoGoals you are able to add goals into a template form, with steps, vision section, subgoals
and a deadline. These goals can be seen at their entirety or just the current step on the website, and each step can be marked as completed
or failed which will increment or decrement your number successes for that step.

## How GoGoals work

You begin of at the frontpage, here you can read about GoGoals and what it offers. You then have the opportunity to register for an account
and log in.

Registration includes:

 - First name
 - Last name
 - Username
 - Email
 - Password
 - Terms and Conditions checkbox (for fanciness and fun)

All the data from the registration can be edited later from the Profile page as long as the changes meet the same requirements as when
registring.

### User logged in

The webapplication uses sessions to identify the user and determine whether the user is logged in or not. The user ID is important since it
links the user to his/hers goals and more.

### Flask and Routing

The webapplication uses Flask and an app.py file to make dynamic HTML. The routes access the database and collects the needed data aswell as updating and checking the data.
Some routes have a login required check that makes sure that only a logged in user can access those pages. A layout HTML has been made and the
rest of the HTML pages work as template extensions.

### Database

A sqlite database is used to store a table of the users and their profile information and a table to store all goals added. Goals is being
linked to the user by a user ID. The password is stored in the users table after being hashed for safety purposes. The goals table also have
coloumns like 'Done' that stores information about whether or not a goal is done or not. This serves the purpose of selecting the right data
from the table.

### JavaScript and JQuery

JavaScript and JQuery is used to make the webpages more dynamic and user friendly.

### Styling

Styling is done by a CSS file and using Bootstrap.

### Helpers.py

A collection of a few function that this webapplication has in common with the CS50 finance project. This project is in part on the CS50
web track's distribution code.

## Getting Started

These instruction will get a copy of GoGoals up and running on your computer, for testing, development or just for fun.

### Prerequisites

Here is a list of the what this application uses, make sure that you have the neccessary packeges preinstalled.

- Sqlite3
- Flask
- phpLiteAdmin if preferred


### Downloading the Code

```
$ mkdir finalProjectJG
$ cd finalProjectJG
$ git clone https://github.com/JacobCGade/CS50-Final-Project-GoGoals.git
$ cd CS50-Final-Project-GoGoals
```

### Running the Flask server

To run the webapplication you need to type in the following in your terminal:

```
$ flask run
```

Make sure that you are in the projects folder.

## Possible Improvements

As I made this webapplication I thought of the following things to do to make it even better:

- Have the deadline send a flash or alert when it is close and when it is overdue.
- Have the webapplication send sms texts to the user as reminders to do the current step.
- Use the success and fail data to show how well the user is during, maybe in a diagram of some sort.
- Gain some sort of exp for completing goals and steps to work as motivation.
- Have friends that you can follow and see some of their goals and keep them accountable so you motivate eachother.


## Short Video Showcasing GoGoals

https://youtu.be/IEmCFxoxfVo









