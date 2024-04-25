import argparse
import csv

parser = argparse.ArgumentParser(description="первый аргумент - координаты центра окружности и ее радиус"
                                             "второй аргумент - координаты точек")

parser.add_argument("data_initial", type=str)
parser.add_argument("points", type=str)

args = parser.parse_args()

with open(args.data_initial) as data:
    lst = []
    for el in csv.reader(data):
        lst.extend(el)
    d = [int(el) for el in lst[0].split(" ")]

with open(args.points) as data:
    for el in csv.reader(data):
        p = [int(el) for el in el[0].split(" ")]
        if (p[0] - d[0]) ** 2 + (p[1] - d[1]) ** 2 < d[2] ** 2:
            print(1)
        elif (p[0] - d[0]) ** 2 + (p[1] - d[1]) ** 2 == d[2] ** 2:
            print(0)
        else:
            print(2)
