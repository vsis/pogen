USER=$(shell whoami)

docker-build:
	docker build -t purchase_orders:$(USER) .

docker-run:
	touch db.sqlite3
	docker run -dPw /pogen --name purchase-orders-$(USER) --volume $(PWD)/db.sqlite3:/pogen/db.sqlite3 purchase_orders:$(USER)
	docker ps -l

docker-rm:
	docker rm -f purchase-orders-$(USER)

docker-init-database:
	docker exec -ti purchase-orders-$(USER) python3 manage.py migrate
	docker exec -ti purchase-orders-$(USER) python3 manage.py createsuperuser

run:
	python3 manage.py runserver 0.0.0.0:8080

run-80:
	python3 manage.py runserver 0.0.0.0:80

init-database:
	python3 manage.py migrate
	python3 manage.py createsuperuser

.PHONY: docker-build docker-run docker-rm docker-init-database run run-80 init-database
