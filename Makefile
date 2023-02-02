env:
	python3 -m venv .mailer_env

init:
	pip install -r requierments.txt

run:
	docker-compose up -d --force-recreate