PY=python
PIP= pip
test: tests/test.py
	$(PY) tests/test.py
install: requirements.txt
	$(PIP) install -r requirements.txt
run: src/main.py
	$(PY) main.py
