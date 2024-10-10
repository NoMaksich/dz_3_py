import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Введите длину пароля: "))
generated_password = generate_password(length)
print("Сгенерированный пароль:", generated_password)
