<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">REST API BLOG </h3>

  <p align="center">
    Rest api blog using Django-restframework
    <br />
    <a href="https://github.com/Lubov93/rest_api_blog"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://apirestblog.herokuapp.com">View blog</a>
    ·
    <a href="https://t.me/pythonDevLuba">Report Bug</a>
    ·
    <a href="">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

![](https://github.com/Lubov93/rest_api_blog/blob/master/blog/static/111.jpg)









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
