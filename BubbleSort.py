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
