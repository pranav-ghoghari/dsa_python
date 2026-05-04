def build_active_user_report(users: list[dict]) -> str:
        users_list = []
        for user in users:
            if "username" in user and "is_active" in user:
                if user.get("is_active") is True:
                    users_list.append(user.get("username"))
        if len(users_list):
            users_list = ", ".join(users_list)
        else:
            users_list = "none"
        return "Active users: " + users_list