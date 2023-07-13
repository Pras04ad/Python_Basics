def bubblesort(data):
    l = len(data)
    
    for i in range(l-1):
        flag = 0
        for j in range(l-1):
            if data[j] > data[j+1]:
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
                flag = 1
        if flag == 0:
            break
            
    return data  
unsortedData = [12,52,1,3,7,89,0,2,5,4]
result = bubblesort(unsortedData)
print(result)

