import json
import random

def save_json(users):
    with open("random_password_generation.json", "w") as file:
        data = [user.to_dict() for user in users]
        json.dump(data, file)

def open_json():
    with open("random_password_generation.json", "r") as file:
        try:
            data = json.load(file)
            users = []
            for i in data:
                users.append(Passwords(site=i["site"], login=["login"], password=["password"]))
            return users
        except:
            return []

class Passwords:
    def __init__(self, site, login, password):
        self.site = site
        self.login = login
        self.password = password

    def to_dict(self):
        return {
            "site": self.site,
            "login": self.login,
            'password': self.password
        }

users = open_json()
password = []
site = input("Введите сайт: ")
while site != "q":
    login = input("Введите login: ")
    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(65, 90)))
    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(97, 122)))
    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(48, 57)))
    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(33, 126)))
    random.shuffle(password)
    users.append(Passwords(site=site, login=login, password=''.join(password)))
    print('Сгенерированный пароль: {}'.format(''.join(password)))
    site = input("Введите сайт: ")
    if site == "q":
        save_json(users)
