class A:
    def __init__(self):
        print("this is class a constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("this is class b constructor")


class C(B):
    def __init__(self):
        super().__init__()
        print("this is class C constructor")


c=C()