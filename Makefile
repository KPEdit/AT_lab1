PYTHON = python3 ./laba/Dialog.py
PYTHON_TEST = python3 ./laba/TestDialog.py
TEST_LOGS = ./tests/logs
TEST_DIR = ./tests
TESTS = ${shell find ${TESTS_DIR} -name '*.test'}

run:
	${PYTHON}


test:
	@for f in ${TESTS}; do ${PYTHON_TEST} $${f} ${TEST_LOGS}; done