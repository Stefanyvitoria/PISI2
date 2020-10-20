import sys
sys.setrecursionlimit(1000000)

def quickSort(arr):
    quick_Sort(arr,0,len(arr)-1)
    
def quick_Sort(arr,low,high): 
	if low < high: 
		pi = partition(arr,low,high) 
		quick_Sort(arr, low, pi-1) 
		quick_Sort(arr, pi+1, high)

def partition(arr,low,high): 
	i = ( low-1 )		  
	pivot = arr[high]	 #pivô 
	for j in range(low , high): 
		if arr[j] <= pivot: 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 
	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 




def quickSort_registros(arr):
    global comp, trocas
    comp = trocas = 0
    quick_Sort_registros(arr,0,len(arr)-1)
    return (comp,trocas)

def quick_Sort_registros(arr,low,high): 
	if low < high: 
		pi = partition_registros(arr,low,high) 
		quick_Sort_registros(arr, low, pi-1) 
		quick_Sort_registros(arr, pi+1, high) 

def partition_registros(arr,low,high): 
    global comp, trocas
    i = ( low-1 )
    pivot = arr[high]	 #pivô
    for j in range(low , high): 
        comp += 1
        if arr[j] <= pivot: 
            trocas += 1
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 
    trocas += 1
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 


from time import process_time

def Calcula_Tempo_Quick(DB):

    temp500 = []
    for j in range(1,50+1):

        j = str(j)
        ti = process_time()
        quickSort(DB[j])
        tf = process_time()

        temp500.append(tf - ti)

    temp1000 = [] 
    for j in range(51,80+1):
        j = str(j)
        ti = process_time()
        quickSort(DB[j])
        tf = process_time()

        temp1000.append(tf - ti)
    
    temp10000 = []
    for j in range(81,83+1):
        j = str(j)

        ti = process_time()
        quickSort(DB[j])
        tf = process_time()

        temp10000.append(tf - ti)
    
    return ( sum(temp500)/50, sum(temp1000)/30, sum(temp10000)/3)

if __name__ == "__main__":
    #print(quickSort_registros([ele for ele in range(501,1001)]))
    import shelve
    DB = shelve.open('DBOrdenada')
    print(Calcula_Tempo_Quick(DB))
