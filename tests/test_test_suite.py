from framework.test_case import TestCase
from framework.test_result import TestResult
from framework.test_suite import TestSuite

from .test_stub import TestStub
from .test_test_case import TestCaseTest


class TestSuiteTest(TestCase):
    def test_suite_size(self):
        suite = TestSuite()

        suite.add_test(TestStub("test_success"))
        suite.add_test(TestStub("test_failure"))
        suite.add_test(TestStub("test_error"))

        assert len(suite.tests) == 3

    def test_suite_success_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub("test_success"))

        suite.run(result)

        assert result.summary() == "1 run, 0 failed, 0 error"

    def test_suite_multiple_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub("test_success"))
        suite.add_test(TestStub("test_failure"))
        suite.add_test(TestStub("test_error"))

        suite.run(result)

        assert result.summary() == "3 run, 1 failed, 1 error"


def run_test():
    result = TestResult()
    suite = TestSuite()

    suite.add_test(TestCaseTest("test_result_success_run"))
    suite.add_test(TestCaseTest("test_result_failure_run"))
    suite.add_test(TestCaseTest("test_result_error_run"))
    suite.add_test(TestCaseTest("test_result_multiple_run"))
    suite.add_test(TestCaseTest("test_was_set_up"))
    suite.add_test(TestCaseTest("test_was_run"))
    suite.add_test(TestCaseTest("test_was_tear_down"))
    suite.add_test(TestCaseTest("test_template_method"))

    suite.add_test(TestSuiteTest("test_suite_size"))
    suite.add_test(TestSuiteTest("test_suite_success_run"))
    suite.add_test(TestSuiteTest("test_suite_multiple_run"))

    suite.run(result)
    print(result.summary())


if __name__ == "__main__":
    run_test()
