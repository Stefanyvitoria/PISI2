import sys, random
sys.setrecursionlimit(1000000)

def quick_sort(alist, first, last):
    """Odena um vetor em ordem crescente."""
    if first < last:
        q = partition(alist, first, last)
        quick_sort(alist, first, q)
        quick_sort(alist, q+1, last)

def partition(alist,f,l):
    x = alist[l-1] #pivô

    for i in range(f,l):
        if alist[i] <= x:
            f += 1
            l += 1
            alist[i], alist[f-1] = alist[f-1], alist[i]
        else:
            l += 1
    return f-1


comp = troca = 0
def R_quick_sort(alist, first, last):
    global comp, troca
    """Odena um vetor em ordem crescente."""
    if first < last:
        q = R_partition(alist, first, last)
        R_quick_sort(alist, first, q)
        R_quick_sort(alist, q+1, last)
        return [comp, troca]


def R_partition(alist,f,l):
    global comp, troca
    x = alist[l-1] #pivô

    for i in range(f,l):
        comp += 1
        if alist[i] <= x:
            f += 1
            l += 1
            troca += 1
            alist[i], alist[f-1] = alist[f-1], alist[i]
        else:
            l += 1
    return f-1
