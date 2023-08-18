
'when a function calls itself it is called recursion'
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(sys.getrecursionlimit()-500)
i=1
def test():
    global i
    print("Today is Friday=",i)
    i=i+1
    test()

test()