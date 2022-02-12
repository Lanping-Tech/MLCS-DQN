from typing import List, Set
from location import Location
from sequence import Sequence

import numpy as np


class MLCS:

    def __init__(self, charset:Set[str], seqs:List[str]):
        self.charset = charset
        self.seqs = seqs
        self.build_start_end()
        char_list = list(charset)
        self.successors_table = []
        for i in range(len(char_list)):
            self.successors_table.append([])
            for j in range(len(seqs)):
                seq = Sequence(seqs[j])
                self.successors_table[i].append(seq.build_successors(char_list[i]))
        self.max_level = len(seqs[0])
        self.seqs_len = [len(seq) for seq in seqs]
    
    def build_start_end(self):
        self.start = Location([0] * len(self.seqs))
        self.end = [0] * len(self.seqs)
        for i in range(len(self.seqs)):
            self.end[i] = len(self.seqs[i])
        self.end = Location(self.end)

    def next_locations(self, current:Location):
        next_locations = []
        for i in range(len(self.successors_table)):
            tmp = []
            for j in range(len(self.seqs)):
                successor = self.successors_table[i][j][current.index[j]]
                if successor < 0 or successor > self.seqs_len[j]:
                    tmp.append(-1)
                    break
                else:
                    tmp.append(successor)
            if tmp[-1] > 0:
                next_locations.append(Location(tmp))
        return next_locations
    
    def load_from_file(file_name:str):
        with open(file_name, 'r', encoding='utf-8') as f:
            charset = set()
            seqs = []
            for line in f:
                line = line.strip()
                if line[0] == '>':
                    continue
                else:
                    seqs.append(line)
                    charset.update(line)
            return MLCS(charset, seqs)



if __name__ == "__main__":
    m = MLCS.load_from_file('data.txt')
    # print(m.start)
    # print(m.end)
    # print(m.charset)
    # print(m.seqs)
    # print(m.successors_table)
    # print(m.max_level)
    nexts = m.next_locations(Location([3,7,6]))
    for n in nexts:
        print(n)
    