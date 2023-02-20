#!/usr/bin/python3
""" compute value from stdin"""

file_size = 0
status_code = {"200": 0, "301": 0, "400": 0,
               "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}


def status(code):
    """check for the status code"""
    if (code in status_code.keys()):
        status_code[code] += 1


def result(status_code, file_size):
    """print the result """
    print("File size: {}".format(file_size))
    for key, value in status_code.items():
        if (value != 0):
            print("{}: {}".format(key, value))


def main():
    """the main  code"""
    count = 0
    file_size = 0
    while (True):
        try:
            line = input()
            lis = line.split()
            if (len(lis) != 9):
                continue

            count += 1
            status(lis[7])
            file_size += int(lis[8])
            if (count % 10 == 0):
                result(status_code, file_size)
        except (KeyboardInterrupt, EOFError):
            result(status_code, file_size)


if __name__ == "__main__":
    main()
