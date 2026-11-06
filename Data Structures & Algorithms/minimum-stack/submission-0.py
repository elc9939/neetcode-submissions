class MinStack:

    def __init__(self):
        self.m = None
        self.lst = []
        

    def push(self, val: int) -> None:
        if self.m == None:
            self.m = val
        elif val < self.m:
            self.m = val
        self.lst.append([val, self.m])

    def pop(self) -> None:
        self.lst.pop()
        if len(self.lst) == 0:
            self.m = None
        else:
            self.m = self.lst[-1][1]

    def top(self) -> int:
        return self.lst[-1][0]

    def getMin(self) -> int:
        return self.m
