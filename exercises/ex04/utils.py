"""List utility functions."""

__author__ = "730396223"


# TODO: Implement your functions here.
def all(a: list[int], given: int) -> bool:

    i: int = 0
    while i < len(a):
        if a[i] != given:
            return False 
        i += 1

    return True


def is_equal(first: list[int], second: list[int]) -> bool:

    i: int = 0
    while i < len(first):
        if first[i] != second[i]:
            return False
        i += 1
    return True


def max(items: list[int]) -> int:
    place: int = 0
    i: int = 0
    while i < len(items):
        if items[i] > items[place]:
            place = i
        i += 1
    return items[place]


def main():
    test: list[int] = list()
    test.append(3)
    test.append(4)
    test.append(9)
    test.append(5)
    test.append(5)

    all(test, 5)


if __name__ == "__main__":
    main()
