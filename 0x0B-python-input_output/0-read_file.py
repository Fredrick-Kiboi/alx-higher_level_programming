#!/usr/bin/python3

'''
read_file - function that reads a text file(UTF8) and prints to stdout

Args:
@filename : the file to read form

Return: Nothing
'''

def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as myfile:
        print(myfile.read())
