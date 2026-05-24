def OddOccurring(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res

arr = []
n = int(input("Enter array size : "))
while(n):
    num = int(input("Enter array size : "))
    arr.append(num)
    n-=1
print("\n\nOdd occurring number is : ",OddOccurring(arr))
