class User:
    def __init__(self, login: str, password: str, is_admin: bool = False):
        self._login = login
        self._password = password
        self._is_admin = is_admin
        self._is_authenticate = False

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @property
    def is_admin(self):
        return self._is_admin

    @property
    def is_authenticate(self):
        return self._is_authenticate

    def authenticate(self, login: str, password: str) -> bool:
        self._is_authenticate = self.login == login and self.password == password
        return self.is_authenticate

    def unauthenticate(self):
        self._is_authenticate = False

    def __eq__(self, other):
        return self.login == other.login

    def __hash__(self):
        return hash((self.login, self.password, self.is_authenticate))

    def __repr__(self):
        return f'User("{self.login}", is_admin={self.is_admin})'


class UserRepository:
    def __init__(self, users: list[User] = None):
        self._users = users
        if users is None:
            self._users = []

    @property
    def users(self):
        return self._users

    def add_user(self, user: User) -> None:
        if user.is_authenticate:
            self._users.append(user)

    def logout_not_admins(self) -> None:
        i = 0
        while i < len(self._users):
            if not self._users[i].is_admin:
                self._users[i].unauthenticate()
                self._users.remove(self._users[i])
                i -= 1
            i += 1