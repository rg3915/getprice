install:
	pip install -r requirements.txt

migrate:
	./manage.py makemigrations
	./manage.py migrate

createuser:
	./manage.py createsuperuser --username='admin' --email=''

selenium_quotation:
	python selenium/selenium_quotation.py

backup:
	./manage.py dumpdata core --format=json --indent=2 > fixtures.json

load:
	./manage.py loaddata fixtures.json

run:
	./manage.py runserver

initialdata:
	./manage.py stores
	./manage.py categorys
	./manage.py products
	./manage.py quotations