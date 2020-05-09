creds = {
    "SW-1": {"username": "admin", "password": "admin", "secret":"admin"},
    "SW-2": {"username": "admin", "password": "admin", "secret":"admin"},
    "SW-3": {"username": "admin", "password": "admin", "secret":"admin"},
    "SW-4": {"username": "admin", "password": "admin", "secret":"admin"},
    "SW-5": {"username": "admin", "password": "admin", "secret":"admin"}, 
    "SW-6": {"username": "admin", "password": "admin", "secret":"admin"}
    }


def adapt_user_password(host):
    host.username = creds[f"{host}"]["username"]
    host.password = creds[f"{host}"]["password"]
    host.secret = creds[f"{host}"]["secret"]
