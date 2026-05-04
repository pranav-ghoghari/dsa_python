
def collect_active_usernames(users: list[dict]) -> list[str]:
        users_list = []
        for user in users:
            if "username" in user and "is_active" in user:
                if user.get("is_active") is True:
                    users_list.append(user.get("username"))
        return users_list

