from html_text import return_square, return_circle


def return_A(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):

    # row 1
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 1, x_current, y_current, 1, -1)
    text = text_tmp

    page[y_current][x_current] = 0
    page[y_current][x_current + 1] = 0
    page[y_current][x_current + 2] = color
    page[y_current][x_current + 3] = color
    page[y_current][x_current + 4] = 0
    page[y_current][x_current + 5] = 0

    # row 2
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 2, x_current, y_current, 0, 0)
    text += text_tmp

    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 4, x_current, y_current, 3, 0)
    text += text_tmp

    page[y_current + 1][x_current] = 0
    page[y_current + 1][x_current + 1] = color
    page[y_current + 1][x_current + 2] = 0
    page[y_current + 1][x_current + 3] = 0
    page[y_current + 1][x_current + 4] = color
    page[y_current + 1][x_current + 5] = 0

    # row 3
    page[y_current + 2][x_current] = 0
    page[y_current + 2][x_current + 1] = color
    page[y_current + 2][x_current + 2] = 0
    page[y_current + 2][x_current + 3] = 0
    page[y_current + 2][x_current + 4] = color
    page[y_current + 2][x_current + 5] = 0

    # row 4
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 3, x_current, y_current, -1, 2)
    text += text_tmp

    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 4, x_current, y_current, 4, 2)
    text += text_tmp

    page[y_current + 3][x_current] = color
    page[y_current + 3][x_current + 1] = color
    page[y_current + 3][x_current + 2] = 0
    page[y_current + 3][x_current + 3] = 0
    page[y_current + 3][x_current + 4] = color
    page[y_current + 3][x_current + 5] = color

    # row 5
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 1, x_current, y_current, 1, 3)
    text += text_tmp

    page[y_current + 4][x_current] = color
    page[y_current + 4][x_current + 1] = color
    page[y_current + 4][x_current + 2] = color
    page[y_current + 4][x_current + 3] = color
    page[y_current + 4][x_current + 4] = color
    page[y_current + 4][x_current + 5] = color

    # row 6
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 2, x_current, y_current, 3, 4)
    text += text_tmp

    page[y_current + 5][x_current] = color
    page[y_current + 5][x_current + 1] = color
    page[y_current + 5][x_current + 2] = 0
    page[y_current + 5][x_current + 3] = 0
    page[y_current + 5][x_current + 4] = color
    page[y_current + 5][x_current + 5] = color

    # row 7
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 1,  x_current, y_current, -1, 5)
    text += text_tmp

    page[y_current + 6][x_current] = color
    page[y_current + 6][x_current + 1] = color
    page[y_current + 6][x_current + 2] = 0
    page[y_current + 6][x_current + 3] = 0
    page[y_current + 6][x_current + 4] = color
    page[y_current + 6][x_current + 5] = color

    # add a space -> this is the length of the letter plus one
    x_current += 7

    return text, x_current, y_current, rect_id, circle_id


def return_B(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    # row 1
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 4, x_current,
                                                      y_current, -1, -1)
    text = text_tmp

    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 1, x_current,
                                                      y_current, 1, -1)
    text += text_tmp
    page[y_current][x_current + 0] = color
    page[y_current][x_current + 1] = color
    page[y_current][x_current + 2] = color
    page[y_current][x_current + 3] = color
    page[y_current][x_current + 4] = 0

    # row 2
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 2, x_current,
                                                      y_current, 3, 0)
    text += text_tmp
    page[y_current+1][x_current + 0] = color
    page[y_current+1][x_current + 1] = color
    page[y_current+1][x_current + 2] = 0
    page[y_current+1][x_current + 3] = 0
    page[y_current+1][x_current + 4] = color

    # row 3
    page[y_current + 2][x_current + 0] = color
    page[y_current + 2][x_current + 1] = color
    page[y_current + 2][x_current + 2] = 0
    page[y_current + 2][x_current + 3] = 0
    page[y_current + 2][x_current + 4] = color

    # row 4
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 4, 1, x_current,
                                                      y_current, -1, 2)
    text += text_tmp
    page[y_current + 3][x_current + 0] = color
    page[y_current + 3][x_current + 1] = color
    page[y_current + 3][x_current + 2] = color
    page[y_current + 3][x_current + 3] = color
    page[y_current + 3][x_current + 4] = 0

    # row 5
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 4, x_current,
                                                      y_current, -1, 3)
    text += text_tmp
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 4, x_current,
                                                      y_current, 0, 3)
    text += text_tmp
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 2, x_current,
                                                      y_current, 3, 3)
    text += text_tmp
    page[y_current + 4][x_current + 0] = color
    page[y_current + 4][x_current + 1] = color
    page[y_current + 4][x_current + 2] = 0
    page[y_current + 4][x_current + 3] = 0
    page[y_current + 4][x_current + 4] = color

    # row 6
    page[y_current + 5][x_current + 0] = color
    page[y_current + 5][x_current + 1] = color
    page[y_current + 5][x_current + 2] = 0
    page[y_current + 5][x_current + 3] = 0
    page[y_current + 5][x_current + 4] = color

    # row 7
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 1, x_current,
                                                      y_current, 1, 5)
    text += text_tmp
    page[y_current + 6][x_current + 0] = color
    page[y_current + 6][x_current + 1] = color
    page[y_current + 6][x_current + 2] = color
    page[y_current + 6][x_current + 3] = color
    page[y_current + 6][x_current + 4] = 0

    x_current += 6
    return text, x_current, y_current, rect_id, circle_id

'''
key : dimension
n : filler
1 : 1x1
2 : 1x2
3 : 1x3
4 : 1x4
5 : 2x1
6 : 2x2
7 : 2x3
8 : 2x4
9 : 3x1
10 : 3x2
11 : 4x1
12 : 4x2
'''

def fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, y_current):

    text = ''

    # iterate through each row
    for xxx, x_val in enumerate(letter_matrix[0]):

        # iterate through each column
        for yyy, y_val in enumerate(letter_matrix):

            if letter_matrix[yyy][xxx] == 0:
                page[y_current+yyy][x_current+xxx] = 0
            if letter_matrix[yyy][xxx] == 'n':
                page[y_current+yyy][x_current+xxx] = color
            if letter_matrix[yyy][xxx] == 1:
                page[y_current+yyy][x_current+xxx] = color
                rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 1,
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

    x_current += 6
    return text, x_current, y_current, rect_id, circle_id


def return_C(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):
    n = 'n'
    letter_matrix = [[0, 9, n, n, 0],
                     [8, n, 9, n, n],
                     [n, n, 0, 0, 0],
                     [n, n, 0, 0, 0],
                     [n, n, 0, 0, 0],
                     [0, 6, n, 5, n],
                     [0, n, n, 1, 0]]
    return fill_letter_in_page(letter_matrix, page, rect_std_size, rect_id, circle_id, color, x_current, y_current)


def return_C_original(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):

    # row 1
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 3, 1, x_current,
                                                      y_current, 0, -1)
    text = text_tmp
    page[y_current][x_current + 0] = 0
    page[y_current][x_current + 1] = color
    page[y_current][x_current + 2] = color
    page[y_current][x_current + 3] = color
    page[y_current][x_current + 4] = 0

    # row 2
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 4, x_current,
                                                      y_current, -1, 0)
    text += text_tmp
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 3, 1, x_current,
                                                      y_current, 1, 0)
    text += text_tmp
    page[y_current+1][x_current + 0] = color
    page[y_current+1][x_current + 1] = color
    page[y_current+1][x_current + 2] = color
    page[y_current+1][x_current + 3] = color
    page[y_current+1][x_current + 4] = color

    # row 3
    page[y_current+2][x_current + 0] = color
    page[y_current+2][x_current + 1] = color
    page[y_current+2][x_current + 2] = 0
    page[y_current+2][x_current + 3] = 0
    page[y_current+2][x_current + 4] = 0

    # row 4
    page[y_current+3][x_current + 0] = color
    page[y_current+3][x_current + 1] = color
    page[y_current+3][x_current + 2] = 0
    page[y_current+3][x_current + 3] = 0
    page[y_current+3][x_current + 4] = 0

    # row 5
    page[y_current+4][x_current + 0] = color
    page[y_current+4][x_current + 1] = color
    page[y_current+4][x_current + 2] = 0
    page[y_current+4][x_current + 3] = 0
    page[y_current+4][x_current + 4] = 0

    # row 6
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 2, x_current,
                                                      y_current, 0, 4)
    text += text_tmp
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 1, x_current,
                                                      y_current, 2, 4)
    text += text_tmp
    page[y_current+5][x_current + 0] = 0
    page[y_current+5][x_current + 1] = color
    page[y_current+5][x_current + 2] = color
    page[y_current+5][x_current + 3] = color
    page[y_current+5][x_current + 4] = color

    # row 7
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 1, x_current,
                                                      y_current, 2, 5)
    text += text_tmp
    page[y_current+6][x_current + 0] = 0
    page[y_current+6][x_current + 1] = color
    page[y_current+6][x_current + 2] = color
    page[y_current+6][x_current + 3] = color
    page[y_current+6][x_current + 4] = 0

    x_current += 6
    return text, x_current, y_current, rect_id, circle_id


def return_D(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):

    # row 1
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 3, 1, x_current,
                                                      y_current, -1, -1)
    text = text_tmp
    page[y_current + 0][x_current + 0] = color
    page[y_current + 0][x_current + 1] = color
    page[y_current + 0][x_current + 2] = color
    page[y_current + 0][x_current + 3] = 0
    page[y_current + 0][x_current + 4] = 0

    # row 2
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 4, x_current,
                                                      y_current, -1, 0)
    text += text_tmp
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 1, x_current,
                                                      y_current, 2, 0)
    text += text_tmp
    page[y_current + 1][x_current + 0] = color
    page[y_current + 1][x_current + 1] = color
    page[y_current + 1][x_current + 2] = 0
    page[y_current + 1][x_current + 3] = color
    page[y_current + 1][x_current + 4] = 0

    # row 3
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 3, x_current,
                                                      y_current, 3, 1)
    text += text_tmp
    page[y_current + 2][x_current + 0] = color
    page[y_current + 2][x_current + 1] = color
    page[y_current + 2][x_current + 2] = 0
    page[y_current + 2][x_current + 3] = 0
    page[y_current + 2][x_current + 4] = color

    # row 4
    page[y_current + 3][x_current + 0] = color
    page[y_current + 3][x_current + 1] = color
    page[y_current + 3][x_current + 2] = 0
    page[y_current + 3][x_current + 3] = 0
    page[y_current + 3][x_current + 4] = color

    # row 5
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 2, x_current,
                                                      y_current, -1, 3)
    text += text_tmp
    page[y_current + 4][x_current + 0] = color
    page[y_current + 4][x_current + 1] = color
    page[y_current + 4][x_current + 2] = 0
    page[y_current + 4][x_current + 3] = 0
    page[y_current + 4][x_current + 4] = color

    # row 6
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 1, 1, x_current,
                                                      y_current, 2, 4)
    text += text_tmp
    page[y_current + 5][x_current + 0] = color
    page[y_current + 5][x_current + 1] = color
    page[y_current + 5][x_current + 2] = 0
    page[y_current + 5][x_current + 3] = color
    page[y_current + 5][x_current + 4] = 0

    # row 7
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 3, 1, x_current,
                                                      y_current, -1, 5)
    text += text_tmp
    page[y_current + 6][x_current + 0] = color
    page[y_current + 6][x_current + 1] = color
    page[y_current + 6][x_current + 2] = color
    page[y_current + 6][x_current + 3] = 0
    page[y_current + 6][x_current + 4] = 0

    x_current += 6
    return text, x_current, y_current, rect_id, circle_id


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