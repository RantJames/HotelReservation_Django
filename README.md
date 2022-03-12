# HotelReservation_Django
Hotel Reservation API on Django

# Steps to run application

# clone project
git clone https://github.com/RantJames/HotelReservation_Django.git

# Install Dependencies
pip install -r requirements.txt

# Update Database details in DjangoProject\classDemo\settings.py
'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': '<database_name>, 'HOST': , 'PORT': <database_port>, 'USER': , 'PASSWORD': }

# To perform migrations
python manage.py makemigrations python manage.py migrate

# Run application
python manage.py runserver

# Application Url to display Hotel list
http://127.0.0.1:8000/hotelList/

# Application Url to display Reservation list
http://127.0.0.1:8000/resList/

# Application Url to perform GET and POST on Hotel list
http://127.0.0.1:8000/HotelGenList/

# Json request body for POST
{
        "name": "Hilton Inn",
        "address": "Halifax",
        "price": 250,
        "rooms_available": 50
 }

# Application Url to perform GET and POST on Reservation list
http://127.0.0.1:8000/ResGenList/

# Json request body for POST
{
        "hotel_name": "Hilton Inn",
        "confirmation_num": 1000,
        "checkin_date": "2022-03-08",
        "checkout_date": "2022-03-09",
        "guestInReservation": [
            {
                "first_name": "Rubin",
                "last_name": "James",
                "gender": "M",
                "address": "Halifax",
                "age": 26
            },
            {
                "first_name": "Vedant",
                "last_name": "Thapa",
                "gender": "M",
                "address": "Halifax",
                "age": 23
            },
            {
                "first_name": "Nimish",
                "last_name": "Sawant",
                "gender": "M",
                "address": "Halifax",
                "age": 29
            }
        ]
    }
    
# Url parameters to perform GET and display hotel availability
http://127.0.0.1:8000/ResGenList/?address=Halifax&checkin_date=2022-03-11&checkout_date=2022-03-10

# Screenshots in folder
HotelReservation_Django/Resources/Screenshots/
