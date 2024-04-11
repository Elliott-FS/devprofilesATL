Rememmber to use python -m pip install django when installing django in ubuntu.
"python3 manage.py runserver" runs server from my ubuntu terminal.
From top folder run source djangoenv/bin/activate to turn on venv from my terminal. 
"python3 manage.py makemigrations/python3 manage.py migrate" to make and send migrations from my terminal. 
Need to redo some data had to revert some migrations and fix bad data re-add projects from admin panel
Fixed data issue

Important files:
In main project file manage.py has scripts to run the server and controll the backend at a high level.
Inner devsearchATL file has settings.py which is the control file for the backend. Also urls.py which has the main path and admin path. Main path has include method that includes the urls from the projects file which is the file for the app on this backend. 
 In the projects file ,which is an app running off this backend, you will see urls.py again and views.py. urls.py has path methods which take in a url, file, and a name for the path. The views file has methods that return the render function which takes a request obj, file path of the html file in templates, and a context object to pass in any needed dictionaries.