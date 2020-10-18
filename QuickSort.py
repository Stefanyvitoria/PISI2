import sys
sys.setrecursionlimit(1000000)

def quickSort(arr,low,high): 
	if low < high: 

		pi = partition(arr,low,high) 

		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high)

def partition(arr,low,high): 
	i = ( low-1 )		  
	pivot = arr[high]	 # pivô 

	for j in range(low , high): 
		if arr[j] <= pivot: 
		
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 


comp = trocas = 0
def quickSort_Registros(arr,low,high): 
	if low < high: 

		pi = partition_Registros(arr,low,high) 

		quickSort_Registros(arr, low, pi-1) 
		quickSort_Registros(arr, pi+1, high) 


def partition_Registros(arr,low,high): 
    global comp, trocas
    i = ( low-1 )
    pivot = arr[high]	 # pivô

    for j in range(low , high): 
        comp += 1
        if arr[j] <= pivot: 
            trocas += 1
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 

    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
