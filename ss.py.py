def selection_sort(L):
    n=len(L)  
    for i in range(n-1):  
        min_index=i  
        
        for j in range(i+1, n):
            if(L[j]<L[min_index]):  
                min_index=j  

        L[i], L[min_index]=L[min_index], L[i]  
    return L  

L = [15, 8, 2, 4]
print("Before Sorting:", L)
print("After Sorting: ", selection_sort(L))
