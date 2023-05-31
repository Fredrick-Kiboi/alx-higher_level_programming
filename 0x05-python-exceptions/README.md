# 0x05. Python - Exceptions

## Resources
**Read or watch:**
- Errors and Exceptions
- Learn to Program 11 Static & Exception Handling (starting at minute 7)

## Learning Objectives
*At the end of this project, you are expected to be able to explain to anyone, without the help of Google:*

### General
- Why Python programming is awesome
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

### Tasks
0. **Safe list printing**<br>
*mandatory*
- Write a function that prints x elements of a list.

  - Prototype: def safe_print_list(my_list=[], x=0):<br>
  - my_list can contain any type (integer, string, etc.)<br>
  - All elements must be printed on the same line followed by a new line.<br>
  - x represents the number of elements to print<br>
  - x can be bigger than the length of my_list<br>
  - Returns the real number of elements printed<br>
  - You have to use try: / except:<br>
  - You are not allowed to import any module<br>
  - You are not allowed to use len()