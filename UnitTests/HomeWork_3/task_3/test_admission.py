import unittest
from random import shuffle

from admission import User, UserRepository


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User('login', 'password')

    def test_successful_authenticate(self):
        self.assertTrue(self.user.authenticate(self.user.login, self.user.password))

    def test_failed_authenticate_wrong_login(self):
        self.assertFalse(self.user.authenticate('', self.user.password))

    def test_failed_authenticate_wrong_password(self):
        self.assertFalse(self.user.authenticate(self.user.login, ''))

    def test_failed_authenticate(self):
        self.assertFalse(self.user.authenticate('', ''))


class TestUserRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.authenticated_user = User('login', 'password')
        self.authenticated_user.authenticate(self.authenticated_user.login, self.authenticated_user.password)

        self.not_authenticated_user = User('another_login', 'password')

        users = ([User(f'login{i}', 'password', is_admin=True) for i in range(5)] +
                 [User(f'login{i}', 'password') for i in range(5, 20)])
        shuffle(users)
        for user in users:
            user.authenticate(user.login, user.password)

        self.repository = UserRepository(users)

    def test_add_authenticated_user(self):
        self.repository.add_user(self.authenticated_user)
        self.assertTrue(self.authenticated_user in self.repository.users)

    def test_add_not_authenticated_user(self):
        self.repository.add_user(self.not_authenticated_user)
        self.assertFalse(self.authenticated_user in self.repository.users)

    def test_logout_not_admins(self):
        self.repository.logout_not_admins()
        self.assertTrue(all(user.is_admin for user in self.repository.users))


_loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTest(_loader.loadTestsFromTestCase(TestUser))
suite.addTest(_loader.loadTestsFromTestCase(TestUserRepository))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)