build:
	docker build . -t whale_adoptions:dev

up:
	docker-compose up -d --build

cron:
	docker exec adoption_script python run.py

local:
	python3 -m venv ./venv
	./venv/bin/pip install wheel
	./venv/bin/pip install -r ./requirements.txt

local-clean:
	rm -rf venv

clean:
	docker-compose down

local-rebuild: local-clean local
rebuild: clean deps

.PHONY: build cron local local-clean clean rebuild