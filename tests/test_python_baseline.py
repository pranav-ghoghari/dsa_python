import unittest

from python_baseline.assessment import build_deployment_report
from python_baseline.assessment import count_active_users
from python_baseline.assessment import deduplicate_preserve_order
from python_baseline.assessment import group_expenses_by_category
from python_baseline.assessment import normalize_username
from python_baseline.assessment import parse_feature_flags


class NormalizeUsernameTests(unittest.TestCase):
    def test_strips_whitespace_and_lowercases(self) -> None:
        self.assertEqual(normalize_username("  Ada Lovelace  "), "ada-lovelace")

    def test_collapses_multiple_spaces(self) -> None:
        self.assertEqual(normalize_username("Grace   Hopper"), "grace-hopper")

    def test_keeps_existing_hyphenated_words(self) -> None:
        self.assertEqual(
            normalize_username("  Mary-Jane   Watson "), "mary-jane-watson"
        )


class CountActiveUsersTests(unittest.TestCase):
    def test_counts_only_active_non_deleted_users(self) -> None:
        users = [
            {"name": "A", "is_active": True, "deleted": False},
            {"name": "B", "is_active": False, "deleted": False},
            {"name": "C", "is_active": True, "deleted": True},
            {"name": "D", "is_active": True},
        ]
        self.assertEqual(count_active_users(users), 2)

    def test_returns_zero_for_empty_list(self) -> None:
        self.assertEqual(count_active_users([]), 0)


class DeduplicatePreserveOrderTests(unittest.TestCase):
    def test_removes_duplicates_and_keeps_first_occurrence(self) -> None:
        items = ["api", "worker", "api", "web", "worker", "jobs"]
        self.assertEqual(
            deduplicate_preserve_order(items),
            ["api", "worker", "web", "jobs"],
        )

    def test_handles_empty_input(self) -> None:
        self.assertEqual(deduplicate_preserve_order([]), [])


class GroupExpensesByCategoryTests(unittest.TestCase):
    def test_groups_and_sums_amounts(self) -> None:
        expenses = [
            {"category": "travel", "amount": 120.0},
            {"category": "food", "amount": 15.5},
            {"category": "travel", "amount": 30.0},
            {"category": "software", "amount": 99.0},
        ]
        expected = {"travel": 150.0, "food": 15.5, "software": 99.0}
        self.assertEqual(group_expenses_by_category(expenses), expected)

    def test_returns_empty_dict_for_no_expenses(self) -> None:
        self.assertEqual(group_expenses_by_category([]), {})


class ParseFeatureFlagsTests(unittest.TestCase):
    def test_parses_flags_and_ignores_spaces(self) -> None:
        raw_config = "search=true, ads=false, beta = true"
        expected = {"search": True, "ads": False, "beta": True}
        self.assertEqual(parse_feature_flags(raw_config), expected)

    def test_returns_empty_dict_for_blank_input(self) -> None:
        self.assertEqual(parse_feature_flags("   "), {})

    def test_accepts_mixed_case_boolean_values(self) -> None:
        raw_config = "feature_a=True, feature_b=FALSE"
        expected = {"feature_a": True, "feature_b": False}
        self.assertEqual(parse_feature_flags(raw_config), expected)

    def test_raises_value_error_for_invalid_values(self) -> None:
        with self.assertRaises(ValueError):
            parse_feature_flags("search=yes")


class BuildDeploymentReportTests(unittest.TestCase):
    def test_formats_multiple_service_lines(self) -> None:
        services = [
            {"name": "api", "status": "healthy", "deployed_by": "sam"},
            {"name": "worker", "status": "degraded", "deployed_by": "jules"},
        ]
        expected = (
            "api: healthy (deployed by sam)\n"
            "worker: degraded (deployed by jules)"
        )
        self.assertEqual(build_deployment_report(services), expected)

    def test_returns_message_for_empty_input(self) -> None:
        self.assertEqual(build_deployment_report([]), "No services found.")


if __name__ == "__main__":
    unittest.main()
