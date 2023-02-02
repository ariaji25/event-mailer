env:
	python3 -m venv .mailer_env
	source .mailer_env/bin/activate

init:
	pip install -r requierments.txt

deploy:
	docker-compose up -d --force-recreate