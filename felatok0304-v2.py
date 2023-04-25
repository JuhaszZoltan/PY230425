nevek:list[str] = []

for _ in range(10):
    nev:str = input('írj be egy nevet: ')
    if nev != '': nevek.append(nev)
    else: break

nevek.sort()
for n in nevek: print(n, end=' ')