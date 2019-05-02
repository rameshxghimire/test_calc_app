_A Python script to test a GUI app_

the main script file name is test_calc_app.py

This is a script to test the functionality of the calculator app on mac osx.
The testing process is automatic after the script is run, no keyboard or mouse input from the user is needed.

This script, upon run, launches the calculator app and tests it's functionality by 
pressing numbers, operation symbols and performing various operations such as addition, subtraction and multiplication.
Python's subprocess module is used along with Unix style òpen`command to launch the app.

The script uses external library PyAutoGui to automate the pressing of buttons.

This script is produced in a virtual environment using pipenv with Python 3.6.
