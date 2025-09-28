from framework.test_case import TestCase


class MyTest(TestCase):
    def set_up(self):
        print("set_up")

    def tear_down(self):
        print("tear_down")

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")

    def test_c(self):
        print("test_c")


def run_test():
    test = MyTest("test_a")
    test.run()

    test = MyTest("test_b")
    test.run()

    test = MyTest("test_c")
    test.run()


if __name__ == "__main__":
    run_test()
