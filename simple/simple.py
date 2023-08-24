import random


def simple_list():
    list_of_dicts = []
    for i in range(10):
        aux_dict = {"id": i, "age": random.randint(1, 130)}
        list_of_dicts.append(aux_dict)
    return list_of_dicts


def sort_list(dicts):
    return sorted(dicts, key=lambda x: x["age"])
