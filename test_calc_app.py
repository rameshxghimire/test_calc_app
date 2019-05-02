"""
A python script to test the basic functionality of calculator app on mac osx.
The testing process is automatic after the script is run, no keyboard or mouse input from the user is needed.
"""


# import required modules and libraries
import sys
import os
import subprocess
import pyautogui as patg
from time import sleep as wait
import random


# Function to check if all the numbers are working (0 to 9)
def basic_operations():
    """
    Checks if
    - all the numbers are working (0 to 9)
    - the clear key is working.
    - the sum or equal key is working.
    :return: None
    """
    # first check if numbers 0 -9 work
    for numbers in range(10):
        try:
            patg.typewrite(str(numbers))
            print("Test Passed. | Number ", numbers, "working.")
        except Exception as e:
            print("test failed because: ", e)
    # check if the clear, sum and equal keys are working
    # corresponding key for clear, sum and equal on keyboard are: esc, + and return keys (or "=" key) respectively
    try:
        patg.typewrite("esc")
        patg.typewrite("esc")
        print("Test Passed. | clear key working.")
        patg.typewrite("+")
        print("Test Passed. | sum key working.")
        patg.typewrite("esc")
        patg.typewrite("=")
        print("Test Passed. | equal key working.")
    except Exception as e:
        print("test failed because: ", e)


def apps_functionality():
    """
    Checks
    - the addition of two integer numbers.
    - the subtraction of two negative numbers.
    - the multiplication of two integer numbers.
    - the division of two integer numbers.
    - the division of a number by zero.
    - the division of zero by any number.
    :return: None
    """
    # addition
    # clear the calculator screen
    patg.typewrite("esc")
    patg.typewrite("esc")
    try:
        # first random integer for addition
        patg.typewrite(str(random.randint(0, 9)))

        # sum
        patg.typewrite("+")

        # second random integer for addition
        patg.typewrite(str(random.randint(0, 9)))

        # equal
        patg.typewrite("=")
        print("Test Passed. | integer addition working.")

    except Exception as e:
        print("test failed because: ", e)

    # subtraction
    # clear the calculator screen
    patg.typewrite("esc")
    patg.typewrite("esc")
    try:
        # first random negative integer for subtraction
        patg.typewrite("-")
        patg.typewrite(str(random.randint(0, 9)))

        # subtract
        patg.typewrite("-")

        # second random negative integer for subtraction
        patg.typewrite("-")
        patg.typewrite(str(random.randint(0, 9)))

        # equal
        patg.typewrite("=")
        print("Test Passed. | negative integer subtraction working.")

    except Exception as e:
        print("test failed because: ", e)

    # multiplication
    # clear the calculator screen
    patg.typewrite("esc")
    patg.typewrite("esc")
    try:
        # first random integer for multiplication
        patg.typewrite(str(random.randint(0, 9)))

        # multiply
        patg.typewrite("*")

        # second random integer for multiplication
        patg.typewrite(str(random.randint(0, 9)))

        # equal
        patg.typewrite("=")
        print("Test Passed. | multiplication working.")

    except Exception as e:
        print("test failed because: ", e)

    # division
    # clear the calculator screen
    patg.typewrite("esc")
    patg.typewrite("esc")
    try:
        # first random integer for division
        patg.typewrite(str(random.randint(0, 9)))

        # devide
        patg.typewrite("/")

        # second random integer for division
        patg.typewrite(str(random.randint(0, 9)))

        # equal
        patg.typewrite("=")
        print("Test Passed. | division working.")

    except Exception as e:
        print("test failed because: ", e)

    # division by zero
    # clear the calculator screen
    patg.typewrite("esc")
    patg.typewrite("esc")
    try:
        # a random integer for division
        patg.typewrite(str(random.randint(0, 9)))

        # devide
        patg.typewrite("/")

        # zero
        patg.typewrite("0")

        # equal
        patg.typewrite("=")
        print("Test Passed. | division by zero working.")

    except Exception as e:
        print("test failed because: ", e)

    # division of zero by a number
    # clear the calculator screen
    patg.typewrite("esc")
    patg.typewrite("esc")
    try:
        # zero
        patg.typewrite("0")

        # devide
        patg.typewrite("/")

        # a random integer
        patg.typewrite(str(random.randint(0, 9)))
        wait(2)
        # equal
        patg.typewrite("=")
        print("Test Passed. | division of zero by an integer working.")

        # clear the screen
        patg.typewrite("esc")
        patg.typewrite("esc")

    except Exception as e:
        print("test failed because: ", e)


# wrap the basic_operation & apps_functionality functions in main function and call upon execution
def main():
    basic_operations()
    apps_functionality()


if __name__ == '__main__':
    # launch the calculator app from it's default location on OSX using subprocess module and unix command
    subprocess.call(
        ["/usr/bin/open", "-n", "-a", "/Applications/Calculator.app"]
    )

    # wait for 1 second
    wait(1.0)

    # run the main function if there is no interruption and system failure
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
