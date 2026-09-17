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
        return 'Error: Division by zero is not allowed'
    return a / b

if __name__ == '__main__':
    print('Add 5 + 3:', add(5, 3))
    print('Multiply 5 * 3:', multiply(5, 3))
