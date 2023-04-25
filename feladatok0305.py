from random import randint

szamok:list[int] = []

for _ in range(50):
    rnd_szam:int = randint(5, 49) * 2 + 1
    szamok.append(rnd_szam)

for i in range(len(szamok)):
    print(szamok[i], end=' ')
    if (i+1) % 10 == 0: print(end='\n')

i:int = 0
while i < len(szamok) and szamok[i] != 13:
    i += 1
if i < len(szamok): print('van benne 13')
else: print('nincs benne 13')

# ez pedig ugyan az
for n in szamok:
    if n == 13:
        print('van benne 13')
        break
else: print('nincs benne 13')

# és ez is
if 13 in szamok: print('van benne 13')
else: print('nincs benne 13')