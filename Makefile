BASEDIR=./bioinfoutils
TESTDIR=./bioinfoutils/tests

all : clean test

clean :
	@rm -rf `find ./ -type d -name "*__pycache__"`
test :
	@python3 ./main_tests.py
