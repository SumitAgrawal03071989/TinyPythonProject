# Tiny Python Project

## How to write and test python programs.

* A Python program is plain text that lives in a file. You need the python3 program to interpret and execute the program file.
* You can make a program executable and copy it to a location in your $PATH so that you can run it like any other program on your computer. Be sure to set the shebang to use env to find the correct python3.
* The argparse module will help you document and parse all the parameters to your program. You can validate the types and numbers of arguments, which can be positional, optional, or flags. The usage will be automatically generated.
* We will use the pytest program to run the test.py programs for each exercise. The make test shortcut will execute pytest -xv test.py, or you can run this command directly.
* Code formatters like YAPF and Black will automatically format your code to community standards, making it easier to read and debug.
* You can use the new.py program to generate new Python programs that use argparse.

