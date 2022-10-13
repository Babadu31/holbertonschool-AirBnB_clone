# holbertonschool-AirBnB_clone

## description of the project

create a console program to emulate a native console that will interpret commands and interact with AirBnB site clone classes and methods

## Learning Objectives

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## description of the command interpreter:

allows the user to interact with the classes and methods of the AirBnB cloned site using commands in the form of lines of text.

## how to start it

clone the repository. run the file console.py and this will initiate the interactive mode.

## how to use it

- quit : exit the console
- EOF : exit program on EOF signal
- help : displays information about the associated command
- empty line + ENTER : execute anything
- create : Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
- show : Prints the string representation of an instance based on the class name and id
- destroy : Deletes an instance based on the class name and id (save the change into the JSON file)
- all : Prints all string representation of all instances based or not on the class name
- update : Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)

## examples


## learning bonus

### What is an UUID

UUID, Universal Unique Identifier, is a python library which helps in generating random objects of 128 bits as ids. It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.).

Advantages of UUID :
- Can be used as general utility to generate unique random id.
- Can be used in cryptography and hashing applications.
- Useful in generating random documents, addresses etc.

### How to manage datetime
https://www.programiz.com/python-programming/datetime

### What is *args and **kwargs and how to use it

*args :

**kwargs

## sources

- UUID
https://www.geeksforgeeks.org/generating-random-ids-using-uuid-python/
https://docs.python.org/3/library/uuid.html

- *args and **kwargs
https://www.freecodecamp.org/news/args-and-kwargs-in-python/
