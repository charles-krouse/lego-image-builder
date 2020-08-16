from functions import *
import html_text
import alphabet

def main():

    # input name of output file
    filename = 'run.svg'

    # input desired text
    # enter an asterisk for a custom image
    text = 'the way of\na pilgrim'

    use_random_colors = True
    debug = False
    debug2 = False
    automatic_sizing = True
    x_buffer =3
    y_buffer = 0
    # set y_buffer = 0 to achieve desired aspect ratio
    # golden ratio = 1.618
    # TODO: will throw error if the x-buffer is not long enough
    # widescreen ratio = 16:9
    x_to_y_aspect_ratio = 16.0/9.0

    # everybody always colors
    # color_list = ['ff0000', 'ff00bf', '6600cc', '009900', '0033cc', '009999']

    # valentines colors
    # color_list = ['ffffff', 'ffccff', 'ff66ff', 'ff0066', 'cc0000']

    # shades of green/teal (Narnia #1)
    color_list = ['008055', '00ace6', '00cca3', '009999']

    # shades of light blue (Narnia #2)
    # color_list = ['009999', '00e6e6', '00cccc']

    # black, purple, and green (Narnia #6)
    # color_list = ['262626', '6600cc', '2db300']


    # input desired text colors
    color_text = ['ffffff'] # white
    # color_text = ['ffad33'] # gold
    # color_text = ['262626'] # black

    # rectangle and document properties
    rect_std_size = 50
    rect_id = 1010
    circle_id = 0
    document_units = 'mm'


    # create a 2D array which will form the page
    alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                     'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # determine page dimensions
    if automatic_sizing:
        x_page, y_page, x_start, y_start = calculate_page_size(text, x_buffer, y_buffer, x_to_y_aspect_ratio)
    else:
        # 1920x1080
        # golden ratio = 1.618
        x_page = 50
        y_page = 50
        x_start = [1]
        y_start = 1
    page = [[0 for _ in range(x_page)] for _ in range(y_page)]

    document_x = x_page*rect_std_size
    document_y = y_page*rect_std_size

    # insert text before filling matrix with blocks
    page, text_svg, rect_id, circle_id = populate_text(debug2, rect_std_size, rect_id, circle_id, text, color_text, use_random_colors, page, x_start, y_start)

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


def calculate_page_size(text, x_buffer, y_buffer, x_to_y_aspect_ratio):

    # create a counter for the length and height of the text
    total_length = 0
    line_length_list = []
    num_lines = 1

    # create lists for the starting locations. need a new starting location for each line
    x_start = []

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

        # numbers
        if letter_upper == '0':
            letter_length = 6
        if letter_upper == '1':
            letter_length = 4
        if letter_upper == '2':
            letter_length = 5
        if letter_upper == '3':
            letter_length = 5
        if letter_upper == '4':
            letter_length = 5
        if letter_upper == '5':
            letter_length = 6
        if letter_upper == '6':
            letter_length = 5
        if letter_upper == '7':
            letter_length = 5

        # special characters
        if letter_upper == ' ':
            letter_length = 6
        if letter_upper == ':':
            letter_length = 4
        if letter_upper == '\'':
            letter_length = 3
        if letter_upper == '-':
            letter_length = 4
        if letter_upper == '#':
            letter_length = 7
        if letter_upper == '*':
            letter_length = 34 # smiley face
            letter_length = 14 # heart
            letter_length = 30 # helmet
            letter_length = 18 # milk
        if letter_upper == '\n':

            # calculate the starting location for the line
            text_length = total_length - 1
            x_page = text_length + x_buffer*2
            x_start.append(int((x_page - total_length) / 2) + 1)

            # reset the length counter
            line_length_list.append(total_length)
            letter_length = 0
            total_length = -1
            num_lines += 1

        total_length += letter_length
        # add a single space after each letter
        total_length += 1

    # get the longest line
    line_length_list.append(total_length)
    text_length = max(line_length_list)

    # remove the last single space
    text_length -= 1
    # calculate total length of the page
    x_page = text_length + x_buffer*2

    # calculate length of last line
    x_start.append(int((x_page - total_length) / 2) + 1)

    # adjust the x-start location of shorter lines so that they are centered
    for iii, x in enumerate(line_length_list):
        if (x < text_length):
            x_start[iii] = int((x_page - x) / 2) + 1

    if '*' in text:
        # using a custom image
        # TODO: add function to automatically calculate height of custom image
        # total_height = 34 # smiley face -> actual height plus 2
        total_height = 20 # heart -> actual height plus 2 + 7
        total_height = 32 # helmet -> actual height plus 2
        total_height = 42 # milk -> actual plus 2
    else:
        # each letter is 7 units high
        text_height = 7
        # add 2 spaces between lines
        text_height += 2
        total_height = text_height * num_lines - 1

    y_page = total_height + y_buffer*2
    y_start = y_buffer

    # calculate y-size if maintaining an aspect ratio
    if y_buffer == 0:
        y_page = int(x_page / x_to_y_aspect_ratio)
        y_start = int((y_page-total_height)/2+1)

    return x_page, y_page, x_start, y_start


def populate_text(debug, rect_std_size, rect_id, circle_id, text, color, use_random_colors, page, x_start, y_start):

    # initialize the starting location
    current_line = 0
    x_current = x_start[current_line]
    if debug:
        print('x_start = {}'.format(x_start))
        print('x_current = {}'.format(x_current))
    y_current = y_start

    # create a string of text
    text_svg = ''

    # populate the page array
    for letter in text:
        letter_upper = letter.upper()

        # get a random color from the list
        # color_rand = get_random_color(color)
        color_rand = color
        color_rand_bool = use_random_colors

        if letter_upper == 'A':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_A(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'B':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_B(rect_std_size, rect_id, circle_id,
                                                                                   color_rand, color_rand_bool, page, x_current,
                                                                                   y_current)
            text_svg += text_tmp

        if letter_upper == 'C':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_C(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'D':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_D(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'E':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_E(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'F':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_F(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'G':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_G(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'H':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_H(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'I':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_I(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'J':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_J(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'K':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_K(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'L':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_L(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'M':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_M(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'N':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_N(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'O':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_O(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'P':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_P(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'Q':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_Q(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'R':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_R(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'S':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_S(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'T':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_T(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'U':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_U(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'V':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_V(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'W':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_W(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'X':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_X(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'Y':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_Y(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == 'Z':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_Z(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '0':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_zero(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '1':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_one(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '2':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_two(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '3':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_three(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '4':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_four(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '5':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_five(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '6':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_six(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '7':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_seven(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == ' ':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_space(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == ':':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_colon(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '-':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_hyphen(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '#':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_pound(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '*':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_milk(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '\'':
            text_tmp, x_current, y_current, rect_id, circle_id = alphabet.return_apostrophe(rect_std_size, rect_id, circle_id, color_rand, color_rand_bool, page, x_current, y_current)
            text_svg += text_tmp

        if letter_upper == '\n':
            current_line += 1
            # move down one letter plus two spaces
            y_current += 9
            # get the next x_start location
            x_current = x_start[current_line]
            if debug:
                print('x_current = {}'.format(x_current))

    return page, text_svg, rect_id, circle_id



if __name__ == '__main__':
    main()