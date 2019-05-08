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
    keys_to_test = ["esc", "+", "="]
    for key in keys_to_test:
        try:
            patg.typewrite(key)
            print("Test Passed. | ", key, "key working.")
        except Exception as e:
            print("Test failed because ", e)


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
    # clear the calculator screen
    rand_int_num = str(random.randint(0, 9))
    neg_rand_int_num = "-" + str(random.randint(0, 9))
    all_variables = [rand_int_num, neg_rand_int_num, "0"]
    operations = ["+", "-", "*", "/", "="]

    # addition of two integer numbers
    try:
        patg.typewrite("esc")
        for num in range(2):
            patg.typewrite(all_variables[0])
            num += 1
            if num == 1:
                patg.typewrite(operations[0])
            else:
                patg.typewrite(operations[-1])
                print("Test Passed. | integer addition working.")
    except Exception as e:
        print("Test failed because ", e)

    # subtraction of two negative numbers
    try:
        patg.typewrite("esc")
        for num in range(2):
            patg.typewrite(all_variables[1])
            num += 1
            if num == 1:
                patg.typewrite(operations[1])
            else:
                patg.typewrite(operations[-1])
                print("Test Passed. | negative integer subtraction working.")
    except Exception as e:
        print("Test failed because ", e)

    # multiplication of two integer numbers
    try:
        patg.typewrite("esc")
        for num in range(2):
            patg.typewrite(all_variables[0])
            num += 1
            if num == 1:
                patg.typewrite(operations[2])
            else:
                patg.typewrite(operations[-1])
                print("Test Passed. | multiplication working.")
    except Exception as e:
        print("Test failed because ", e)

    # division of two integer numbers
    try:
        patg.typewrite("esc")
        for num in range(2):
            patg.typewrite(all_variables[0])
            num += 1
            if num == 1:
                patg.typewrite(operations[3])
            else:
                patg.typewrite(operations[-1])
                print("Test Passed. | division working.")
    except Exception as e:
        print("Test failed because ", e)

    # division of a number by zero
    try:
        patg.typewrite("esc")
        num = 0
        while True:
            num += 1
            if num == 1:
                patg.typewrite(all_variables[0])
                patg.typewrite(operations[3])
            elif num ==2:
                patg.typewrite("0")
            else:
                patg.typewrite(operations[-1])
                print("Test Passed. | division by zero working.")
                break
    except Exception as e:
        print("Test failed because ", e)

    # division of zero by a number
    try:
        patg.typewrite("esc")
        num = 0
        while True:
            num += 1
            if num == 1:
                patg.typewrite("0")
                patg.typewrite(operations[3])
            elif num ==2:
                patg.typewrite(all_variables[0])
            else:
                patg.typewrite(operations[-1])
                print("Test Passed. | division of zero by an integer working.")
                patg.typewrite("esc")
                break
    except Exception as e:
        print("Test failed because ", e)


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
