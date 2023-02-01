init:
	pip install -r requierments.txt

run-api:
	flask --app main run

run-queue:
	python3 ./services/queue_service.py

run-cron:
	python3 ./services/cron_service.py