class MinStack:

    def __init__(self):
        self.pila=[]

    def push(self, val: int) -> None:
        self.pila.append(val)

    def pop(self) -> None:
        if self.pila:
            self.pila.pop()

    def top(self) -> int:
        if self.pila:
            return self.pila[-1]

    def getMin(self) -> int:
        if self.pila:
            ordenada=sorted(self.pila)
            return ordenada[0]