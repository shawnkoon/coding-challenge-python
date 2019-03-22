.PHONY: install
install:
	pip3 install -r requirements.txt

.PHONY: ci
ci:
	python3 -m unittest discover -v -b

.PHONY: test
test:
	python3 -m unittest src/$(module)/test_app.py -v -b
