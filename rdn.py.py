def right_dominant(L):
    D=[]  
    max_so_far=float('-inf') 
    
    for i in range(len(L)-1, -1, -1):
        if(L[i]>max_so_far):  
            D.append(L[i])  
            max_so_far = L[i]  

    return D[::-1]  
    ##################or##################
    #D.reverse()    
    #return D

L=[9, 10, 2, 5, 3]
print("Right dominant elements:", right_dominant(L))
