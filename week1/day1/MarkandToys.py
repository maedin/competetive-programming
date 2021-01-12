def MarkandToys(k,n):
    list=sorted(n)
    c=[]
    j=0
    for i in range(len(list)):
        j+=list[i]
        if (j<=k):
            c +=[list[i]]
    return len(c)
        