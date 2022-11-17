import random


def random_first_name():
    with open(r"data_name/first_name.txt", encoding='utf-8') as f:
        lines = f.readlines()
        first_name = random.choice(lines).replace("\n", "")
        print(first_name)
        f.close()
        return first_name


def random_last_name():
    with open(r"data_name/last_name.txt", encoding='utf-8') as f:
        lines = f.readlines()
        last_name = random.choice(lines).replace("\n", "")
        print(last_name)
        f.close()
        return last_name


