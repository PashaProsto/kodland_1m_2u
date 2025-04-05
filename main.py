import random, time, string

print('_-_-_-ГЕНЕРАТОР_-_-_-')
print('_-_-_-_ПАРОЛЕЙ_-_-_-_')

long = int(input('Введите длину пароля: '))

password = ''

for i in range(long):
    password += random.choice(string.printable)

time.sleep(1)

print('Ваш сгенерированный пароль: ', password)
