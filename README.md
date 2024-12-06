To make this project work, the following things are needed to be installed:

Django
Django Rest Framework
JWT Token for auth
psycopg2 
psycopg2 -binary for running the postgresql

commands to install:

pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install psycopg2-binary
pip install psycopg2


if changes are needed to be made in the repo list of the PostgreSQL then run these comnnnmands and then save the file

sudo nano /etc/apt/sources.list.d/pgdg.list
this command will open the file in text editor then paste the following by deleting any existing thing in the repo

deb [arch=amd64] https://apt.postgresql.org/pub/repos/apt focal-pgdg main

to save and exit the file hit CTRL + O and then ENTER and then CTRL + X to exit


paste these in the settings.py file of the project to make postgresql default database of the project:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'name of db',  # Name of your database
        'USER': 'username of the db',            # Database user
        'PASSWORD': 'password for db created at the time of db creation',        # Password for the database user
        'HOST': 'localhost',        # Host, usually 'localhost' for local development
        'PORT': '5432',             # Default PostgreSQL port
    }
}

Also for the email authentication to work paste these in the settings.py file
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'  # Replace with your Gmail address
EMAIL_HOST_PASSWORD = 'your_app_password_here'  # Replace with the App Password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

Now to use the API, we have the following addresses and some of them requires header to be passed in postman as well. The header are simply the bearer token and we need to supply them with the access token or in some cases refresh token(for logout specially)

1. Registeration
Method = POST
http://127.0.0.1:8000/api/accounts/register/
body: 
{
    "email": "admin@example.com",
    "username": "Admin",
    "password": "admin",
    "role": "admin"
}

2. Login:
Method = POST
http://127.0.0.1:8000/api/accounts/login/
body: 
{
    "username": "Employee",
    "password": "Employee"
} 
after login it will generate an access token and refresh token that we need for other process:

3. To get the count of indiviual and total user via Dashboard

METHOD = GET
http://127.0.0.1:8000/api/accounts/dashboard/
in Auth we have to select bearer token and supply the access token generated from login

4. Change-Password
METHOD = POST
http://127.0.0.1:8000/api/accounts/change-password/
supply the access token in auth 
body:
{
    
    "old_password": "employee",
    "new_password": "Employee"
}

5. Update Profile
Method = POST
http://127.0.0.1:8000/api/accounts/update-profile/
auth -> bearer token -> access token
body:
{ 
  "username": "Employee",
  "gender": "male",
  "age": 23
}

6. Reset Password:
Method = POST
body: 
{
    "email: "email of the
}
this will generate a uid and token that we will be needing

7. Confirm Reset Password
Method: POST
body:
{
    "uid": "uid generated from reset password",
    "token": "generated from reset password",
    "new_password": "employee3"
}

8. Logout:
Method: POST
body: 
{
    "refresh-token" : "token generated from login"
}


to run the server and migrations:

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

if using python-3 replace python with python3.

