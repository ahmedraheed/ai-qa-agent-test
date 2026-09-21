import math

# Simple Calculator Application

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    # BUG: Addition is written instead of multiplication!
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)

def cube(x):
    return x ** 3

def cube_root(x):
    if x < 0:
        return -((-x) ** (1/3))
    return x ** (1/3)

if __name__ == '__main__':
    print('Add 5 + 3:', add(5, 3))
    print('Multiply 5 * 3:', multiply(5, 3))
    print('Sqrt 9:', sqrt(9))
    print('Cube 3:', cube(3))
    print('Cube Root 27:', cube_root(27))
