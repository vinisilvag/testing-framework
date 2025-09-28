from framework.test_case import TestCase
from framework.test_loader import TestLoader
from framework.test_runner import TestRunner
from framework.test_suite import TestSuite

from .test_spy import TestSpy
from .test_stub import TestStub
from .test_test_case import TestCaseTest


class TestLoaderTest(TestCase):
    def test_create_suite(self):
        loader = TestLoader()
        suite = loader.make_suite(TestStub)
        assert len(suite.tests) == 3

    def test_create_suite_of_suites(self):
        loader = TestLoader()
        stub_suite = loader.make_suite(TestStub)
        spy_suite = loader.make_suite(TestSpy)

        suite = TestSuite()
        suite.add_test(stub_suite)
        suite.add_test(spy_suite)

        assert len(suite.tests) == 2

    def test_get_multiple_test_case_names(self):
        loader = TestLoader()
        names = loader.get_test_case_names(TestStub)
        assert names == ["test_error", "test_failure", "test_success"]

    def test_get_no_test_case_names(self):
        class Test(TestCase):
            def foobar(self):
                pass

        loader = TestLoader()
        names = loader.get_test_case_names(Test)
        assert names == []


def run_test():
    loader = TestLoader()
    suite = loader.make_suite(TestLoaderTest)
    runner = TestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_test()
