import random


def get_random_color(color_list):
    # get a random color from the list
    color_id = random.randint(0, len(color_list) - 1)
    color_rand = color_list[color_id]
    return color_rand


def get_random_size():
    # only allow lego blocks as big as 4x4
    x = 4
    y = 4
    while (x>=3 and y>=3):
        x = random.randint(1, 4)
        y = random.randint(1, 4)
    return x, y


def print_matrix(m):
    for item in m:
        print(item)