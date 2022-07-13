from .. import io


def add(a, b):
    return a + b


def add5(a):
    return add(a, 5)


def mult(a, b):
    return a * b


def div(a, b):
    if b == 0:
        io.console.boxed("ERROR: denominator cannot be 0")
        raise ValueError("b = 0")

    return a / b
