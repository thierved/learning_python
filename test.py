def product(x):
    def add(y):
        return x * y
    
    return add

multiply_by = product(3)
quadriples = product(4)

print(multiply_by(3))
print(multiply_by(4))
print(multiply_by(10))
print()
print(quadriples(2))
print(quadriples(4))
print(quadriples(10))