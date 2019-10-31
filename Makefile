PY=python
PYT=pytest
PIP= pip
test: analyzer/test.py
	$(PYT) analyzer/test.py
install: requirements.txt
	$(PIP) install -r requirements.txt
run: analyzer/main.py
	$(PY) main.py
