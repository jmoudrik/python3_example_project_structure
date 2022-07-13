from .count import mult, add


def reduce(iterable, initial, op):
    total = initial
    for item in iterable:
        total = op(total, item)
    return total


def reduce_add(iterable):
    return reduce(iterable, 0, add)


def reduce_mult(iterable):
    return reduce(iterable, 1, mult)
