def double(number: int) -> None:
    """: Returns the double of the input number.
    :
    : This function takes a number as input and returns its double.
    :
    : Args:
    :   number (int): The number to be doubled.
    :
    : Returns:
    :   int
    :
    : Raises:
    :   TypeError: If the input is not a number."""
    return number * 2


if __name__ == "__main__":
    new = double(5)
    print(new)
