PY=python
PIP= pip
test: tests/test.py
	$(PY) test/test.py
install: requirements.txt
	$(PIP) install -r requirements
run: src/main.py
	$(PY) main.py
