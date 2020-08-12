# Cecotec

### Docs

For seeing all the endpoints go to 127.0.0.1 and it will display a list of all the endpoints,
if you want more info of and endpoint select it (ex. 127.0.0.1/selected_endpoint) and the
rest_framework will auto-document it and show all the available options of filters, structure and methods.   
 
### Setup
> 📁cecotec
> > 📁cecotec
> > > 📁settings
> > > > 📝base.py

Set environment variables or change values in the base.py file. \
*EMAIL_HOST \
EMAIL_HOST_USER \
EMAIL_HOST_PASSWORD* 

### Default users

Admin: \
email: test@test.com \
password: 12345678A

Normal user: \
email: example@example.com
password: Qwerty123-

### Start server

Install dependencies 
```shell script
pip install -r requirements.txt
```
\
Create normal user 
```shell script
Go to http://127.0.0.1:8000/auth/register/
```
\
Create admin \
_email, password, confirm password_
```shell script
python manage.py createsuperuser --settings=cecotec.settings.base
```
\
Makemigrations and migrate
```shell script
python manage.py makemigrations --settings=cecotec.settings.base
python manage.py migrate --settings=cecotec.settings.base
```
\
Run server
```shell script
python manage.py runserver --settings=cecotec.settings.base
```

### Use demo
Login in the admin site 127.0.0.1/admin. \
Click on tickets and create a new one, when you save the ticket you will get an email in the specified email direction with an csv file in it.
