#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = sum(
        int(arguments) for arguments in sys.argv if arguments != sys.argv[0]
    )
    print(result)
