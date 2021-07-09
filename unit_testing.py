import unittest


class unit_testing(unittest.TestCase):

    def test_method_1(self):
        self.assertTrue("foo".islower())

    def test_method_2(self):
        try:
            self.assertEqual("foo".upper(), "foo".lower())
        except AssertionError:
            self.assertNotEqual("foo".upper(), "foo".lower())
        else:
            pass  # else condition to be added later
        finally:
            print("Method completed")

    def test_method_3(self):
        pass


if __name__ == "__main__":
    unittest.main()
