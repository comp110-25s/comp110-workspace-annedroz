"""Making My First Test Module!"""

__author__: str = "730518576"


# Unit Tests:
from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len

# Unit Tests for invert:


# Use Case
def test_invert_simple() -> None:
    """Test for simple inversion of dictionary."""
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}


# Use Case
def test_invert_single() -> None:
    """Test for inversion of single key-value pair."""
    assert invert({"tree": "door"}) == {"door": "tree"}


# Edge Case
def test_invert_empty() -> None:
    """Test for inversion of empty dictionary."""
    assert invert({}) == {}


# Unit Tests for count:


# Use Case
def test_count_multiple() -> None:
    """Test that counts values having multiple occurrences."""
    assert count(["burger", "fries", "fries", "soda", "burger", "burger"]) == {
        "burger": 3,
        "fries": 2,
        "soda": 1,
    }


# Use Case
def test_count_single() -> None:
    """Test that counts values each having a single occurrence."""
    assert count(["sun", "star", "moon"]) == {"sun": 1, "star": 1, "moon": 1}


# Edge Case
def test_count_empty() -> None:
    """Test that counts values in an empty list."""
    assert count([]) == {}


# Unit Tests for favorite_color:


# Use Case
def test_favorite_color_single() -> None:
    """Test for most popular color in dictionary with a single most popular color."""
    assert (
        favorite_color({"Anne": "pink", "Natalie": "pink", "Quinn": "purple"}) == "pink"
    )


# Use Case
def test_favorite_color_multiple() -> None:
    """Test for most popular color in dictionary with multiple most popular colors."""
    assert (
        favorite_color(
            {"Oliver": "blue", "Bob": "green", "Billy": "green", "Joe": "blue"}
        )
        == "blue"
    )


# Edge Case
def test_favorite_color_empty() -> None:
    """Test for most popular color in empty dictionary."""
    assert favorite_color({}) == ""


# Unit Tests for bin_len:


# Use Case
def test_bin_len_unique() -> None:
    """Test for bin_len with only unique strings."""
    assert bin_len(["the", "big", "whale"]) == {3: {"the", "big"}, 5: {"whale"}}


# Use Case
def test_bin_len_multiple() -> None:
    """Test for bin_len with multiple equivalent strings."""
    assert bin_len(["the", "big", "big"]) == {3: {"the", "big"}}


# Edge Case
def test_bin_len_empty() -> None:
    """Test for bin_len with empty list."""
    assert bin_len([]) == {}
