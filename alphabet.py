from html_text import return_square, return_circle


def return_A(rect_std_size, rect_id, circle_id, color, page, x_current, y_current):

    # row 1
    rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color, rect_std_size, 2, 1, x_current, y_current, 1, -1)
    text = text_tmp

    # TODO: create a function and loop to simplify this -> is it possible?
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