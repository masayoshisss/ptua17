# Create four functions that:

# Return the sum of all provided numbers (using the *args parameter in the function).

# Return the square root of a given number. If a string argument is passed to this function, an exception should be logged in the log file with a custom error message.

# Return the number of characters in a given sentence.

# Return the result of dividing number x by number y. If 0 is passed as the second argument, an exception should be logged in the log file with a custom error message.

# In the log entries, include the date, time, and logging level. Additionally, each function should log an INFO level message about what it performed, for example:


# logging.info(f"The sum of numbers {args} is: {sum(args)}")
# Test each function with chosen arguments.

# Hint: Use try/except/else/finally (not necessarily all), and logging.exception() for exception handling.

import logging
import math

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="math.log")

provided_numbers = (5, 5, 5, 4, 5)

def sum_of_numbers(*args:int) -> int:
    logging.info(f"Calculating the sum of numbers: {args}")
    return sum(args)
print(sum_of_numbers(*provided_numbers))

def square_root_of_number(number: int) -> float:
    logging.info(f"Calculating the square root of number: {number}")
    try:
        return math.sqrt(number)
    except Exception as e:
        logging.exception(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
print(square_root_of_number(25))

def number_of_characters(sentence: str) -> int:
    logging.info(f"Calculating the number of characters in the sentence: {sentence}")
    logging.info(f"The number of characters in the sentence is: {len(sentence)}")
    return len(sentence)
print(number_of_characters("Hello my name is Augustas"))

def divide_numbers(x: int, y: int) -> float:
    logging.info(f"Dividing number {x} by number {y}")
    try:
        return x / y
    except ZeroDivisionError as e:
        logging.exception(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
print(divide_numbers(10, 0))
