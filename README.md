# flask-regression-azure-db
A web application with Python + Flask + PostgreSQL and deploy on Azure.

>> virtualenv virt

>> source virt/bin/activate

>> pip install flask sklearn flask_script flask_migrate psycopg2-binary

export DBUSER = ...
export DBPASS = ...
export DBHOST = ...
export DBNAME = ...

>> export APP_SETTINGS="config.ProductionConfig"

* python manage.py db init
* python manage.py db migrate
* python manage.py db upgrade
* python manage.py runserver

>> pip freeze > requirements.txt
