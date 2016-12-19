USER=$(shell whoami)

docker-build:
	docker build -t purchase_orders:$(USER) .

docker-run:
	docker run -dP --name purchase-orders-$(USER) purchase_orders:$(USER)
	docker ps -l

docker-rm:
	docker rm -f purchase-orders-$(USER)

.PHONY: docker-build docker-run docker-rm
