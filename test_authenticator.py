import unittest
from authenticator import Authenticator

class TestAuthenticator(unittest.TestCase):
    def setUp(self):
        self.auth = Authenticator()

    def test_valid_credentials(self):
        self.assertEqual(self.auth.authenticate("user1", "password1"), "Access granted")

    def test_invalid_username(self):
        self.assertEqual(self.auth.authenticate("invalid_user", "password1"), "Access denied")

    def test_invalid_password(self):
        self.assertEqual(self.auth.authenticate("user1", "wrong_password"), "Access denied")

if __name__ == "__main__":
    unittest.main()