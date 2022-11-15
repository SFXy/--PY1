import random
import string
def get_random_password(length = 8) -> str:
    return ''.join(random.sample(string.ascii_letters + string.digits, length))  # TODO написать функцию генерации случайных паролей

print(get_random_password())
