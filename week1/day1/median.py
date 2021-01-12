def Median(nlist,llist):
    listed=sorted(llist)
    k=int(nlist/2)
    if (nlist%2==0):
        
        m=(listed[k-1]+listed[k])/2
       
    else:
        m=listed[k]
    return m