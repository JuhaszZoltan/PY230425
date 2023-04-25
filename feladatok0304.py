nevek:list[str] = []
nev:str = '_'
while len(nevek) < 10 and nev != '':
    nev = input('írj be egy nevet: ')
    if nev != '': nevek.append(nev)

nevek.sort()

for nev in nevek:
    print(nev, end=' ')

print(f'\nnevek száma: {len(nevek)}')