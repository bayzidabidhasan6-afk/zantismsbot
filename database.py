import json
import os

from config import USERS_FILE, SERVICES_FILE, NUMBERS_FILE


def create_file(filename, default_data):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4)


create_file(USERS_FILE, [])
create_file(SERVICES_FILE, [])
create_file(NUMBERS_FILE, [])


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def add_user(user_id):
    users = load_json(USERS_FILE)
    if user_id not in users:
        users.append(user_id)
        save_json(USERS_FILE, users)


def get_users():
    return load_json(USERS_FILE)


def get_services():
    return load_json(SERVICES_FILE)


def save_services(data):
    save_json(SERVICES_FILE, data)


def get_numbers():
    return load_json(NUMBERS_FILE)


def save_numbers(data):
    save_json(NUMBERS_FILE, data)
