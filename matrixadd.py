from numpy import *
arr=array([
    [1,2,3],
    [3,4,5],
    [6,7,8],
    [6,6,6]
])



arr2=array([
    [1,2,3],
    [3,4,5],
    [6,7,8],

])

#print(arr+arr2)
print(arr@arr2)
print(dot(arr,arr2))

print(diagonal(arr2))