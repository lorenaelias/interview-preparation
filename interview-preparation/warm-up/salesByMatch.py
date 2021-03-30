#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0

    for s in range(n):
        if ar[s] in pairs:
            pairs[ar[s]] += 1
        else:
            pairs[ar[s]] = 1
            
    return int(sum(y//2 for y in pairs.values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

