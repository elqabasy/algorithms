def insertion_sort(A):
    for j in range(1, len(A)):
        current_element=A[j]  
        i=j-1  
        
        while (i>=0 and A[i]>current_element):
            A[i+1]=A[i]  
            i-=1  

        A[i+1]=current_element  
    return A  

A=[7, 2, 5, 1, 9]
print("Before Sorting:", A)  
print("After Sorting: ", insertion_sort(A))  
