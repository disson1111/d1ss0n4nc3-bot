import json
import os


FILE = "users.json"


def load_users():
    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            users,
            f,
            ensure_ascii=False,
            indent=4
        )


def create_user(user_id):
    users = load_users()

    uid = str(user_id)

    if uid not in users:
        users[uid] = {
            "cards": [],
            "last_open": "",
            "best_rarity": "нет"
        }

        save_users(users)


def get_user(user_id):
    users = load_users()
    uid = str(user_id)

    if uid not in users:
        create_user(user_id)
        users = load_users()

    return users[uid]


def update_user(user_id, data):
    users = load_users()

    users[str(user_id)] = data

    save_users(users)
