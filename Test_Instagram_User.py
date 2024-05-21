import unittest
from Jmurugan_class import InstagramUser
import os
import csv

class TestInstagramUser(unittest.TestCase):
    def setUp(self):
        # We are creating a new clean environment for testing as we don't to test them in the real one.
        self.test_users_file = 'test_users.csv'
        self.test_data_file = 'testuser_data.csv'
        self.user_manager = InstagramUser(filename=self.test_users_file)

        # We are adding users for testing.
        self.user_manager.add_or_update_user('testuser', 'testpass')

        # We are adding some random data for testing.
        self.user_manager.add_data('testuser', '5', '150', '75')  # Posts, followers, and likes in the list.

    def test_authenticate(self):
        # If the test is success:
        self.assertTrue(self.user_manager.authenticate('testuser', 'testpass'))
        # If the test is a failure:
        self.assertFalse(self.user_manager.authenticate('testuser', 'wrongpass'))

    def test_add_or_update_user(self):
        # We are testing the ability to add new users.
        self.user_manager.add_or_update_user('newuser', 'newpass')
        self.assertTrue(self.user_manager.authenticate('newuser', 'newpass'))

    def test_data_storage(self):
        # We are checking if the data is added properly.
        with open(self.test_data_file, mode='r') as file:
            data = list(csv.reader(file))
            self.assertEqual(len(data), 1) # Since I'm in windows the header doesn't count as one.

    def test_summarize_data(self):
        def test_summarize_data(self):
    # We are making sure if the data exists.
            with open('testuser_data.csv', 'r') as file:
                data = list(csv.reader(file))
                self.assertGreater(len(data), 1)  # We are making sure that atleast one row exists. Since header doesn't count we keep it as 1. Else we will keep it as 2.

    # We are running the test for the summary.
            result = self.user_manager.summarize_data('testuser', 'Average likes per post')
            self.assertIn('Average likes per post:', result)

    def tearDown(self):
# We are removing the current test files so that it wouldn't affect the other tests.
        try:
            os.remove(self.test_users_file)
            os.remove(self.test_data_file)
        except OSError:
            pass

if __name__ == '__main__':
    unittest.main()
