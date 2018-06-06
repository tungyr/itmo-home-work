import random
import string


def password_generator(leng):
    while True:
        passw = []
        for i in range(leng):
            rand = random.choice(string.ascii_letters)
            passw.append(rand)
        passw = ''.join(passw)
        yield passw
