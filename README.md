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

login allows users to see their specific account details
the shopping cart allows the user to purchase multiple access
the upvote and complete allows users to know which tasks have been completed



Technologies Used 
this product uses django, Aws to host the static files, jinja to render python,
stripe for the shopping cart
gunicorn to comunicate with heroku
heroku to host the app

JQuery
The project uses JQuery to simplify DOM manipulation.
Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

Credits
Content
The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from ...
Acknowledgements
I received inspiration for this project from X