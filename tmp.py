import sys
sys.setrecursionlimit(1000000)

comp = trocas = 0

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
    return (comp,trocas)

def quickSortHelper(alist,first,last):
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    global comp, trocas
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            comp += 1
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            comp += 1
            rightmark = rightmark -1

        
        if rightmark < leftmark:
            done = True
        else:
            trocas += 1
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    
    trocas += 1
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    
    return rightmark

#import random
#dados = [ele for ele in range(100)]
dados = [ele for ele in range(100,0,-1)]
#dados = [random.randint(0,20) for _ in range(100)]

print(quickSort(dados))
print(dados)