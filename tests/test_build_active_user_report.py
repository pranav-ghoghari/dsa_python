import unittest
from python_baseline.build_active_user_report import build_active_user_report

class UserNameTest(unittest.TestCase):
    def test_multiple_users(self) -> None:
        users = [
            {"username": "pranav", "is_active": True},
            {"username": "manshi", "is_active": False},
            {"username": "nishi", "is_active": True},
            {"username": "rushab", "is_active": True}
        ]
        self.assertEqual( build_active_user_report(users),"Active users: pranav, nishi, rushab")

    def test_missing_keys(self) -> None:
        users = [
                {"username": "pranav", "is_active": True},
                {"username": "manshi", },
                {"is_active": True},
                {"username": "rushab", }
        ]
        self.assertEqual(build_active_user_report(users), "Active users: pranav")

    def test_empty_input(self) -> None:
        users = []
        self.assertEqual(build_active_user_report(users), "Active users: none")

