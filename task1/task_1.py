from array import *
import argparse

parser = argparse.ArgumentParser(description="первый аргумент n - длинна массива от 1 до n,"
                                             "второй аргумент m - длина шага")
parser.add_argument("n", type=int)
parser.add_argument("m", type=int)
args = parser.parse_args()

arr = array('i', range(1, args.n + 1)) * args.m

start = 0
lst = []
for _ in range(args.m+1):
    lst.append(arr[start:start + args.m])
    start += args.m - 1

print("".join([str(el[0]) for el in lst]))


