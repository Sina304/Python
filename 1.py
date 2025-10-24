class complex_number:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex_number(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return complex_number(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"
    
# Example usage:
c1 = complex_number(2, 3)
c2 = complex_number(4, 5)
c3 = c1 + c2
c4 = c1 - c2
print(c3)  # Output: 6 + 8i
print(c4)  # Output: -2 + -2i