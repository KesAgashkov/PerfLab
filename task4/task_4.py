import argparse
import csv

parser = argparse.ArgumentParser(description="путь к файлу с данными")
parser.add_argument("data", type=str)
args = parser.parse_args()

with open(args.data, encoding="utf-8") as file:
    nums = []
    for el in csv.reader(file):
        nums.extend(el)
    nums = [int(el) for el in nums]

# из задания непонятно к какому числу нужно осуществлять приведение.
# буду использовать среднее арифметическое всех элементов с округлением в меньшую сторону

aver = int(sum(nums) / len(nums))
step = 0
for el in nums:
    step += abs(el - aver)

print(step)
