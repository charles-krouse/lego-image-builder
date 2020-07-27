from html_text import return_square, return_circle
from functions import get_random_color


def fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color_list, random_color, x_current, x_add, y_current):

    text = ''

    # iterate through each row
    for xxx, x_val in enumerate(letter_matrix[0]):

        # iterate through each column
        for yyy, y_val in enumerate(letter_matrix):

            # get the current value in the matrix
            if letter_matrix[yyy][xxx] != 'n' and letter_matrix[yyy][xxx] != 'i':
                matrix_value = int(letter_matrix[yyy][xxx])
                filler = False
            else:
                matrix_value = letter_matrix[yyy][xxx]
                filler = True

            # get a random color
            if random_color:
                color = get_random_color(color_list)

            # get selected color
            elif filler:
                if matrix_value == 'n':
                    color = color_list[0]
                elif matrix_value == 'i':
                    color = color_list[1]
            elif not filler:
                if matrix_value < 13:
                    color = color_list[0]
                elif matrix_value < 33:
                    color = color_list[1]

            if matrix_value == 0:
                page[y_current+yyy][x_current+xxx] = 0
            if matrix_value == 'n' or matrix_value == 'i':
                page[y_current+yyy][x_current+xxx] = color
            if matrix_value == 1 or matrix_value == 21:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 1,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if matrix_value == 2 or matrix_value == 22:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 2,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if matrix_value == 3 or matrix_value == 23:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 3,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if matrix_value == 4 or matrix_value == 24:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 4,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if matrix_value == 5 or matrix_value == 25:
                page[y_current + yyy][x_current + xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 1,
                                                                  x_current, y_current, xxx - 1, yyy - 1)
                text += text_tmp
            if matrix_value == 6 or matrix_value == 26:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 2,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if matrix_value == 7 or matrix_value == 27:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 3,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if matrix_value == 8 or matrix_value == 28:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 4,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if matrix_value == 9 or matrix_value == 29:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 3, 1,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if matrix_value == 10 or matrix_value == 30:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 3, 2,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if matrix_value == 11 or matrix_value == 31:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 4, 1,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp
            if matrix_value == 12 or matrix_value == 32:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 4, 2,
                                                                  x_current, y_current, xxx-1, yyy-1)
                text += text_tmp

    x_current += x_add
    return text, x_current, y_current, rect_id, circle_id

def return_A(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 5, n, 0, 0],
                     [0, 11, n, n, n, 0],
                     [8, n, 0, 0, 8, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 5, n, n, n],
                     [n, n, 0, 0, n, n],
                     [5, n, 0, 0, 5, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_B(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 9, n, n, 0],
                     [n, n, 0, 0, 6, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 9, n, n, 0],
                     [7, n, 0, 0, 6, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 9, n, n, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_C(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 9, n, n, 0],
                     [0, 11, n, n, n, 2],
                     [7, n, 0, 0, 0, n],
                     [n, n, 0, 0, 0, 0],
                     [n, n, 0, 0, 0, 2],
                     [0, 11, n, n, n, n],
                     [0, 0, 9, n, n, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_D(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[11, n, n, n, 0, 0],
                     [7, n, 9, n, n, 0],
                     [n, n, 0, 0, 7, n],
                     [n, n, 0, 0, n, n],
                     [6, n, 0, 0, n, n],
                     [n, n, 9, n, n, 0],
                     [11, n, n, n, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_E(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 10, n, n],
                     [n, n, n, n, n],
                     [n, n, 0, 0, 0],
                     [n, n, 5, n, 0],
                     [7, n, 0, 0, 0],
                     [n, n, 10, n, n],
                     [n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_F(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[10, n, n, 6, n],
                     [n, n, n, n, n],
                     [5, n, 0, 0, 0],
                     [12, n, n, n, 0],
                     [n, n, n, n, 0],
                     [6, n, 0, 0, 0],
                     [n, n, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_G(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 9, n, n, 0, 0],
                     [0, 9, n, n, 5, n, 0],
                     [7, n, 0, 0, 0, 0, 0],
                     [n, n, 0, 0, 1, 3, 2],
                     [n, n, 0, 0, 0, n, n],
                     [0, 11, n, n, n, n, 0],
                     [0, 0, 9, n, n, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_H(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 0, 0, 7, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 6, n, 8, n],
                     [7, n, n, n, n, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 0, 0, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_I(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[10, n, n, 10, n, n],
                     [n, n, n, n, n, n],
                     [0, 0, 7, n, 0, 0],
                     [0, 0, n, n, 0, 0],
                     [0, 0, n, n, 0, 0],
                     [10, n, n, 10, n, n],
                     [n, n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_J(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 12, n, n, n],
                     [0, 0, n, n, n, n],
                     [0, 0, 0, 0, 7, n],
                     [0, 0, 0, 0, n, n],
                     [6, n, 0, 0, n, n],
                     [n, n, 9, n, n, 0],
                     [0, 9, n, n, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_K(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[7, n, 0, 0, 6, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 0, 5, n, 0],
                     [8, n, 5, n, 0, 0],
                     [n, n, 9, n, n, 0],
                     [n, n, 0, 9, n, n],
                     [n, n, 0, 0, 5, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_L(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 0, 0, 0],
                     [n, n, 0, 0, 0],
                     [n, n, 0, 0, 0],
                     [n, n, 0, 0, 0],
                     [7, n, 0, 0, 0],
                     [n, n, 10, n, n],
                     [n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_M(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 0, 0, 0, 0, 0, 7, n],
                     [n, n, 2, 0, 0, 0, 2, n, n],
                     [n, n, n, 2, 0, 2, n, n, n],
                     [n, n, 0, n, 2, n, 0, 8, n],
                     [7, n, 0, 0, n, 0, 0, n, n],
                     [n, n, 0, 0, 0, 0, 0, n, n],
                     [n, n, 0, 0, 0, 0, 0, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_N(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 0, 0, 0, 0, 7, n],
                     [n, n, 2, 0, 0, 0, n, n],
                     [n, n, n, 2, 0, 0, n, n],
                     [n, n, 0, n, 2, 0, 8, n],
                     [7, n, 0, 0, n, 2, n, n],
                     [n, n, 0, 0, 0, n, n, n],
                     [n, n, 0, 0, 0, 0, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_O(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 9, n, n, 0, 0],
                     [0, 5, n, 9, n, n, 0],
                     [7, n, 0, 0, 0, 7, n],
                     [n, n, 0, 0, 0, n, n],
                     [n, n, 0, 0, 0, n, n],
                     [0, 9, n, n, 5, n, 0],
                     [0, 0, 9, n, n, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_P(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 9, n, n, 0, 0],
                     [9, n, n, 5, n, 0],
                     [8, n, 0, 0, 6, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 9, n, n, 0],
                     [n, n, 0, 0, 0, 0],
                     [5, n, 0, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_Q(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 11, n, n, n, 0, 0],
                     [8, n, 11, n, n, n, 0],
                     [n, n, 0, 0, 8, n, 0],
                     [n, n, 0, 0, n, n, 0],
                     [n, n, 0, 0, n, n, 0],
                     [11, n, n, n, n, n, 0],
                     [0, 5, n, 11, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_R(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 9, n, n, 0, 0, 0],
                     [9, n, n, 5, n, 0, 0],
                     [8, n, 0, 0, 6, n, 0],
                     [n, n, 0, 0, n, n, 0],
                     [n, n, 9, n, n, 0, 0],
                     [n, n, 0, 9, n, n, 0],
                     [5, n, 0, 0, 9, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_S(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[12, n, n, n, 6, n],
                     [n, n, n, n, n, n],
                     [5, n, 0, 0, 0, 0],
                     [0, 11, n, n, n, 0],
                     [0, 0, 0, 0, 5, n],
                     [6, n, 12, n, n, n],
                     [n, n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_T(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[10, n, n, 10, n, n],
                     [n, n, n, n, n, n],
                     [0, 0, 7, n, 0, 0],
                     [0, 0, n, n, 0, 0],
                     [0, 0, n, n, 0, 0],
                     [0, 0, 6, n, 0, 0],
                     [0, 0, n, n, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_U(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 0, 0, 8, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 0, 0, n, n],
                     [6, n, 0, 0, 6, n],
                     [n, n, 5, n, n, n],
                     [0, 11, n, n, n, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_V(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[5, n, 0, 0, 0, 0, 0, 5, n],
                     [0, 6, n, 0, 0, 0, 6, n, 0],
                     [0, n, n, 0, 0, 0, n, n, 0],
                     [0, 0, 6, n, 0, 6, n, 0, 0],
                     [0, 0, n, n, 0, n, n, 0, 0],
                     [0, 0, 0, 9, n, n, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_W(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
                     [n, n, 0, 0, 0, 10, n, n, 0, 0, 0, n, n],
                     [n, n, 0, 0, 0, n, n, n, 0, 0, 0, n, n],
                     [0, 6, n, 0, 6, n, 0, 6, n, 0, 6, n, 0],
                     [0, n, n, 0, n, n, 0, n, n, 0, n, n, 0],
                     [0, 0, 9, n, n, 0, 0, 0, 9, n, n, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_X(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[2, 0, 0, 0, 0, 0, 2],
                     [n, 2, 0, 0, 0, 2, n],
                     [0, n, 3, 0, 3, n, 0],
                     [0, 0, n, 1, n, 0, 0],
                     [0, 2, n, 0, n, 2, 0],
                     [2, n, 0, 0, 0, n, 2],
                     [n, 0, 0, 0, 0, 0, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_Y(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[6, n, 0, 0, 0, 0, 6, n],
                     [n, n, 0, 0, 0, 0, n, n],
                     [0, 5, n, 0, 0, 5, n, 0],
                     [0, 0, 11, n, n, n, 0, 0],
                     [0, 0, 0, 7, n, 0, 0, 0],
                     [0, 0, 0, n, n, 0, 0, 0],
                     [0, 0, 0, n, n, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_Z(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[6, n, 12, n, n, n],
                     [n, n, n, n, n, n],
                     [0, 0, 0, 0, 5, n],
                     [0, 11, n, n, n, 0],
                     [5, n, 0, 0, 0, 0],
                     [12, n, n, n, 6, n],
                     [n, n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_space(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_colon(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 0, 0],
                     [0, 6, n, 0],
                     [0, n, n, 0],
                     [0, 0, 0, 0],
                     [0, 6, n, 0],
                     [0, n, n, 0],
                     [0, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_apostrophe(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[9, n, n],
                     [0, 6, n],
                     [0, n, n],
                     [0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_hyphen(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [11, n, n, n],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_pound(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 0, 4, 0, 2, 0, 0],
                     [0, 0, n, 0, n, 0, 0],
                     [5, n, n, 11, n, n, n],
                     [0, 0, n, 0, 4, 0, 0],
                     [11, n, n, n, n, 5, n],
                     [0, 0, 4, 0, n, 0, 0],
                     [0, 0, n, 0, n, 0, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_zero(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 11, n, n, n, 0],
                     [8, n, 11, n, n, n],
                     [n, n, 0, 0, 8, n],
                     [n, n, 0, 0, n, n],
                     [n, n, 0, 0, n, n],
                     [11, n, n, n, n, n],
                     [0, 11, n, n, n, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_one(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[10, n, n, 0],
                     [n, n, n, 0],
                     [0, 7, n, 0],
                     [0, n, n, 0],
                     [0, n, n, 0],
                     [12, n, n, n],
                     [n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_two(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[11, n, n, n, 0],
                     [9, n, n, 5, n],
                     [0, 0, 9, n, n],
                     [0, 9, n, n, 0],
                     [9, n, n, 0, 0],
                     [6, n, 10, n, n],
                     [n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_three(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[6, n, 10, n, n],
                     [n, n, n, n, n],
                     [0, 0, 0, 7, n],
                     [0, 5, n, n, n],
                     [0, 0, 0, n, n],
                     [10, n, n, 6, n],
                     [n, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_four(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[8, n, 0, 7, n],
                     [n, n, 0, n, n],
                     [n, n, 0, n, n],
                     [n, n, 9, n, n],
                     [0, 0, 0, 7, n],
                     [0, 0, 0, n, n],
                     [0, 0, 0, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_five(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[10, n, n, 6, n,0 ],
                     [n, n, n, n, n,0 ],
                     [5, n, 0, 0, 0, 0],
                     [11, n, n, n, 4, 0],
                     [0, 0, 0, 0, n, 2],
                     [12, n, n, n, n, n],
                     [n, n, n, n, n, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_six(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[11, n, n, n, 0],
                     [6, n, 0, 0, 0],
                     [n, n, 0, 0, 0],
                     [7, n, 9, n, n],
                     [n, n, 0, 7, n],
                     [n, n, 0, n, n],
                     [9, n, n, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_seven(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[3, 12, n, n, n],
                     [n, n, n, n, n],
                     [n, 0, 0, 7, n],
                     [0, 0, 0, n, n],
                     [0, 0, 0, n, n],
                     [0, 0, 0, 6, n],
                     [0, 0, 0, n, n]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_heart(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    letter_matrix = [
        [0, 0, 9, n, n, 0, 0, 0, 0, 9, n, n, 0, 0],
        [0, 9, n, n, 5, n, 0, 0, 5, n, 9, n, n, 0],
        [3, 4, 10, n, n, 12, n, n, n, 10, n, n, 4, 3],
        [n, n, n, n, n, n, n, n, n, n, n, n, n, n],
        [n, n, 3, 2, 6, n, 8, n, 6, n, 2, 3, n, n],
        [0, n, n, n, n, n, n, n, n, n, n, n, n, 0],
        [0, 0, n, 1, 5, n, n, n, 5, n, 1, n, 0, 0],
        [0, 0, 0, 9, n, n, n, n, 9, n, n, 0, 0, 0],
        [0, 0, 0, 0, 9, n, n, 9, n, n, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 11, n, n, n, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, n, 0, 0, 0, 0, 0, 0]
    ]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)



def return_smile(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
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
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)


def return_helmet(rect_std_size, rect_id, circle_id, color, color_rand_bool, page, x_current, y_current):
    n = 'n'
    i = 'i'
    letter_matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, n, 8, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, n, n, n, n, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, n, n, n, n, n, 6, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 12, n, n, n, 12, n, n, n, 12, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, n, n, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6, n, 0, 0, 0, 0, 7, n, 0, 0, 0, 0, 6, n, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, n, n, 11, n, n, n, n, n, 11, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, n, 5, n, 9, n, n, n, n, 9, n, n, 5, n, 6, n, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, n, n, 32, i, i, i, 32, i, i, i, 32, i, i, i, n, n, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 29, i, i, i, i, i, i, i, i, i, i, i, i, i, i, 29, i, i, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 26, i, 0, 26, i, 0, 22, 0, 27, i, 0, 22, 0, 26, i, 0, 26, i, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, i, i, 0, i, i, 0, i, 0, i, i, 0, i, 0, i, i, 0, i, i, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, n, n, 21, 30, i, i, 0, 24, 0, i, i, 0, 24, 0, 30, i, i, 21, 9, n, n, 0, 0, 0, 0],
        [0, 0, 6, n, 11, n, n, n, i, i, i, 0, i, 0, 27, i, 0, i, 0, i, i, i, 11, n, n, n, 6, n, 0, 0],
        [1, 2, n, n, 9, n, n, 7, n, 21, 26, i, i, 0, i, i, 0, i, 26, i, 21, 7, n, 9, n, n, n, n, 2, 1],
        [0, n, 6, n, 0, 5, n, n, n, 1, i, i, i, 0, i, i, 0, i, i, i, 1, n, n, 5, n, 0, 6, n, n, 0],
        [0, 0, n, n, 9, n, n, n, n, 8, n, 31, i, i, i, 31, i, i, i, 8, n, n, n, 9, n, n, n, n, 0, 0],
        [0, 0, 0, 1, 6, n, 10, n, n, n, n, 6, n, 31, i, i, i, 6, n, n, n, 10, n, n, 6, n, 1, 0, 0, 0],
        [0, 0, 0, 0, n, n, n, n, n, n, n, n, n, 11, n, n, n, n, n, n, n, n, n, n, n, n, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 6, n, 0, n, n, 12, n, n, n, 12, n, n, n, n, n, 0, 6, n, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, n, n, 9, n, n, n, n, n, n, n, n, n, n, 9, n, n, n, n, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 6, n, 10, n, n, 12, n, n, n, 10, n, n, 6, n, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, n, 0, 11, n, n, n, 0, 6, n, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, 9, n, n, 9, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, n, 6, n, 6, n, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, n, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, color_rand_bool, x_current, len(letter_matrix[0])+1, y_current)




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