all: build run

build:
	sudo docker build -t follownext-backend .

run:
	docker run -v $(PWD):/app follownext-backend

run-it:
	docker run -v $(PWD):/app -it --entrypoint /bin/bash follownext-backend