<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>



You can change/configure the env variables if you wanna run project Localy.Delete Procfile to run locally.
Start db and adminer: with
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
