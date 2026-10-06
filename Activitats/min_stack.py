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
        return None

    def top(self) -> int:
        if self.pila:
            return self.pila[-1]
        return None

    def getMin(self) -> int:
        if self.minim:
            return self.minim[-1]
        return None