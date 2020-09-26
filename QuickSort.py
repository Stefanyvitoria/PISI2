def quicksort(alist, first, last):
    """Odena um vetor em ordem crescente."""
    if first < last:
        q = partition(alist, first, last)
        quicksort(alist, first, q-1)
        quicksort(alist, q+1, last)

def partition(alist,f,l):
    x = alist[l] #pivô
    i = f-1
    
    for j in range(f,l):
        if alist[j] <= x:
            i = i+1
            alist[i], alist[j] = alist[j], alist[i]
    alist[i+1],alist[l]  = alist[l], alist[i+1]
    return i+1


comp = 0
troca = 0
def quicksort_registros(alist, first, last):
    """Odena um vetor em ordem crescente e retorna o número de comparações e trocas."""
    global comp, troca
    
    if first < last:
        q = partition_registros(alist, first, last)
        quicksort_registros(alist, first, q-1)
        quicksort_registros(alist, q+1, last)
    return [comp, troca]

def partition_registros(alist,f,l):
    global comp, troca
    
    x = alist[l] #pivô
    i = f-1
    for j in range(f,l):
        comp += 1
        if alist[j] <= x:
            troca += 1
            i = i+1
            alist[i], alist[j] = alist[j], alist[i]
            
    troca += 1
    alist[i+1],alist[l]  = alist[l], alist[i+1]
    return i+1
