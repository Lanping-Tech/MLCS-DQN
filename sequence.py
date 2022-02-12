class Sequence:
    def __init__(self, strbases):
        self.strbases = strbases
        self.strbases = '.' + self.strbases

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases) - 1

    def charsets(self):
        return set(self.strbases)

    def char_at(self, pos):
        return self.strbases[pos + 1]
    
    def build_successors(self, c):
        successors = [-1 for i in range(len(self.strbases))]
        i = 0
        j = i + 1
        while i < len(self.strbases):
            if j == i:
                j += 1
            while j < len(self.strbases) and self.strbases[j] != c:
                j += 1
            if j == len(self.strbases):
                successors[i] = -1
            else:
                successors[i] = j
            i += 1
        return successors
    
