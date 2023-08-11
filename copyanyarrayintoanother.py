from numpy import *

arr=array([1,2,3,4,5])
print(arr,id(arr))
arr2=arr  #aliasing
print(arr2,id(arr2))

# arr2[0]=5000
# print(arr,id(arr))
# print(arr2,id(arr2))

# what if u ant different address
arr3=arr.view()  # shallow copy
print(arr3,id(arr))

arr3[2]=96563
print(arr3,id(arr3))
print(arr,id(arr))

# what if u wwant differetn address as well as changes of one
#does not effect another

print("Deep copy")
arr4=arr.copy()  # deep copy
print(arr4,id(arr4))

arr4[2]=67676
print(arr4,id(arr4))
print(arr,id(arr))