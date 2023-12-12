MAIN = cosmic.py
PY = python3

all: unittest localtest check_style clean
	@echo "All done!"

localtest:
	@cat 1.in | $(PY) $(MAIN) | diff - 1.ans
	@echo "All local tests passed!"

unittest:
	pytest test.py

check_style:
	flake8 comsic.py --count --show-source --statistics
	flake8 cosmic.py --count --show-source --statistics

clean:
	rm -rf __pycache__
	rm -rf *.pyc
