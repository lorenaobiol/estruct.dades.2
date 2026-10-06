class MinStack:

    def __init__(self):
        self.pila=[]
        self.minim=[]

    def push(self, val: int) -> None:
        self.pila.append(val)
        if not self.minim or val <= self.minim[-1]:
            self.minim.append(val)


    def pop(self) -> None:
        if self.pila:
            p=self.pila.pop()
            if p == self.minim[-1]:
                self.minim.pop()

    def top(self) -> int:
        if self.pila:
            return self.pila[-1]

    def getMin(self) -> int:
        print(self.pila, self.minim)
        if self.minim:
            return self.minim[-1]