def insertionsort(alist):
    """Ordena um vetor em ordem crescente."""
    for ind in range(1,len(alist)):
        currentvalue = alist[ind]
        position = ind

        while position > 0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def insertionsort_registros(alist):
    """Ordena um vetor em ordem crescente e retorna o número de comparações e trocas."""
    comp = 0
    troca = 0
    for ind in range(1,len(alist)):
        currentvalue = alist[ind]
        position = ind
        comp += 1
        while position > 0 and alist[position-1]>currentvalue:
            troca += 1
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue
    return (comp, troca)


from time import process_time

def Calcula_Tempo_insertion(DB):

    temp500 = []
    for j in range(1,50+1):

        j = str(j)
        ti = process_time()
        insertionsort(DB[j])
        tf = process_time()

        temp500.append(tf - ti)

    temp1000 = [] 
    for j in range(51,80+1):
        j = str(j)
        ti = process_time()
        insertionsort(DB[j])
        tf = process_time()

        temp1000.append(tf - ti)
    
    temp10000 = []
    for j in range(81,83+1):
        j = str(j)

        ti = process_time()
        insertionsort(DB[j])
        tf = process_time()

        temp10000.append(tf - ti)
    
    return ( sum(temp500)/50, sum(temp1000)/30, sum(temp10000)/3)

if __name__ == "__main__":
    import shelve
    DB = shelve.open('DBOrdenada')
    print(Calcula_Tempo_insertion(DB))
