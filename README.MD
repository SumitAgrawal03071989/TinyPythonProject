# Tiny Python Project

## How to write and test python programs.

* A Python program is plain text that lives in a file. You need the python3 program to interpret and execute the program file.
* You can make a program executable and copy it to a location in your $PATH so that you can run it like any other program on your computer. Be sure to set the shebang to use env to find the correct python3.
* The argparse module will help you document and parse all the parameters to your program. You can validate the types and numbers of arguments, which can be positional, optional, or flags. The usage will be automatically generated.
* We will use the pytest program to run the test.py programs for each exercise. The make test shortcut will execute pytest -xv test.py, or you can run this command directly.
* Code formatters like YAPF and Black will automatically format your code to community standards, making it easier to read and debug.
* You can use the new.py program to generate new Python programs that use argparse.

## Chapter 02: working with strings
* All Python’s documentation is available at https://docs.python.org/3/ and via the help command in the REPL.
* Variables in Python are dynamically typed according to whatever value you assign them, and they come into existence when you assign a value to them.
* Strings have methods like str.upper() and str.isupper() that you can call to alter them or get information.
* You can get parts of a string by using square brackets and indexes like [0] for the first letter or [-1] for the last.
* You can concatenate strings with the + operator.
* The str.format() method allows you to create a template with {} placeholders that get filled in with arguments.
* F-strings like f'{article} {word}' allow variables and code to go directly inside the brackets.
* The x in y expression will report whether the value x is present in the collection y.
* Statements like if/else do not return a value, whereas expressions like x if y else z do return a value.
* Test-driven development is a way to ensure programs meet some minimum criteria of correctness. Every feature of a program should have tests, and writing and running test suites should be an integral part of writing programs.

# chapter 03:  Working with lists
* Python lists are ordered sequences of other Python data types, such as strings and numbers.
* There are methods like list.append() and list.extend() to add elements to a list. Use list.pop() and list.remove() to remove elements.
* You can use x in y to ask if element x is in the list y. You can also use list.index() to find the index of an element, but this will cause an exception if the element is not present.
* Lists can be sorted and reversed, and elements within lists can be modified. Lists are useful when the order of the elements is important.
* Strings and lists share many features, such as using len() to find their lengths, using zero-based indexing where 0 is the first element and -1 is the last, and using slices to extract smaller pieces from the whole.
* The str.join() method can be used to make a new str from a list.
* if/elif/else can be used to branch code depending on conditions.

# Chapter 04: Working with dictionaries
* You can create a new dictionary using the dict() function or with empty curly brackets ({}).
* Dictionary values are retrieved using their keys inside square brackets or by using the dict.get() method.
* For a dict called x, you can use 'key' in x to determine if a key exists.
* You can use a for loop to iterate through the characters of a str just like you can iterate through the elements of a list. You can think of strings as lists of characters.
* The print() function takes optional keyword arguments like end='', which you can use to print a value to the screen without a newline.


