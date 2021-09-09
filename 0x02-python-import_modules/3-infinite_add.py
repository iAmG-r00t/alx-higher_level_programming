#!/usr/bin/python3
if __name__ == "__main__":
    """ Add all arguments."""
    import sys

    result = 0

    if (len(sys.argv) > 1):
        for i in range(len(sys.argv) - 1):
            result += (int(sys.argv[i + 1]))

        print("{:d}".format(result))
