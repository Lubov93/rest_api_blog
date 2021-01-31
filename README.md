How to start


You can change/configure the env variables in ./scripts/env.sh Start db and adminer: with
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements/dev.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver

It will run the server
The server should run on http://127.0.0.1:8000/
API:
http://127.0.0.1:8000/api
To apply autopep8 and flake8 run:
$ make format
