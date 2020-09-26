import shelve, random

def CreateDBAleatoria():
    """gera um data base nomeado DBAleatoria com 300 vetores com 500, 1000 e 10.000 elementos aleatórios entre 0 e 100.000"""
    
    dataBase = shelve.open('DBAleatoria')
    for num in range(1,50+1): 
        dt = []
        while len(dt) < 500:
            dt.append(random.randint(0,100000)) 
        dataBase[str(num)] = dt

    for num in range(51,80+1): 
        dt = []
        while len(dt) < 1000: 
            dt.append(random.randint(0,100000)) 
        dataBase[str(num)] = dt

    for num in range(81,83+1):
        dt = []
        while len(dt) < 10000: 
            dt.append(random.randint(0,100000)) 
        dataBase[str(num)] = dt
    dataBase.close()

def CreateDBOrdenada():
    """gera um data base nomeado DBOrdenada com 300 vetores com 500, 1000 e 10.000 elementos ordenados crescentemente entre 0 e 100.000"""

    dataBase = shelve.open('DBOrdenada')
    for num in range(1,50+1): 
        dt = []
        while len(dt) < 500: 
            dt.append(random.randint(0,100000)) 
        dataBase[str(num)] = sorted(dt)

    for num in range(51,80+1): 
        dt = []
        while len(dt) < 1000: 
            dt.append(random.randint(0,100000)) 
        dataBase[str(num)] = sorted(dt)

    for num in range(81,83+1): 
        dt = []
        while len(dt) < 10000: 
            dt.append(random.randint(0,100000)) 
        dataBase[str(num)] = sorted(dt)
    dataBase.close()  

def CreateDBInversa():
    """gera um data base nomeado DBInversa com 300 vetores com 500, 1000 e 10.000 elementos Ordenados em ordem decrescente entre 0 e 100.000"""
    
    dataBase = shelve.open('DBInversa')
    for num in range(1,50+1): 
        dt = []
        while len(dt) < 500: 
            dt.append(random.randint(0,100000))
        dt = [ele for ele in reversed(sorted(dt))]
        dataBase[str(num)] = dt

    for num in range(51,80+1): 
        dt = []
        while len(dt) < 1000: 
            dt.append(random.randint(0,100000)) 
        dt = [ele for ele in reversed(sorted(dt))]
        dataBase[str(num)] = dt

    for num in range(81,83+1): 
        dt = []
        while len(dt) < 10000: 
            dt.append(random.randint(0,100000)) 
        dt = [ele for ele in reversed(sorted(dt))]
        dataBase[str(num)] = dt
    dataBase.close()