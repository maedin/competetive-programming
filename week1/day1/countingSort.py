def countingSort(array):
    size = len(array)
    output = [0] * size
    k=max(array)+1
   
    count = [0] * k

  
    for i in range(0, size):
        count[array[i]] += 1
   

    for i in range(1, k):
        count[i] += count[i - 1]

    
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
    return array
    