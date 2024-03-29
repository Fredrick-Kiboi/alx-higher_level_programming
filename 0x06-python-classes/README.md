# 0x06. Python - Classes and Objects

## Background Context
- OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).

- As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

*Read or watch the below resources in the order presented.*

## Resources
**Read or Watch:**
- Object Oriented Programming (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet)
- Object-Oriented Programming (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The `__init__` Method, *"Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”*)
- Properties vs. Getters and Setters
- Learn to Program 9 : Object Oriented Programming
- Python Classes and Objects
- Object Oriented Programming

## Learning Objectives
** At the end of this project, you are expected to be able to explain to anyone, without the help of Google: **

### General
- Why Python programming is awesome
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the `__dict__` of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the getattr function

### More Info
- Documentation is now mandatory! Each module, class, and method must contain docstring as comments.
- Example Google Style Python Docstrings

## Tasks
0. **My first square**<br>
*mandatory*

- Write an empty class Square that defines a square:<br>
  - You are not allowed to import any module


1. **Square with size**<br>
*mandatory*

- Write a class Square that defines a square by: (based on 0-square.py)<br>
  - Private instance attribute: size<br>
  - Instantiation with size (no type/value verification)<br>
  - You are not allowed to import any module

  - Why size is private attribute?
  - The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute.<br> One way to have the control is to keep it privately.<br> You will see in next tasks how to get, update and validate the size value.

2. **Size validation** <br>
*mandatory*
- Write a class Square that defines a square by: (based on 1-square.py)<br>
  - Private instance attribute: size<br>
  - Instantiation with optional size: def __init__(self, size=0):<br>
  - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer<br>
  - if size is less than 0, raise a ValueError exception with the message size must be >= 0<br>
- You are not allowed to import any module

3. **Area of a square** <br>
*mandatory*
- Write a class Square that defines a square by: (based on 2-square.py)<br>
  - Private instance attribute: size<br>
  - Instantiation with optional size: def __init__(self, size=0):<br>
  - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer<br>
  - if size is less than 0, raise a ValueError exception with the message size must be >= 0<br>
- Public instance method: def area(self): that returns the current square area
- You are not allowed to import any module


4. **Access and update private attribute** <br>
*mandatory*
- Write a class Square that defines a square by: (based on 3-square.py)<br>
  - Private instance attribute: size<br>
    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:
    - size must be an integer, otherwise raise a    TypeError exception with the message size must be an integer<br>
    - if size is less than 0, raise a ValueError exception with the message size must be >= 0<br>
- Instantiation with optional size: def __init__(self, size=0):<br>
- You are not allowed to import any module
- Public instance method: def area(self): that returns the current square area

5. **Printing a square** <br>
*mandatory*
- Write a class Square that defines a square by: (based on 4-square.py)<br>
  - Private instance attribute: size<br>
    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:
    - size must be an integer, otherwise raise a    TypeError exception with the message size must be an integer<br>
    - if size is less than 0, raise a ValueError exception with the message size must be >= 0<br>
- Instantiation with optional size: def __init__(self, size=0):<br>
- Public instance method: def area(self): that returns the current square area
- Public instance method: def my_print(self): that prints in stdout the square with the character #:
  - if size is equal to 0, print an empty line
- You are not allowed to import any module

6. **Coordinates of a square** <br>
*mandatory*
- Write a class Square that defines a square by: (based on 5-square.py)<br>
  - Private instance attribute: size<br>
    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:
    - size must be an integer, otherwise raise a    TypeError exception with the message size must be an integer<br>
    - if size is less than 0, raise a ValueError exception with the message size must be >= 0<br>
- Private instance attribute: position:
  - property def position(self): to retrieve it
  - property setter def position(self, value): to set it:
     - position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
- Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
- Public instance method: def area(self): that returns the current square area
- Public instance method: def my_print(self): that prints in stdout the square with the character #:
  - if size is equal to 0, print an empty line
  - position should be use by using space - Don’t fill lines by spaces when position[1] > 0
- You are not allowed to import any module

7.  **Singly linked list** <br>
*#advanced*
- Write a class Node that defines a node of a singly linked list by:
  - Private instance attribute: data:
  - property def data(self): to retrieve it
  - property setter def data(self, value): to set it:
  - data must be an integer, otherwise raise a TypeError exception with the message data must be an integer

- Private instance attribute: next_node:
  - property def next_node(self): to retrieve it
  - property setter def next_node(self, value): to set it:
  - next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object

- Instantiation with data and next_node: def __init__(self, data, next_node=None):

- And, write a class SinglyLinkedList that defines a singly linked list by:
  - Private instance attribute: head (no setter or getter)
  - Simple instantiation: def __init__(self):
  - Should be printable:
    - print the entire list in stdout
    - one node number by line
  - Public instance method: def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list (increasing order)
  - You are not allowed to import any module

8. **Print Square instance** <br>
#advanced
- Write a class Square that defines a square by: (based on 6-square.py)<br>
  - Private instance attribute: size<br>
    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:
    - size must be an integer, otherwise raise a    TypeError exception with the message `size must be an integer`<br>
    - if size is less than 0, raise a ValueError exception with the `message size must be >= 0`<br>
- Private instance attribute: position:
  - property def position(self): to retrieve it
  - property setter def position(self, value): to set it:
     - position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
- Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
- Public instance method: def area(self): that returns the current square area
- Public instance method: def my_print(self): that prints in stdout the square with the character #:
  - if size is equal to 0, print an empty line
  - position should be use by using space
- Printing a Square instance should have the same behavior as my_print()
- You are not allowed to import any module
