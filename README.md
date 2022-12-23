# letsride
#1. clon the repo

git clon https://github.com/prafull25/letsride.git

#2. Create virtual environment

$ python3 -m venv venv

$ source venv/bin/activate

#3. Install requirements

$ pip install -r requirements.txt

#4. Make  migrations

$ python manage.py makemigrations

$ python manage.py migrate

#5. create Super User (Optional)

$ python manage.py createsuperuser

# 6. Runserver

$ python manage.py runserver


#API Endpoints are:(exapmle)
http://127.0.0.1:8000/rider/request/

http://127.0.0.1:8000/rider/riderinfo/

http://127.0.0.1:8000/rider/myrequest/<reqid>/

http://127.0.0.1:8000/rider/apply/<riderid>/

http://127.0.0.1:8000/rider/matchingrides/

respective requestbody can be seen from the models and the viewa

#Notes:
1. I am assuming if no of asset for rider and requester is differ but rider can take only for one requester
2. cron jobs can we used to update the status of request every minutes

