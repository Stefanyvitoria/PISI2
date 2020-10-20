import shelve, random


dataBase = shelve.open('DBInversa')


for ele in range(1,len(dataBase)+1):
    if ele == 50:
        print(ele)

    if ele == 80:
        print(ele)
    print(dataBase[str(ele)])
    print(len(dataBase[str(ele)]))
    print()
    

print(len(dataBase))