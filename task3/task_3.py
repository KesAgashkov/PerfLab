import argparse
import json

parser = argparse.ArgumentParser(description="первый аргумент - результаты прохождения тестов"
                                             "второй аргумент - структура для построения отчетов на основе прошедших тестов"
                                             "третий аргумент - результат")

parser.add_argument("test_res", type=str)
parser.add_argument("structure", type=str)
parser.add_argument("result", type=str)

args = parser.parse_args()

with open(args.test_res, encoding="utf-8") as file, open(args.structure, encoding="utf-8") as val:
    data_tests = json.load(file)
    data_value = json.load(val)


def set_value(nested_dicts, key, iden, value):
    for k in nested_dicts:
        if k == key and nested_dicts["id"] == iden:
            nested_dicts[k] = value
        elif type(nested_dicts[k]) == dict:
            set_value(nested_dicts[k], key, iden, value)
        elif k == "values" or k == "tests":
            for el in nested_dicts[k]:
                if type(el) == dict:
                    set_value(el, key, iden, value)
                elif k == key and nested_dicts["id"] == iden:
                    nested_dicts[k][el] = value


for el in data_value["values"]:
    set_value(data_tests, "value", el["id"], el["value"])

with open(args.result, "w", encoding="utf-8") as record:
    json.dump(data_tests, record, indent=3)


# python task_3.py tests.json values.json report.json
