class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.lst = [None]*capacity



    def get(self, i: int) -> int:
        if i <= self.size:
            return self.lst[i]


    def set(self, i: int, n: int) -> None:
        if i < self.size:
            self.lst[i] = n


    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        self.lst[self.size] = n
        self.size += 1
        


    def popback(self) -> int:
        val = self.lst[self.size-1]
        self.size -= 1
        return val

 

    def resize(self) -> None:
        self.capacity = self.size * 2
        new_lst = [None] * self.capacity
        for i in range(self.size):
            new_lst[i] = self.lst[i]
        self.lst = new_lst
        


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
