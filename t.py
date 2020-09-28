import random
def quicksort(alist, first, last):
    if first < last:
        q = partition(alist, first, last)
        quicksort(alist, first, q)
        quicksort(alist, q+1, last)

def partition(alist,f,l):
    x = alist[random.randint(f,l)]
    i = f-1
    
    for j in range(f,l+1):
        if alist[j] <= x:
            i = i+1
            alist[i], alist[j] = alist[j], alist[i]

    return i


import random, sys
sys.setrecursionlimit(1000000)

a = [ele for ele in range(100000,0,-1)]
print(len(a))

quicksort(a,0, len(a)-1)
print("\n",'#'*50, end='\n\n')
print(a)

b = [ele for ele in range(1,100001)]

print(b==a)
