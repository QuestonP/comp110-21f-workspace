"""Utility functions."""

from csv import DictReader
__author__ = "123456789"

# Define your functions below
"""Some helpful utility functions for CSV Files."""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'"""
    result: list[dict[str, str]] = []
    # read file
    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)

    # close file 
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column"""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform row oriented table to column oriented one."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(ds: dict[str, list[str]], p: int) -> dict[str, list[str]]:
    """Create a new column based table only containing the first X rows of data for each column."""
    result: dict[str, list[str]] = {}
    for keys in ds:
        xs: list[str] = []
        i: int = 0
        while i < p:
            xs.append(ds[keys][i])
            i += 1
        result[keys] = xs
    return result


def select(ds: dict[str, list[str]], xs: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    i: int = 0
    for keys in xs:
        if i < len(xs):
            result[keys] = ds[xs[i]]
        i += 1
    return result


def concat(xs: dict[str, list[str]], ds: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for keys in xs:
        result[keys] = xs[keys]
    for keys in ds:
        if keys not in result:
            result[keys] = ds[keys]
        else:
            i: int = 0
            while i < len(ds):
                result[keys].append(ds[keys][i])
                i += 1
    return result


def count(xs: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}

    for names in xs:
        if names not in result:
            result[names] = 1
        else:
            result[names] += 1

    return result
