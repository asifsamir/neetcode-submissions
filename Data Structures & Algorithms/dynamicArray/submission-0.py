class DynamicArray:
    
    def __init__(self, capacity: int):
        self.dynArray = [0]*capacity
        self.capacity = capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.dynArray[i]


    def set(self, i: int, n: int) -> None:
        self.dynArray[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.dynArray[self.size] = n
        self.size += 1


    def popback(self) -> int:
        self.size -= 1
        return self.dynArray[self.size]
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        tempArray = [0]*self.capacity
        for i in range(self.size):
            tempArray[i] = self.dynArray[i]
        self.dynArray = tempArray



    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity

