BASEDIR=./bioinfoutils
TESTDIR=./bioinfoutils/tests

all : clean tests

clean :
	@rm -rf `find ./ -type d -name "*__pycache__"`
tests :
	@python3 ./main_tests.py
