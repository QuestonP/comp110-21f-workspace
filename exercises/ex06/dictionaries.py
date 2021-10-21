"""Practice with dictionaries."""

__author__ = "730396223"


def invert(xs: dict[str, str]) -> dict[str, str]:
    hold: str = ""
    ys: dict[str, str] = {}
    for keys in xs:
        hold = xs[keys]
        ys[hold] = keys 
    return ys
# Define your functions below


def favorite_color(ds: dict[str, str]) -> str:
    fav: str = ""
    second_fav: str = ""
    fav_count: int = 0
    count2: int = 0
    for keys in ds:
        count2 = 0
        second_fav = ds[keys]
        for key in ds:
            if ds[key] == second_fav:
                count2 += 1
            if fav_count < count2:
                fav = ds[keys]
                fav_count = count2

    return fav


def count(xs: list[str]) -> dict[str, int]:
    """Counts how many times a value appears in a list and gives it a unique key in a dictionary with the amount of times it appears."""
    values: dict[str, int] = dict()
    i: int = 0
    while i < len(xs):
        if xs[i] in values:
            values[str(xs[i])] += 1
        else:
            values[str(xs[i])] = 1
        i += 1
    return values 
