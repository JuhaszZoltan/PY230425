from random import randint

szamok:list[int] = []

for _ in range(20):
    rnd_szam:int = randint(50, 150)
    szamok.append(rnd_szam)

for szam in szamok:
    print(szam, end=' ')

osszeg:int = sum(szamok)

atlag:float = osszeg/len(szamok)

c:int = 0
for szam in szamok:
    if szam % 10 == 0:
        c += 1

print(f'\nszámok összege: {osszeg}')
print(f'számok átlaga: {atlag}')
print(f'0ra végződő számok száma: {c}')