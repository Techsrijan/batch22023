def even_no(n):
    if n%2==0:
        return "even no"

print(even_no(25))

# can we pass function as argument-no

def test():
    print('hi')

#yes- anomymous function or lambda function

def even_no2(n):
    return n%2

print(even_no2(10))

def add(a,b):
    return a+b

# a fuction which has only one line --we can make lambda

f=lambda a,b:a+b
print(f(55,60))

print(f(4.5,6.3))