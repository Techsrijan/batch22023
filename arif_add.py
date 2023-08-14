name="Akash"
def add(x,y):
    c=x+y
    print(c)

def mul(x,y):
    c=x*y
    print(c)
print(__name__)

if __name__=='__main__':
    def securefunction():
        print("this will run when original file run")
    securefunction()
