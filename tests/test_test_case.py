from framework.test_case import TestCase
from framework.test_result import TestResult

from .test_stub import TestStub


class TestSpy(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.was_run = False
        self.was_set_up = False
        self.was_tear_down = False
        self.log = ""

    def set_up(self):
        self.was_set_up = True
        self.log += "set_up "

    def test_method(self):
        self.was_run = True
        self.log += "test_method "

    def tear_down(self):
        self.was_tear_down = True
        self.log += "tear_down"


class TestCaseTest(TestCase):
    def set_up(self):
        self.result = TestResult()

    def test_result_success_run(self):
        stub = TestStub("test_success")
        stub.run(self.result)
        assert self.result.summary() == "1 run, 0 failed, 0 error"

    def test_result_failure_run(self):
        stub = TestStub("test_failure")
        stub.run(self.result)
        assert self.result.summary() == "1 run, 1 failed, 0 error"

    def test_result_error_run(self):
        stub = TestStub("test_error")
        stub.run(self.result)
        assert self.result.summary() == "1 run, 0 failed, 1 error"

    def test_result_multiple_run(self):
        stub = TestStub("test_success")
        stub.run(self.result)
        stub = TestStub("test_failure")
        stub.run(self.result)
        stub = TestStub("test_error")
        stub.run(self.result)
        assert self.result.summary() == "3 run, 1 failed, 1 error"

    def test_was_set_up(self):
        spy = TestSpy("test_method")
        spy.run(self.result)
        assert spy.was_set_up

    def test_was_run(self):
        spy = TestSpy("test_method")
        spy.run(self.result)
        assert spy.was_run

    def test_was_tear_down(self):
        spy = TestSpy("test_method")
        spy.run(self.result)
        assert spy.was_tear_down

    def test_template_method(self):
        spy = TestSpy("test_method")
        spy.run(self.result)
        assert spy.log == "set_up test_method tear_down"


def run_test():
    result = TestResult()

    test = TestCaseTest("test_result_success_run")
    test.run(result)

    test = TestCaseTest("test_result_failure_run")
    test.run(result)

    test = TestCaseTest("test_result_error_run")
    test.run(result)

    test = TestCaseTest("test_result_multiple_run")
    test.run(result)

    test = TestCaseTest("test_was_set_up")
    test.run(result)

    test = TestCaseTest("test_was_run")
    test.run(result)

    test = TestCaseTest("test_was_tear_down")
    test.run(result)

    test = TestCaseTest("test_template_method")
    test.run(result)

    print(result.summary())


if __name__ == "__main__":
    run_test()
