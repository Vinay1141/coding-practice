def dutch(arr):
    while(m<=h):
        if arr[m] == 0:
            arr[m],arr[l] = arr[l],arr[m]
            m+=1
            l+=1
        elif arr[m] == 1:
            m+=1
        else:
            arr[m],arr[h] = arr[h],arr[m]
            h-=1
    return arr
