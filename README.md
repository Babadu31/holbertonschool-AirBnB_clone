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
