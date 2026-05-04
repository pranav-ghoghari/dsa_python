import unittest
from python_baseline.collect_active_username import collect_active_usernames

class UserNameTest(unittest.TestCase):
    def test_multiple_users(self) -> None:
        users = [
            {"username": "pranav", "is_active": True},
            {"username": "manshi", "is_active": False},
            {"username": "nishi", "is_active": True},
            {"username": "rushab", "is_active": True}
        ]
        self.assertEqual( collect_active_usernames(users),["pranav", "nishi","rushab"])

    def test_missing_keys(self) -> None:
        users = [
                {"username": "pranav", "is_active": True},
                {"username": "manshi", },
                {"is_active": True},
                {"username": "rushab", }
        ]
        self.assertEqual(collect_active_usernames(users), ["pranav"])

    def test_empty_input(self) -> None:
        users = []
        self.assertEqual(collect_active_usernames(users), [])

