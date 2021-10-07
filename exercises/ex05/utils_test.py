"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730396223"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_no_evens() -> None:
    """Test function when there are no evens."""
    xs: list[int] = [1, 3, 5, 7]
    assert only_evens(xs) == []


def test_only_evens_multiple_evens() -> None:
    """Test function when there are multiple evens (normal use case)."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


def test_only_evens_only_evens() -> None:
    """Test function when there are only evens."""
    xs: list[int] = [12, 22, 24, 64, 2]
    assert only_evens(xs) == [12, 22, 24, 64, 2]


def test_sub_one_item() -> None:
    """Test function when there is only one item."""
    xs: list[int] = [1]
    assert sub(xs, 0, 1) == [1]


def test_sub_normal() -> None:
    """Test function with normal use."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(xs, 1, 4) == [2, 3, 4]


def test_sub_empty() -> None:
    """Test an empty list."""
    xs: list[int] = []
    assert sub(xs, 0, 0) == []


def test_concat_one_list() -> None:
    """Test when there is only one list."""
    xs: list[int] = [1, 2, 4, 5]
    ys: list[int] = []
    assert concat(xs, ys) == [1, 2, 4, 5]


def test_concat_normal_use() -> None:
    """Test function in normal use."""
    xs: list[int] = [1, 2, 4, 5]
    ys: list[int] = [3, 4, 5, 6]
    assert concat(xs, ys) == [1, 2, 4, 5, 3, 4, 5, 6]


def test_concat_small_list() -> None:
    """Test function with one smaller list."""
    xs: list[int] = [1, 2]
    ys: list[int] = [4, 5, 6, 7, 8, 9]
    assert concat(xs, ys) == [1, 2, 4, 5, 6, 7, 8, 9]
