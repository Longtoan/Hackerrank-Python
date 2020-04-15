#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result = ""
    for i in range(len(s)):
        if(i == 0 or s[i-1]==' '):
            if("a" <= s[i] <= "z"):
                result += chr(ord(s[i])-32)
            else:
                result += s[i]
        else:
            if("A" <= s[i] <= "Z"):
                result += chr(ord(s[i])+32)
            else:
                result += s[i]
    return result
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
