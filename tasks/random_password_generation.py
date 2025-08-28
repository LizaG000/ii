import random

class

password = []
for i in range(random.randint(2, 4)):
    password.append(chr(random.randint(65, 90)))
for i in range(random.randint(2, 4)):
    password.append(chr(random.randint(97, 122)))
for i in range(random.randint(2, 4)):
    password.append(chr(random.randint(48, 57)))
for i in range(random.randint(2, 4)):
    password.append(chr(random.randint(33, 126)))
random.shuffle(password)
print('Сгенерированный пароль: {}'.format(''.join(password)))