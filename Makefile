run:
	uvicorn main:app --reload

requirements-update:
	pip freeze > requirements.txt

requirements-install:
	pip install -r requirements.txt
