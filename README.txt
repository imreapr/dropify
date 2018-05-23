PROJECT TITLE:
Dropify is a program that searches for trendy products.
The user inputs a keyword for a product and the program will run and
find a product for them and give them information on in. The program
uses things like number of orders and keyword trends in conjunction with
web crawling to find a good product for them.

GETTING STARTED:
In order to run this program open up a command line and cd into the
Dropify/mysite folder. Then enter the command: python manage.py runserver
After the server has started go to your web browser and go to 
127.0.0.1:8000/webapp to begin using the webapp.

PREREQUISITES:
In order to use this program you will need to have Python3 and the Python web 
framework Django installed on your computer. You can download Python 3 from the 
official Python website and you can install Django using pip with the command:
pip install django

BUILT WITH:
Outside libraries that I used for this project are requests and lxml.
Both can be install via pip using: pip install requests and
pip install lxml.

FILES:
Files created and modified by me are Dropify/mysite/webapp/views.py, 
Dropify/mysite/webapp/utils.py, Dropify/mysite/webapp/forms.py, 
Dropify/mysite/mysite/urls.py,and the entire Dropify/mysite/webapp/Templates folder.

AUTHOR:
Tyler O'Hare

LICENSE:
Apache License 2.0

ACKNOWLEDGEMENTS:
Thank you to Sentdex and TheNewBoston on youtube for helping me learn the basic
of Django.