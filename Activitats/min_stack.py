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
            min=self.pila[0]
            for n in self.pila:
                if min>n:
                    min=n
            return min