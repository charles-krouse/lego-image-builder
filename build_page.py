import random
import html_text
import alphabet

def main():

    # input name of output file
    filename = 'view_legos.svg'

    debug = False
    automatic_sizing = True
    # input page dimensions if automatic_sizing is turned off
    x_page, y_page = 40, 20

    # input desired background colors
    # yellow, green, red, blue
    # color_list = ['e1fb00', '26d400', 'ff0019', '0071ff']
    color_list = ['717171']
    # gray scale: black -> white
    # color_list = ['000000', '242424', '717171', 'bdbdbd', 'ffffff']

    # input desired text colors
    color_text = ['ffffff']

    # rectangle and document properties
    rect_std_size = 50
    rect_id = 1010
    circle_id = 0
    document_units = 'mm'

    # input desired text
    text = 'i am new'

    # for i in text:
    #     print(i)
    #     if i == '\n':
    #         print('********')
    # quit()

    # create a 2D array which will form the page
    alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                     'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # determine page dimensions
    if automatic_sizing:
        x_buffer = 4
        y_buffer = 4
        x_page, y_page, x_start, y_start = calculate_page_size(text, x_buffer, y_buffer)
    page = [[0 for _ in range(x_page)] for _ in range(y_page)]

    document_x = x_page*rect_std_size
    document_y = y_page*rect_std_size

    # insert text before filling matrix with blocks
    page, text_svg, rect_id, circle_id = populate_text(debug, rect_std_size, rect_id, circle_id, text, color_text, page, x_start, y_start)

    if debug:
        print(text_svg)
        print_matrix(page)

    # create a counter to iterate through alphabet
    alphabet_counter = 0

    # open and write to file
    print('Creating file...')
    with open(filename, 'w') as f:

        # initialize the svg file
        f.write(html_text.return_svg_header(document_x, document_y, document_units, filename))
        f.write(html_text.return_square_filter())
        f.write(html_text.return_circle_filter())
        f.write(html_text.return_svg_mid())

        # write the text blocks
        f.write(text_svg)

        # TODO: this is a nasty nested loop, and it should be revised
        # TODO: debug missing circles
        # iterate through each column
        for x_loc in range(x_page):

            # iterate through each row
            for y_loc in range(y_page):

                # generate random size
                x_rand, y_rand = get_random_size()

                # get random color
                color_rand = get_random_color(color_list)

                if debug:
                    print('x_loc = {}, y_loc = {}'.format(x_loc, y_loc))
                    print('\tletter = {}'.format(alphabet_list[alphabet_counter]))

                # replace every location on the page that equals zero
                if page[y_loc][x_loc] == 0:
                    if debug:
                        print('\tx, y = {}, {}'.format(x_rand, y_rand))

                    # need to check if each y-location equals zero, otherwise values underneath get overwritten
                    for y_test in range(y_rand):
                        # check if we are on the page and if the location is filled
                        if (y_loc+y_test<=y_page-1) and page[y_loc + y_test][x_loc] != 0:
                            y_rand = y_test
                            if debug:
                                print('\tavoid overwriting, new y = {}'.format(y_rand))
                            break

                        # need to check if each x-location equals zero, avoids overwriting
                        for x_test in range(x_rand):
                            if (y_loc+y_test<=y_page-1) and (x_loc+x_test<=x_page-1) and page[y_loc+y_test][x_loc+x_test] != 0:
                                x_rand = x_test
                                if debug:
                                    print('\tavoid overwriting, new x = {}'.format(x_rand))
                                break

                    # fill the appropriate y-coordinates
                    for y_inc in range(y_rand):
                        # check if y-bound will be exceeded, and revise if needed
                        if (y_loc+y_inc > y_page-1):
                            y_rand = y_page-y_loc
                            if debug:
                                print('\tend of page, new y = {}'.format(y_rand))
                            break
                        # fill the x coordinates
                        for x_inc in range(x_rand):
                            # check if the x-bound will be exceeded and revise if needed
                            if (x_loc+x_inc > x_page-1):
                                x_rand = x_page-x_loc
                                if debug:
                                    print('\tend of page, new x = {}'.format(x_rand))
                                break

                            # fill the matrix with a block
                            page[y_loc+y_inc][x_loc+x_inc] = alphabet_list[alphabet_counter]

                    # increment alphabet counter
                    alphabet_counter+=1
                    if (alphabet_counter >= len(alphabet_list)):
                        alphabet_counter = 0

                    # write block to file
                    x_rect = rect_std_size*x_rand
                    y_rect = rect_std_size*y_rand
                    x_offset = rect_std_size*(x_loc-1)
                    y_offset = rect_std_size*(y_loc-1)
                    f.write(html_text.return_square(rect_id, color_rand, x_rect, y_rect, x_offset, y_offset))

                    # write circles to file
                    for y_inc in range(y_rand):
                        for x_inc in range(x_rand):
                            x_circle = rect_std_size * (x_loc + x_inc) - rect_std_size/2
                            y_circle = rect_std_size * (y_loc + y_inc) - rect_std_size/2
                            f.write(html_text.return_circle(circle_id, color_rand, x_circle, y_circle))
                            circle_id += 1

                    # increment the block id
                    rect_id+=1

                # do not fill already occupied spaces
                else:
                    if debug:
                        print('\t->filled')

        # write the svg footer to file
        f.write(html_text.return_svg_footer())

    if debug:
        print_matrix(page)

    print('Done! File created: {}'.format(filename))


def calculate_page_size(text, x_buffer, y_buffer):

    # create a counter for the length and height of the text
    total_length = 0
    total_height = 0

    # loop through each letter in the text to get total unit length
    for letter in text:

        letter_length = 0
        letter_upper = letter.upper()

        if letter_upper == 'A':
            letter_length = 6
        if letter_upper == 'B':
            letter_length = 6
        if letter_upper == 'C':
            letter_length = 6
        if letter_upper == 'D':
            letter_length = 6
        if letter_upper == 'E':
            letter_length = 5
        if letter_upper == 'F':
            letter_length = 5
        if letter_upper == 'G':
            letter_length = 7
        if letter_upper == 'H':
            letter_length = 6
        if letter_upper == 'I':
            letter_length = 6
        if letter_upper == 'J':
            letter_length = 6
        if letter_upper == 'K':
            letter_length = 6
        if letter_upper == 'L':
            letter_length = 5
        if letter_upper == 'M':
            letter_length = 9
        if letter_upper == 'N':
            letter_length = 8
        if letter_upper == 'O':
            letter_length = 7
        if letter_upper == 'P':
            letter_length = 6
        if letter_upper == 'Q':
            letter_length = 7
        if letter_upper == 'R':
            letter_length = 7
        if letter_upper == 'S':
            letter_length = 6
        if letter_upper == 'T':
            letter_length = 6
        if letter_upper == 'U':
            letter_length = 6
        if letter_upper == 'V':
            letter_length = 9
        if letter_upper == 'W':
            letter_length = 13
        if letter_upper == 'X':
            letter_length = 7
        if letter_upper == 'Y':
            letter_length = 8
        if letter_upper == 'Z':
            letter_length = 6
        if letter_upper == ' ':
            letter_length = 6
        total_length += letter_length
        # add a single space after each letter
        total_length += 1

    # remove the last single space
    text_length = total_length - 1
    x_page = text_length + x_buffer*2

    # each letter is 7 units high
    # TODO: add ability for multiple lines of text
    text_height = 7
    num_lines = 1
    total_height = text_height * num_lines
    y_page = text_height + y_buffer*2

    # determine upper-left starting position to begin writing the text
    x_start = int((x_page - total_length) / 2)+1
    y_start = int((y_page - total_height) / 2)

    return x_page, y_page, x_start, y_start


def populate_text(debug, rect_std_size, rect_id, circle_id, text, color, page, x_start, y_start):

    # initialize the starting location
    x_current = x_start
    y_current = y_start

    # create a string of text
    text_svg = ''

    # populate the page array
    for letter in text:
        letter_upper = letter.upper()

        # get a random color from the list
        color_rand = get_random_color(color)

        if letter_upper == 'A':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_A(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'B':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_B(rect_std_size, rect_id, circle_id,
                                                                                   color_rand, page, x_current,
                                                                                   y_current)
            text_svg += text_tmp

        if letter_upper == 'C':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_C(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'D':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_D(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'E':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_E(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'F':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_F(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'G':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_G(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'H':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_H(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'I':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_I(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'J':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_J(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'K':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_K(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'L':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_L(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'M':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_M(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'N':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_N(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'O':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_O(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'P':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_P(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'Q':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_Q(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'R':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_R(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'S':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_S(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'T':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_T(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'U':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_U(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'V':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_V(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'W':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_W(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'X':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_X(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'Y':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_Y(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'Z':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_Z(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == ' ':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_space(rect_std_size, rect_id, circle_id, color_rand, page, x_current, y_current)
            text_svg += text_tmp

    return page, text_svg, rect_id, circle_id


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


if __name__ == '__main__':
    main()