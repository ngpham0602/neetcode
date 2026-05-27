class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        if 0 <= i < self.length:
            return self.arr[i]


    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.length:
            self.arr[i] = n
        return


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1
            
    def popback(self) -> int:
        if self.length == 0:
            raise Exception("The length of an array cannot be 0")
        last_idx = self.length - 1
        value = self.arr[last_idx]
        self.length -= 1
        return value

 

    def resize(self) -> None:
        new_cap = self.capacity * 2
        new_arr = [0] * new_cap
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_cap
        



    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
