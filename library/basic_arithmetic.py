from typing import Union

class BasicArithmetic:
    def add(self, *args:Union[int, float]) -> float:
        total = 00.00
        for num in args:
            total += num
        return total
    
print(BasicArithmetic().add(1, 2, 3, 4, 5))