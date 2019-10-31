PY=python
PIP= pip
test: tests/test.py
	$(PY) analyzer/test.py
install: requirements.txt
	$(PIP) install -r requirements.txt
run: analyzer/main.py
	$(PY) main.py
