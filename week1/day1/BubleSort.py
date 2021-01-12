def buble_sort(n):
    for i in range(len(n)-2,-1,-1):
        for k in range(i+1):
            if (n[i]>n[i+1]):
                t=n[i]
                n[i]=n[i+1]
                n[i+1]=t
            
                
    return n