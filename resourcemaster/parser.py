import numpy as np


def load_namelinks(_path):
    with open(_path, 'r', encoding='utf-8') as txt:
        name_links = txt.readlines()
        name_link = {i.split()[0]: i.split()[1] for i in name_links}

    return name_link


def random_choice(limits, nums=10):
    return list(set([int(np.random.rand()*limits) for i in range(nums)]))
