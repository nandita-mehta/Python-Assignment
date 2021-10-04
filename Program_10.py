class ReverseIter:
    def __init__(self, x):
        self.x = x
        self.index = len(x)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.x[self.index]


list = [3, 7, 1, 6, 8]
n = ReverseIter(list)
for i in n:
    print(i, end=" ")
