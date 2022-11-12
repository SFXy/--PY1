import random
import string
def get_random_password(n = None) -> str:
    if n is None: n = 8
    return ''.join(random.sample(string.ascii_letters + string.digits, n))  # TODO написать функцию генерации случайных паролей

print(get_random_password())

