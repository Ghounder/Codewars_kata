import math
def binary_array_to_number(arr):
    arr.reverse()
    print(arr)
    a=0
    index=0
    for i in range(0, arr.count(1)):
        num=arr.index(1,index)
        print(num)
        a+=math.pow(2, num)
        index=num+1
    return(int(a))
