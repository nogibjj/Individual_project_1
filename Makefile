install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval srcipt/*.ipynb
	python -m pytest -vv --cov=src.lib

format:	
	black srcipt/*.py
	nbqa black srcipt/*.ipynb 

lint:
	nbqa ruff srcipt/*.ipynb
	ruff check srcript/*.py
		
all: install lint test format
