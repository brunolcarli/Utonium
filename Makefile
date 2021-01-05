run:
	python manage.py runserver 0.0.0.0:6777 --settings=utonium.settings.common

install:
	pip install -r utonium/requirements/common.txt

migrate:
	python manage.py makemigrations --settings=utonium.settings.common
	python manage.py migrate --settings=utonium.settings.common

replit_pipeline:
	make install
	make migrate
	make run

shell:
	python manage.py shell --settings=utonium.settings.common
