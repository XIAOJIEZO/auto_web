import test_admin_login
import test_user_login
import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()

    suite.addTest(loader.loadTestsFromModule(test_admin_login))
    suite.addTest(loader.loadTestsFromModule(test_user_login))


    runner.run(suite)