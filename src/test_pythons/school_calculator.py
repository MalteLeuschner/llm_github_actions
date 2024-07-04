from typing import Union
from typing import Union


def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    """Multiply two numbers.

    This function takes two numbers as input and returns their product.

    Args:
      x (float): The first number.
      y (float): The second number.

    Returns:
      float: The product of x and y."""
    return x * y


def divide(x: float, y: float) -> Union[float, str]:
    """Divides two numbers.

    Returns the result of the division if the second number is not zero,
    otherwise returns an error message.

    Args:
      x (float): The first number.
      y (float): The second number.

    Returns:
      Union[float, str]: The result of the division or an error message.

    Raises:
      ValueError: If the input values are not numeric."""
    if y == 0:
        return "Error! Division by zero."
    return x / y


def school_calculator() -> None:
    """School calculator function.

    This function provides a simple calculator interface to perform basic arithmetic operations.

    Args:
      None

    Returns:
      None

    Raises:
      ValueError: If the input values are not numeric."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            if choice == "1":
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            next_calculation = input(
                "Do you want to perform another calculation? (yes/no): "
            )
            if next_calculation.lower() != "yes":
                break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    calculator()
