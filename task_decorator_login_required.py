from functools import wraps
import hashlib

def make_token(username, password): 
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()




auth = []


def login_required(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if func.__name__ not in auth:
                with open('token.txt') as f:
                    saved_crdntls = f.read()
                    chance = 0
                    while chance < 3:
                        usr_login = input("Enter login:" )
                        usr_pass = input("Enter pass:" )
                        punched_crdntls = make_token(usr_login, usr_pass)
                        if punched_crdntls == saved_crdntls:
                            auth.append(str(func.__name__))
                            return func()
                        else:
                            chance += 1
                        return None
            else:
                auth.append(str(func.__name__))
                return func()
        return wrapper
