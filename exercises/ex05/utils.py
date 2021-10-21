"""List utility functions part 2."""

__author__ = "730396223"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    new: list[int] = list()
    for item in xs:
        if item % 2 == 0:
            new.append(item)
    return new


def sub(xs: list[int], a: int, b: int) -> list[int]:
    new: list[int] = list()
    i: int = a
    if a <= 0 or a > 0:
        while i < b:
            new.append(xs[i])
            i += 1
    return new


def concat(xs: list[int], ys: list[int]) -> list[int]:
    new: list[int] = list()
    i: int = 0
    j: int = 0
    while i < len(xs) + len(ys):
        if i < len(xs):
            new.append(xs[i])
        if i >= len(xs):
            new.append(ys[j])
            j += 1
        i += 1
    return new
