"""Making My First Definitions Module!"""

__author__: str = "730518576"


# Part 1: invert
def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts Keys and Values of Dictionary."""
    invert_dict = {}  # Initialize empty dictionary.
    # Will be the dictionary with the keys and values inverted.

    # Loops through key and value pairs
    #   of initial dictionary (input_dict) using .items().
    for key, value in input_dict.items():
        if value in invert_dict:  # Checks if the current value is in
            raise KeyError(f"Duplicate value found: {value}")
            # If encounter more than one of same key, raises KeyError.
        else:
            invert_dict[value] = key
            # Otherwise switch current key with value and vise versa.
    return invert_dict  # Returns inverted dictionary.


# Part 2: count
def count(values: list[str]) -> dict[str, int]:
    # dict[str, int] -> example) "blue": 3
    """Counts number of times value occurs in list."""
    counts = {}  # Initialize empty dictionary.

    # Loops through list (values) to count occurences of each value.
    for value in values:
        if value in counts:  # Check if current string (value) is a key in counts.
            counts[value] += 1  # If so, will increase value's count by 1 in counts.
        else:
            counts[value] = 1
            # Otherwise, the current string will remain with its count of 1.
    return counts  # Returns completed dictionary with values and corresponding counts.


# Part 3: favorite_color
def favorite_color(color_dict: dict[str, str]) -> str:
    # color_dict -> Dictionary of names with corresponding colors (both str).
    """Determines the most popular color in dictionary."""
    color_count = count(list(color_dict.values()))
    # color_dict.values() -> extracts values from color_dict.
    # list() -> makes color_dict values into list.
    # count() -> utilize count() from previous part, where keys are colors,
    #   and values are the number of times colors appear.

    max_count = 0  # Will keep track of color with most appearances.
    most_popular_color = ""  # Will equal the most frequently appearing color.

    # Loops through each color (values) listed in color_dict.
    for color in color_dict.values():
        if color_count[color] > max_count:
            # If the current color has a higher frequency than max_count.
            # Ensures if multiple colors with same highest frequencies exist,
            #   first colors that appeared will return.
            max_count = color_count[color]  # If so, make current color equal max_count.
            most_popular_color = color
            # Therefore, implement the current value as the most popular one.

    return most_popular_color  # After loop is complete, refer to most


# Part 4: bin_len
def bin_len(bin_dict: list[str]) -> dict[int, set[str]]:
    """Bins list of strings into dictionary based on lengths."""
    bin_lengths = {}  # Initialize empty dictionary.

    # Loops through each string in dictionary (bin_dict)
    for string in bin_dict:
        length = len(string)  # Initialize variable that's the length of current string.
        # (used as key in returned dictionary).
        if length in bin_lengths:
            # If current length exists in returned dictionary (bin_dict).
            bin_lengths[length].add(string)
            # If so, add current string to the existing set if key exists.
        else:
            bin_lengths[length] = {string}
            # Otherwise, create new set with current value.

    return bin_lengths  # Return dictionary
