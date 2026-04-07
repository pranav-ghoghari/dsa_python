"""Hands-on Python baseline assessment.

Implement the functions below without changing their names or signatures.
Each function focuses on a core Python skill used in day-to-day software work.
"""

from __future__ import annotations

def normalize_username(raw_username: str) -> str:
    """Return a simple username from a human-entered name.

    Rules:
    - Remove leading and trailing whitespace.
    - Convert everything to lowercase.
    - Replace runs of whitespace with a single hyphen.

    Examples:
    - "  Ada Lovelace  " -> "ada-lovelace"
    - "Grace   Hopper" -> "grace-hopper"
    """

    raw_words = raw_username.split()
    return '-'.join(raw_words).lower()
def count_active_users(users: list[dict]) -> int:
    """Count users who are active and not deleted.

    Each user is a dictionary that may contain:
    - "is_active": bool
    - "deleted": bool

    Count a user only when:
    - is_active is True
    - deleted is not True
    """
    count = 0
    for user in users:
        active = user.get("is_active")
        status = user.get("deleted")
        if active is True and status is not True:
            count+=1
    return count


def deduplicate_preserve_order(items: list[str]) -> list[str]:
    """Return a new list with duplicates removed.

    Keep the first occurrence of each item and preserve the original order.

    Example:
    - ["api", "worker", "api", "web"] -> ["api", "worker", "web"]
    """
    new_list = []
    for item in items:
        if item not in new_list:
            new_list.append(item)
    return new_list


def group_expenses_by_category(expenses: list[dict]) -> dict[str, float]:
    """Sum expense amounts by category.

    Each expense dictionary contains:
    - "category": str
    - "amount": float

    Example:
    - [
          {"category": "travel", "amount": 120.0},
          {"category": "food", "amount": 15.5},
          {"category": "travel", "amount": 30.0},
      ]
      becomes {"travel": 150.0, "food": 15.5}
    """
    total_exp = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in total_exp:
            total_exp[category] += amount
        else:
            total_exp[category]=amount

    return total_exp

def parse_feature_flags(raw_config: str) -> dict[str, bool]:
    """Parse feature flags from a config string.

    Input format:
    - "search=true,ads=false,beta=true"

    Rules:
    - Ignore extra spaces around keys, values, and commas.
    - Return an empty dictionary for an empty or whitespace-only string.
    - Accepted values are "true" and "false", case-insensitive.
    - Raise ValueError for any other value.

    Example:
    - "search=true, ads=false" -> {"search": True, "ads": False}
    """
    config = {}
    if raw_config.strip() == "":
        return {}
    split_string = raw_config.split(',')
    for sub_string in split_string:
        section = sub_string.split('=')
        key = section[0].strip()
        value_text = section[1].strip().lower()
        if value_text == 'true':
            config[key] = True
        elif value_text == 'false':
            config[key] = False
        else:
            raise ValueError
    return config

def build_deployment_report(services: list[dict]) -> str:
    """Build a human-readable deployment report.

    Each service dictionary contains:
    - "name": str
    - "status": str
    - "deployed_by": str

    Output format:
    - "api: healthy (deployed by sam)"
    - "worker: degraded (deployed by jules)"

    Join multiple lines with "\\n".
    Return "No services found." when the input list is empty.
    """
    if not services:
        return "No services found."

    report = []
    for service in services:
        txt = f"{service['name']}: {service['status']} (deployed by {service['deployed_by']})"
        report.append(txt)
    return "\n".join(report)

