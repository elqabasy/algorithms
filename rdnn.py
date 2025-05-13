def right_dominant(L):
    D=[]
    for i in range(len(L)):
        is_dominant=True
        for j in range(i+1,len(L)):
            if(L[i]<=L[j]):
                is_dominant=False
                break
        if(is_dominant):
            D.append(L[i])
    return D

L=[10,9,5,13,2,7,1,8,4,6,3]
print("Right dominant elements: ", right_dominant(L))
