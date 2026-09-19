# Simple Calculator Application

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    return base ** exponent

def percentage(part, total):
    if total == 0:
        raise ValueError("Cannot calculate percentage with zero total")
    return (part / total) * 100

if __name__ == '__main__':
    print('Add 5 + 3:', add(5, 3))
    print('Subtract 5 - 3:', subtract(5, 3))
    print('Multiply 5 * 3:', multiply(5, 3))
    print('Divide 6 / 2:', divide(6, 2))
    print('Power 2 ^ 3:', power(2, 3))
    print('Percentage 20 of 50:', percentage(20, 50))
