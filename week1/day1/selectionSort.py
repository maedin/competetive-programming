def selection_sort(n):
    for i in range(len(n)-1):
        imin=i
        for k in range(i+1,len(n)):
            if(n[k]<n[imin]):
                imin=k
        t=n[i]
        n[i]=n[imin]
        n[imin]=t
    return n