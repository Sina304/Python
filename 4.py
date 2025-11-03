class Fibonacci:
    def __init__(self,steps):
        self.steps=steps
        self.index = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= self.steps:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.index += 1
        return value

example = Fibonacci(25)
for num in example:
    print(num, end=" ")