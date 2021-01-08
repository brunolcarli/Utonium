run:
	python3 manage.py runserver 0.0.0.0:8088 --settings=utonium.settings.production

install:
	pip3 install -r utonium/requirements/common.txt

migrate:
	python3 manage.py makemigrations --settings=utonium.settings.common
	python3 manage.py migrate --settings=utonium.settings.common

replit_pipeline:
	make install
	make migrate
	make run

shell:
	python3 manage.py shell --settings=utonium.settings.common

train:
	python3 manage.py daemons --model train --settings=utonium.settings.common