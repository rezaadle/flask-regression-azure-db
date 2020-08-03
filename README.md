# flask-regression-azure-db
A web application with Python + Flask + PostgreSQL and deploy on Azure.

> virtualenv virt

> source virt/bin/activate

> pip install flask sklearn flask_script flask_migrate psycopg2-binary

export DBUSER = ...,
export DBPASS = ...,
export DBHOST = ...,
export DBNAME = ...

> export APP_SETTINGS="config.ProductionConfig"

* python manage.py db init
* python manage.py db migrate
* python manage.py db upgrade
* python manage.py runserver

> pip freeze > requirements.txt

You can find more info here:
https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc
