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
    return [comp, troca]

