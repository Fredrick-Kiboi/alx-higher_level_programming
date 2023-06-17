#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1

    if length == 0:
        print(f"{length} arguments.")
    elif length == 1:
        print(f"{length} argument:")
    else:
        print(f"{length} arguments:")

    if length >= 1:
        for length, arguments in enumerate(sys.argv):
            if length != 0:
                print(f"{length}: {arguments}")
