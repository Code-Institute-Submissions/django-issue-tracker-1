travis testing markdown code:
[![Build Status](https://travis-ci.org/marcuscistudent/django-issue-tracker.svg?branch=master)](https://travis-ci.org/marcuscistudent/django-issue-tracker)

django_issue_tracker

The project brief was to design product which would be of use to businessess.
The issue tracker is meant to be purchased so that teams can log problems,
monitor there progress and mark them as complete.

there is also a blog system so people can list and edit their issues and 
they will be ranked based on their number of views.

The user can add, update and remove posts as well as mark them as complete

The features of this app are the login, logout, register account.
The create, remove, update and delete functions
the add photo, log views
and finally the shopping cart function which uses AWS

login allows users to see their account details
the shopping cart allows the user to purchase multiple access
to see and increase the views of each post
it also allows users to know which tasks have been completed



Technologies Used 
this product uses django, Aws to host the static files, jinja to render python,
stripe for the shopping cart
gunicorn to comunicate with heroku
heroku to host the app

The app uses bootstrap, jquery and fontawesome to improve the user exerience
by enhancing forms, menues and icons.

Testing

I have tested all parts of the product by submiting forms and using the crud functions.
The mian testing completed was using the django automated test framework


Deployment

the app is deployed on heroku and has also has been pushed to github. To deploy to heroku, I had
to make sure all of the environment variables were correct throughout the code, heroku and aws
I had to scale dynos, create a procfile and requirements.txt file. 

The first time I pushed my files to github, aws blocked my account becuase there was an error
in my gitignore file and i pushed my aws keys. I changed all of the keys, ignored my env.py and 
a few other files and then repushed successfully.


In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

the version deployed in heroku uses postrgres as the database 
the version which isnt deployed needs to have the env uncommented in the settings.py file
so that it can use djdatabseurl to run the databse from sqlite3.

to run locally uncomment the env int settings.py and hit run.