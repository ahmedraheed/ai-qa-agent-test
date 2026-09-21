import math

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

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)

def power(base, exponent):
    """Calculate base raised to the power of exponent ($base^{exponent}$)."""
    # Input validation / edge cases if any
    # 0^0 is typically 1 in Python math.pow / exponentiation, or raise ValueError if needed, but math.pow(0, 0) is 1.0.
    # Let's check edge cases like negative base with fractional exponents if needed, but math.pow or ** handles standard math.
    try:
        return math.pow(base, exponent)
    except ValueError:
        raise ValueError("Invalid operation for power calculation")

def percentage(part, whole):
    """Calculate what percentage part is of whole (i.e., (part / whole) * 100)."""
    if whole == 0:
        raise ValueError("Cannot calculate percentage with zero whole")
    return (part / whole) * 100

if __name__ == '__main__':
    print('Add 5 + 3:', add(5, 3))
    print('Multiply 5 * 3:', multiply(5, 3))
    print('Sqrt 9:', sqrt(9))
    print('Power 2^3:', power(2, 3))
    print('Percentage 50 of 200:', percentage(50, 200))
