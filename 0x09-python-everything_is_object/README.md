# 0x09. Python - Everything is object

## Resources
**Read or watch:**
- 9.10. Objects and values
- 9.11. Aliasing
- Immutable vs mutable types
- Mutation (Only this chapter)
- 9.12. Cloning lists
- Python tuples: immutable but potentially changing

## Learning Objectives
*At the end of this project, you are expected to be able to explain to anyone, without the help of Google:*
### General
- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions


#### Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

#### Requirements
- Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a newline character
- The first line of all your script files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- .txt Answer Files
- Only one line
- No Shebang
- All your files should end with a new line

## Tasks
0. **Who am I?**
*mandatory*
- What function would you use to get the type of an object?
  - Write the name of the function in the file, without ().

1. **Where are you?**
*mandatory*
- How do you get the variable identifier (which is the memory address in the CPython implementation)?
  - Write the name of the function in the file, without ().

2. **Right count**
*mandatory*
- In the following code, do a and b point to the same object? Answer with Yes or No.
```Python
>>> a = 89
>>> b = 100
```

3. **Right count =**
*mandatory*
- In the following code, do a and b point to the same object? Answer with Yes or No.
```Python
>>> a = 89
>>> b = 89
```

4. **Right count =**
*mandatory*
- In the following code, do a and b point to the same object? Answer with Yes or No.
```Python
>>> a = 89
>>> b = a
```

    
5. **Right count =+**
*mandatory*
- In the following code, do a and b point to the same object? Answer with Yes or No.
```Python
>>> a = 89
>>> b = a + 1
```

6. **Is equal**
*mandatory*
- What do these 3 lines print?
```Python
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

7. **Is the same**
*mandatory*
- What do these 3 lines print?
```Python
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

8. **Is really equal**
*mandatory*
- What do these 3 lines print?
```Python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

9. **Is really the same**
*mandatory*
- What do these 3 lines print?
```Python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

10. **And with a list, is it equal**
*mandatory*
- What do these 3 lines print?
```Python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

11. And with a list, is it the same
mandatory
Score: 0.0% (Checks completed: 0.0%)
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)