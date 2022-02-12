from utils import *
import functools

class Location:

    def __init__(self, index:list):
        self.index = index

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Location):
            return False
        a = self.index
        b = __o.index
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False

        return True
    
    def __hash__(self):
        return hash(str(self.index))
    
    def __str__(self) -> str:
        return str(self.index)



if __name__ == "__main__":
    a = Location([1, 2, 3])
    b = Location([2, 1, 4])
    c = Location([2, 2, 5])
    l = [a, b, c]
    sorted_l = sorted(l, key=functools.cmp_to_key(compare_locations))
    
    for l in sorted_l:
        print(l)