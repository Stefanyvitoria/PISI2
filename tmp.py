def insertionsort(alist):
    """Ordena um vetor em ordem crescente."""
    for ind in range(1,len(alist)):
        currentvalue = alist[ind]
        position = ind

        while position > 0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue
   

a = [ele for ele in range(1,10001)]

from time import process_time
import shelve
DB = shelve.open('DBOrdenada')


ti = process_time()
insertionsort(a)
tf = process_time()

print(tf-ti)