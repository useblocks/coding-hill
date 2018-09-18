class A:
    def __init__(self):
        super().__init__()
        print("A")


class B(A):
    def __init__(self):
        super().__init__()
        print("B")


class C:
    def __init__(self):
        super().__init__()
        print("C")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")


if "main" in __name__:
    D()
