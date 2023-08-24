import random


def simple_list():
    return [{"id": i, "age": random.randint(1, 6)} for i in range(10)]


def sort_list(dicts):
    aux = sorted(dicts, key=lambda x: x["age"])
    return aux
