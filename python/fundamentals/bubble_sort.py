def bubble_sort(arr):
    for i in range(len(arr)-1  ):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
x=[1,5,3,2,0,8]
print(bubble_sort(x))