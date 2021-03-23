IMAGE = vahidmostofi/pca-hpa-test:latest

default:
	@echo "=============Building docker images============="
	docker build -t $(IMAGE) .

push: default
	@echo "=============Pushing docker images============="
	docker login
	docker push $(IMAGE)