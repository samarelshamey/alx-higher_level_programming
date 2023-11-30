#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    res = 0
    for arg in range(1, argc):
        res += int(sys.argv[arg])
    print(res)
