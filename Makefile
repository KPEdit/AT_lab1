PYTHON_DIALOG = python3 ./laba/Dialog.py
PYTHON_GEN = python3 ./laba/TestGenerate.py
PYTHON_TEST = python3 ./laba/TestDialog.py
TEST_LOGS = ./tests/logs
TEST_DIR = ./tests
TESTS = ${shell find ${TESTS_DIR} -name '*.test'}

N=50000
M=100
CHECK_FIND = _100.log

run:
	${PYTHON_DIALOG}

test:
	@for f in ${TESTS}; do ${PYTHON_TEST} $${f} ${TEST_LOGS}; done

generate:
	${PYTHON_GEN} ${TEST_DIR} ${N} ${M}

check:
	ls ./tests/logs | grep ${CHECK_FIND} | while read file; do sha256sum ./tests/logs/$$file; done