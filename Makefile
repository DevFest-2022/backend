all: build run

build:
	sudo docker build -t follownext-backend .

run:
	docker run -v $(PWD):/app -p 5001:5001 follownext-backend

run-it:
	docker run -v $(PWD):/app -p 5001:5001 -it --entrypoint /bin/bash follownext-backend