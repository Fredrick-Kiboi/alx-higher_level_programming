#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for arguments in sys.argv:
        if arguments != sys.argv[0]:
            result += int(arguments)
    print(result)
