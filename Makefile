init:
	pip install -r requierments.txt

run-api:
	flask --app app run

run-queue:
	python3 ./app/services/queue_service.py

run-cron:
	python3 ./app/services/cron_service.py