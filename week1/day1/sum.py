def findsum(a,b):
    if (len(b)>len(a)):
        t=b
        b=a
        a=t
    result=""
    n1=len(a)
    n2=len(b)
    #reversing to access the unit , the tenth ...digit respectivily 
    a=a[::-1]
    b=b[::-1]
    carry=0
    for i in range(n1):
        sum=(int(a[i]) + int(b[i])+carry)
        result += chr(sum%10+48)
        carry=int(sum/10)
    print(result)
    for i in range(n1,n2):
        sum=(int(n1[i])+carry)
        result +=chr(sum%10+48)
        carry=int(sum/10)
    if(carry):
        result += char(carry)
    result=result[::-1]
    return result