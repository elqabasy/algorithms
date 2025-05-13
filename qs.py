def partition(A, p, r):
    pivot = A[p] 
    i = p - 1 
    j = r + 1 
    
    while(True):
        j -= 1
        while(A[j] > pivot):
            j -= 1
        
        i += 1
        while(A[i] < pivot):
            i += 1
        
        if(i < j): 
            A[i], A[j] = A[j], A[i]  
        else:
            return j  

def quicksort(A, p, r):
    if(p < r):
        q = partition(A, p, r)
        quicksort(A, p, q)
        quicksort(A, q + 1, r)

A = [5, 3, 2, 6, 4]
print("Before Sorting:", A)
quicksort(A, 0, len(A) - 1)
print("After Sorting:", A)






