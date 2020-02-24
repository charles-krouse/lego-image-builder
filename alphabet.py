from html_text import return_square, return_circle
from functions import get_random_color


def fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color_list, x_current, x_add, y_current):

    text = ''

    # iterate through each row
    for xxx, x_val in enumerate(letter_matrix[0]):

        # iterate through each column
        for yyy, y_val in enumerate(letter_matrix):

            # get a random color
            color = get_random_color(color_list)

            if letter_matrix[yyy][xxx] == 0:
                page[y_current+yyy][x_current+xxx] = 0
            if letter_matrix[yyy][xxx] == 'n':
                page[y_current+yyy][x_current+xxx] = color
            if letter_matrix[yyy][xxx] == 1:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 1,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if letter_matrix[yyy][xxx] == 2:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 2,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if letter_matrix[yyy][xxx] == 3:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 3,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if letter_matrix[yyy][xxx] == 4:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 4,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if letter_matrix[yyy][xxx] == 5:
                page[y_current + yyy][x_current + xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 1,
                                                                  x_current, y_current, xxx - 1, yyy - 1)
                text += text_tmp
            if letter_matrix[yyy][xxx] == 6:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 2,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if letter_matrix[yyy][xxx] == 7:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 3,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if letter_matrix[yyy][xxx] == 8:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 4,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if letter_matrix[yyy][xxx] == 9:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 3, 1,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if letter_matrix[yyy][xxx] == 10:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 3, 2,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if letter_matrix[yyy][xxx] == 11:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 4, 1,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if letter_matrix[yyy][xxx] == 12:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 4, 2,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp

    x_current += x_add
    return text, x_current, y_current, rect_id, circle_id

def return_A(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 5, n, 0, 0],
                     [0, 11, n, n, n, 0],
                     [8, n, 0, 0, 8, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 5, n, n, n],
                     [n, n, 0, 0, n, n],
                     [5, n, 0, 0, 5, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_B(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 9, n, n, 0],
                     [n, n, 0, 0, 6, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 9, n, n, 0],
                     [7, n, 0, 0, 6, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 9, n, n, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_C(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 9, n, n, 0],
                     [0, 11, n, n, n, 2],
                     [7, n, 0, 0, 0, n],
                     [n, n, 0, 0, 0, 0],
                     [n, n, 0, 0, 0, 2],
                     [0, 11, n, n, n, n],
                     [0, 0, 9, n, n, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_D(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[11, n, n, n, 0, 0],
                     [7, n, 9, n, n, 0],
                     [n, n, 0, 0, 7, n],
                     [n, n, 0, 0, n, n],
                     [6, n, 0, 0, n, n],
                     [n, n, 9, n, n, 0],
                     [11, n, n, n, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_E(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 10, n, n],
                     [n, n, n, n, n],
                     [n, n, 0, 0, 0],
                     [n, n, 5, n, 0],
                     [7, n, 0, 0, 0],
                     [n, n, 10, n, n],
                     [n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_F(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[10, n, n, 6, n],
                     [n, n, n, n, n],
                     [5, n, 0, 0, 0],
                     [12, n, n, n, 0],
                     [n, n, n, n, 0],
                     [6, n, 0, 0, 0],
                     [n, n, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_G(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 9, n, n, 0, 0],
                     [0, 9, n, n, 5, n, 0],
                     [7, n, 0, 0, 0, 0, 0],
                     [n, n, 0, 0, 1, 3, 2],
                     [n, n, 0, 0, 0, n, n],
                     [0, 11, n, n, n, n, 0],
                     [0, 0, 9, n, n, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_H(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 0, 0, 7, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 6, n, 8, n],
                     [7, n, n, n, n, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 0, 0, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_I(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[10, n, n, 10, n, n],
                     [n, n, n, n, n, n],
                     [0, 0, 7, n, 0, 0],
                     [0, 0, n, n, 0, 0],
                     [0, 0, n, n, 0, 0],
                     [10, n, n, 10, n, n],
                     [n, n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_J(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 12, n, n, n],
                     [0, 0, n, n, n, n],
                     [0, 0, 0, 0, 7, n],
                     [0, 0, 0, 0, n, n],
                     [6, n, 0, 0, n, n],
                     [n, n, 9, n, n, 0],
                     [0, 9, n, n, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_K(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[7, n, 0, 0, 6, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 0, 5, n, 0],
                     [8, n, 5, n, 0, 0],
                     [n, n, 9, n, n, 0],
                     [n, n, 0, 9, n, n],
                     [n, n, 0, 0, 5, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_L(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 0, 0, 0],
                     [n, n, 0, 0, 0],
                     [n, n, 0, 0, 0],
                     [n, n, 0, 0, 0],
                     [7, n, 0, 0, 0],
                     [n, n, 10, n, n],
                     [n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_M(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 0, 0, 0, 0, 0, 7, n],
                     [n, n, 2, 0, 0, 0, 2, n, n],
                     [n, n, n, 2, 0, 2, n, n, n],
                     [n, n, 0, n, 2, n, 0, 8, n],
                     [7, n, 0, 0, n, 0, 0, n, n],
                     [n, n, 0, 0, 0, 0, 0, n, n],
                     [n, n, 0, 0, 0, 0, 0, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_N(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 0, 0, 0, 0, 7, n],
                     [n, n, 2, 0, 0, 0, n, n],
                     [n, n, n, 2, 0, 0, n, n],
                     [n, n, 0, n, 2, 0, 8, n],
                     [7, n, 0, 0, n, 2, n, n],
                     [n, n, 0, 0, 0, n, n, n],
                     [n, n, 0, 0, 0, 0, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_O(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 9, n, n, 0, 0],
                     [0, 5, n, 9, n, n, 0],
                     [7, n, 0, 0, 0, 7, n],
                     [n, n, 0, 0, 0, n, n],
                     [n, n, 0, 0, 0, n, n],
                     [0, 9, n, n, 5, n, 0],
                     [0, 0, 9, n, n, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_P(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 9, n, n, 0, 0],
                     [9, n, n, 5, n, 0],
                     [8, n, 0, 0, 6, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 9, n, n, 0],
                     [n, n, 0, 0, 0, 0],
                     [5, n, 0, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_Q(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 11, n, n, n, 0, 0],
                     [8, n, 11, n, n, n, 0],
                     [n, n, 0, 0, 8, n, 0],
                     [n, n, 0, 0, n, n, 0],
                     [n, n, 0, 0, n, n, 0],
                     [11, n, n, n, n, n, 0],
                     [0, 5, n, 11, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_R(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 9, n, n, 0, 0, 0],
                     [9, n, n, 5, n, 0, 0],
                     [8, n, 0, 0, 6, n, 0],
                     [n, n, 0, 0, n, n, 0],
                     [n, n, 9, n, n, 0, 0],
                     [n, n, 0, 9, n, n, 0],
                     [5, n, 0, 0, 9, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_S(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[12, n, n, n, 6, n],
                     [n, n, n, n, n, n],
                     [5, n, 0, 0, 0, 0],
                     [0, 11, n, n, n, 0],
                     [0, 0, 0, 0, 5, n],
                     [6, n, 12, n, n, n],
                     [n, n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_T(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[10, n, n, 10, n, n],
                     [n, n, n, n, n, n],
                     [0, 0, 7, n, 0, 0],
                     [0, 0, n, n, 0, 0],
                     [0, 0, n, n, 0, 0],
                     [0, 0, 6, n, 0, 0],
                     [0, 0, n, n, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_U(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 0, 0, 8, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 0, 0, n, n],
                     [6, n, 0, 0, 6, n],
                     [n, n, 5, n, n, n],
                     [0, 11, n, n, n, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_V(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[5, n, 0, 0, 0, 0, 0, 5, n],
                     [0, 6, n, 0, 0, 0, 6, n, 0],
                     [0, n, n, 0, 0, 0, n, n, 0],
                     [0, 0, 6, n, 0, 6, n, 0, 0],
                     [0, 0, n, n, 0, n, n, 0, 0],
                     [0, 0, 0, 9, n, n, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_W(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                     [n, 2, 0, 0, 0, 10, n, n, 0, 0, 0, 2, n],
                     [n, n, 0, 0, 0, n, n, n, 0, 0, 0, n, n],
                     [0, 6, n, 0, 6, n, 0, 6, n, 0, 6, n, 0],
                     [0, n, n, 0, n, n, 0, n, n, 0, n, n, 0],
                     [0, 0, 9, n, n, 0, 0, 0, 9, n, n, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_X(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[2, 0, 0, 0, 0, 0, 2],
                     [n, 2, 0, 0, 0, 2, n],
                     [0, n, 3, 0, 3, n, 0],
                     [0, 0, n, 1, n, 0, 0],
                     [0, 2, n, 0, n, 2, 0],
                     [2, n, 0, 0, 0, n, 2],
                     [n, 0, 0, 0, 0, 0, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_Y(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[6, n, 0, 0, 0, 0, 6, n],
                     [n, n, 0, 0, 0, 0, n, n],
                     [0, 5, n, 0, 0, 5, n, 0],
                     [0, 0, 11, n, n, n, 0, 0],
                     [0, 0, 0, 7, n, 0, 0, 0],
                     [0, 0, 0, n, n, 0, 0, 0],
                     [0, 0, 0, n, n, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_Z(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[6, n, 12, n, n, n],
                     [n, n, n, n, n, n],
                     [0, 0, 0, 0, 5, n],
                     [0, 11, n, n, n, 0],
                     [5, n, 0, 0, 0, 0],
                     [12, n, n, n, 6, n],
                     [n, n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_space(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_colon(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 0, 0],
                     [0, 6, n, 0],
                     [0, n, n, 0],
                     [0, 0, 0, 0],
                     [0, 6, n, 0],
                     [0, n, n, 0],
                     [0, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_apostrophe(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[9, n, n],
                     [0, 6, n],
                     [0, n, n],
                     [0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_hyphen(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [11, n, n, n],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_zero(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 11, n, n, n, 0],
                     [8, n, 11, n, n, n],
                     [n, n, 0, 0, 8, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 0, 0, n, n],
                     [11, n, n, n, n, n],
                     [0, 11, n, n, n, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_one(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[10, n, n, 0],
                     [n, n, n, 0],
                     [0, 7, n, 0],
                     [0, n, n, 0],
                     [0, n, n, 0],
                     [12, n, n, n],
                     [n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_two(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[11, n, n, n, 0],
                     [9, n, n, 5, n],
                     [0, 0, 9, n, n],
                     [0, 9, n, n, 0],
                     [9, n, n, 0, 0],
                     [6, n, 10, n, n],
                     [n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)


def return_smile(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [
        [0, 0, 0, 0, 12, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, n, n, n, 0, 0, 0, 0],
        [0, 0, 0, 1, n, n, n, n, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, n, n, n, n, 1, 0, 0, 0],
        [0, 0, 6, n, 12, n, n, n, 6, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, n, 12, n, n, n, 6, n, 0, 0],
        [0, 1, n, n, n, n, n, n, n, n, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, n, n, n, n, n, n, n, n, 1, 0],
        [8, n, 8, n, 6, n, 6, n, 8, n, 8, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, n, 8, n, 6, n, 6, n, 8, n, 8, n],
        [n, n, n, n, n, n, n, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, n, n, n, n, n, n, n],
        [n, n, n, n, 6, n, 6, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, 6, n, 6, n, n, n, n, n],
        [n, n, n, n, n, n, n, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, n, n, n, n, n, n, n],
        [0, 1, 6, n, 12, n, n, n, 6, n, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, n, 12, n, n, n, 6, n, 1, 0],
        [0, 0, n, n, n, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, n, n, n, 0, 0],
        [0, 0, 0, 1, 12, n, n, n, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 12, n, n, n, 1, 0, 0, 0],
        [0, 0, 0, 0, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [12, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, n, n, n],
        [n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n],
        [0, 12, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, n, n, n, 0],
        [0, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, 0],
        [0, 0, 12, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, n, n, n, 0, 0],
        [0, 0, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, 0, 0],
        [0, 0, 0, 12, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, n, n, n, 0, 0, 0],
        [0, 0, 0, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, 0, 0, 0],
        [0, 0, 0, 0, 6, n, 10, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, n, n, 6, n, 0, 0, 0, 0],
        [0, 0, 0, 0, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 10, n, n, 6, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, n, 10, n, n, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6, n, 10, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 10, n, n, 6, n, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, 8, n, 8, n, 8, n, 8, n, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, n, n, n, n, n, n, n, n, n, n, 10, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, len(letter_matrix[0])+1, y_current)




def return_square_text(id_rect, id_circle, color, rect_std_size, x_size, y_size, x_loc, y_loc, dx, dy):

    # create text for the square
    x_rect = rect_std_size * x_size
    y_rect = rect_std_size * y_size
    x_offset = rect_std_size * (x_loc + dx)
    y_offset = rect_std_size * (y_loc + dy)
    text = return_square(id_rect, color, x_rect, y_rect, x_offset, y_offset) + '\n'
    id_rect += 1

    # create text for the circles
    for y_inc in range(y_size):
        for x_inc in range(x_size):
            x_circle = rect_std_size * (x_loc + x_inc + dx + 1) - rect_std_size / 2
            y_circle = rect_std_size * (y_loc + y_inc + dy + 1) - rect_std_size / 2
            text_circle = return_circle(id_circle, color, x_circle, y_circle)
            text += text_circle
            id_circle += 1

    return id_rect, id_circle, text