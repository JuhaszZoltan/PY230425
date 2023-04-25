from random import randint

print('\u0048')
print(chr(97))

print('random jelszó:')

for _ in range(16):
    arj:int = randint(0, 2)
    if arj == 0: print(chr(randint(97, 122)), end='')
    elif arj == 1: print(chr(randint(65, 90)), end='')
    else: print(randint(0, 9), end='')