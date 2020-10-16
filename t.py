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

dados = [random.randint(0,50) for _ in range(100000,0,-1)]

a = dados.copy()
b = dados.copy()

print(a)
#print('#'*80)
print(b)

quick_sort(a,0,len(a))
b = sorted(b)

print('*'*80)

print(a)
#print('#'*80)
print(b)

print(a==b)