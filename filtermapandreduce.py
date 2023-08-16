'''
Think of lambdas as one-line methods without a name. They work practically the same as any other method in Python
https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/
'''
from functools import reduce
l=[1,33,55,3,66,44,23,46,56]

def even_no2(n):
    return n%2

f=lambda n:n%2==0

even_l=list(filter(f,l))
print(even_l)

g=lambda a:a+10
output=list(map(g,even_l))
print(output)

h=lambda a,b:a+b
x=reduce(h,output)
print(x)