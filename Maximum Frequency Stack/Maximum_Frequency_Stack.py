'''Maximum Frequency Stack'''
class FreqStack:
    '''class FreqStack'''

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        '''Push value onto the stack'''
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1

        f = self.freq[val]

        if f > self.max_freq:
            self.max_freq = f

        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)

    def pop(self) -> int:
        '''Pop and return the most frequent element'''
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val
