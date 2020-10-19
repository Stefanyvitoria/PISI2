def bubblesort(alist):
    """Ordena um vetor em ordem crescente."""
    n = len(alist)
    for j in range(n-1,0,-1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                

def bubblesort_regitros(alist):
    """Ordena um vetor em ordem crescente e retorna o número de comparações e trocas."""
    comp = 0
    troca = 0
    n = len(alist)
    for j in range(n-1,0,-1):
        for i in range(j):
            comp += 1
            if alist[i] > alist[i+1]:
                troca += 1
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return (comp, troca)

from time import process_time

def Calcula_Tempo_Bubble(DB):

    temp500 = []
    for j in range(1,50+1):

        j = str(j)
        ti = process_time()
        bubblesort(DB[j])
        tf = process_time()

        temp500.append(tf - ti)

    temp1000 = [] 
    for j in range(51,80+1):
        j = str(j)
        ti = process_time()
        bubblesort(DB[j])
        tf = process_time()

        temp1000.append(tf - ti)
    
    temp10000 = []
    for j in range(81,83+1):
        j = str(j)

        ti = process_time()
        bubblesort(DB[j])
        tf = process_time()

        temp10000.append(tf - ti)
    
    return ( sum(temp500)/50, sum(temp1000)/30, sum(temp10000)/3)

if __name__ == "__main__":
    import shelve
    DB = shelve.open('DBOrdenada')
    print(Calcula_Tempo_Bubble(DB))
