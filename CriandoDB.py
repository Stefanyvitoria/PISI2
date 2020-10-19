import shelve, random

def CreateDBAleatoria():
    """Gera um Data Base nomeado DBAleatoria com 50 vetores com 500 elementos,
    30 com 1000 e 3 com 10.000, todos em ordem aleatória e entre 0 e 10.000 elementos."""
    
    dataBase = shelve.open('DBAleatoria')
    
    for num in range(1,50+1): 
        vetor = [random.randint(0,10000) for _ in range(500)]
        dataBase[str(num)] = vetor

    for num in range(51,80+1): 
        vetor = [random.randint(0,10000) for _ in range(1000)]
        dataBase[str(num)] = vetor

    for num in range(81,83+1):
        vetor = [random.randint(0,10000) for _ in range(10000)] 
        dataBase[str(num)] = vetor
    
    dataBase.close()

def CreateDBOrdenada():
    """Gera um Data Base nomeado DBOrdenada com 50 vetores com 500 elementos,
    30 com 1000 e 3 com 10.000 elementos, todos ordenados crescentemente e entre 0 e 10.000 elementos."""

    dataBase = shelve.open('DBOrdenada')

    i,j =1,501
    for num in range(1,50+1): 
        vetor = [ele for ele in range(i,j)]
        dataBase[str(num)] = vetor
        i,j = j, j+500

    i,j = 1,1001
    for num in range(51,80+1):  
        vetor = [ele for ele in range(i,j)]
        dataBase[str(num)] = vetor
        i,j = j,j+1000

    i,j = 1,10001
    for num in range(81,83+1):  
        vetor = [ele for ele in range(i,j)]
        dataBase[str(num)] = vetor
        i,j = j,j+10000

    dataBase.close()  

def CreateDBInversa():
    """gera um data base nomeado DBInversa com 300 vetores com 500, 1000 e 10.000 elementos Ordenados em ordem decrescente entre 0 e 10.000"""
    
    dataBase = shelve.open('DBInversa')

    i,j = 0,500
    for num in range(1,50+1): 
        vetor = [ele for ele in range(j,i,-1)]
        dataBase[str(num)] = vetor
        i,j = j,j+500
    
    i,j = 0,1000
    
    for num in range(51,80+1): 
        vetor = [ele for ele in range(j,i,-1)]
        dataBase[str(num)] = vetor
        i,j = j,j+1000

    i,j = 0,10000
    for num in range(81,83+1): 
        vetor = [ele for ele in range(j,i,-1)]
        dataBase[str(num)] = vetor
        i,j = j,j+10000

    dataBase.close()