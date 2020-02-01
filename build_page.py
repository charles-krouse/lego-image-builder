import random
# TODO: break into multiple files in order to simplify

def main():

    # input name of output file
    filename = 'view_legos.svg'

    debug = False

    # create a 2D array which will form the page
    alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                     'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    x_page, y_page = 40, 20
    page = [[0 for _ in range(x_page)] for _ in range(y_page)]

    # input desired background colors
    # yellow, green, red, blue
    # color_list = ['e1fb00', '26d400', 'ff0019', '0071ff']
    color_list = ['ff0019']
    # gray scale: black -> white
    # color_list = ['000000', '242424', '717171', 'bdbdbd', 'ffffff']

    # input desired text colors
    # color_text = ['1', '2', '3']
    color_text = ['bdbdbd']

    # input desired text
    text = 'aaaa'

    # rectangle and document properties
    rect_std_size = 50
    rect_id = 1010
    circle_id = 0
    document_units = 'mm'
    document_x = x_page*rect_std_size
    document_y = y_page*rect_std_size

    # insert text before filling matrix with blocks
    page, text_svg, rect_id, circle_id = populate_text(rect_std_size, rect_id, circle_id, text, color_text, page)
    if debug:
        print(text_svg)
        print_matrix(page)

    # create a counter to iterate through alphabet
    alphabet_counter = 0

    # open and write to file
    print('Creating file...')
    with open(filename, 'w') as f:

        # initialize the svg file
        f.write(return_svg_header(document_x, document_y, document_units, filename))
        f.write(return_square_filter())
        f.write(return_circle_filter())
        f.write(return_svg_mid())

        # write the text blocks
        f.write(text_svg)

        # TODO: this is a nasty nested loop, and it should be revised
        # TODO: there is a bug that results in missing circles, but it seems random
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
                    f.write(return_square(rect_id, color_rand, x_rect, y_rect, x_offset, y_offset))

                    # write circles to file
                    for y_inc in range(y_rand):
                        for x_inc in range(x_rand):
                            x_circle = rect_std_size * (x_loc + x_inc) - rect_std_size/2
                            y_circle = rect_std_size * (y_loc + y_inc) - rect_std_size/2
                            f.write(return_circle(circle_id, color_rand, x_circle, y_circle))
                            circle_id += 1

                    # increment the block id
                    rect_id+=1

                # do not fill already occupied spaces
                else:
                    if debug:
                        print('\t->filled')

        # write the svg footer to file
        f.write(return_svg_footer())

    if debug:
        print_matrix(page)
    print('Done! File created: {}'.format(filename))


def populate_text(rect_std_size, rect_id, circle_id, text, color, page):

    # each letter is 7 units high
    y_letter = 7
    y_page = len(page)
    x_page = len(page[0])

    # create a counter for the length of the text
    total_length = 0

    # loop through each letter in the text to get total unit length
    for letter in text:
        letter_length = 0
        letter_upper = letter.upper()

        if letter_upper == 'A':
            letter_length = 6
        if letter_upper == 'B':
            letter_length = 5
        total_length+=letter_length

    # calculate total length by adding space between each letter
    total_length = total_length+len(text)-1

    # determine upper-left starting position
    x_start = int((x_page - total_length) / 2)
    # TODO: what if this is a 1/2 number?
    y_start = int((y_page - y_letter) / 2)

    # initialize the starting location
    x_current = x_start
    y_current = y_start

    # create a string of text
    text_svg = ''

    # after getting length, populate the page array
    for letter in text:
        letter_upper = letter.upper()

        # get a random color from the list
        color_rand = get_random_color(color)

        # TODO: implement other letters
        if letter_upper == 'A':

            # row 1
            rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color_rand, rect_std_size, 2, 1, x_current, y_current, 1, -1)
            text_svg += text_tmp

            # TODO: create a function and loop to simplify this -> is it possible?
            page[y_current][x_current] = 0
            page[y_current][x_current+1] = 0
            page[y_current][x_current+2] = color_rand
            page[y_current][x_current+3] = color_rand
            page[y_current][x_current+4] = 0
            page[y_current][x_current+5] = 0

            # row 2
            rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color_rand, rect_std_size, 1, 2, x_current, y_current, 0, 0)
            text_svg += text_tmp

            rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color_rand, rect_std_size, 1, 4, x_current, y_current, 3, 0)
            text_svg += text_tmp

            page[y_current+1][x_current] = 0
            page[y_current+1][x_current + 1] = color_rand
            page[y_current+1][x_current + 2] = 0
            page[y_current+1][x_current + 3] = 0
            page[y_current+1][x_current + 4] = color_rand
            page[y_current+1][x_current + 5] = 0

            # row 3
            page[y_current + 2][x_current] = 0
            page[y_current + 2][x_current + 1] = color_rand
            page[y_current + 2][x_current + 2] = 0
            page[y_current + 2][x_current + 3] = 0
            page[y_current + 2][x_current + 4] = color_rand
            page[y_current + 2][x_current + 5] = 0

            # row 4

            rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color_rand, rect_std_size, 2, 3, x_current, y_current, -1, 2)
            text_svg += text_tmp

            rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color_rand, rect_std_size, 1, 4, x_current, y_current, 4, 2)
            text_svg += text_tmp

            page[y_current + 3][x_current] = color_rand
            page[y_current + 3][x_current + 1] = color_rand
            page[y_current + 3][x_current + 2] = 0
            page[y_current + 3][x_current + 3] = 0
            page[y_current + 3][x_current + 4] = color_rand
            page[y_current + 3][x_current + 5] = color_rand

            # row 5
            rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color_rand, rect_std_size, 2, 1, x_current, y_current, 1, 3)
            text_svg += text_tmp

            page[y_current + 4][x_current] = color_rand
            page[y_current + 4][x_current + 1] = color_rand
            page[y_current + 4][x_current + 2] = color_rand
            page[y_current + 4][x_current + 3] = color_rand
            page[y_current + 4][x_current + 4] = color_rand
            page[y_current + 4][x_current + 5] = color_rand

            # row 6
            rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color_rand, rect_std_size, 1, 2, x_current, y_current, 3, 4)
            text_svg += text_tmp

            page[y_current + 5][x_current] = color_rand
            page[y_current + 5][x_current + 1] = color_rand
            page[y_current + 5][x_current + 2] = 0
            page[y_current + 5][x_current + 3] = 0
            page[y_current + 5][x_current + 4] = color_rand
            page[y_current + 5][x_current + 5] = color_rand

            # row 7
            rect_id, circle_id, text_tmp = return_square_text(rect_id, circle_id, color_rand, rect_std_size, 2, 1, x_current, y_current, -1, 5)
            text_svg += text_tmp

            page[y_current + 6][x_current] = color_rand
            page[y_current + 6][x_current + 1] = color_rand
            page[y_current + 6][x_current + 2] = 0
            page[y_current + 6][x_current + 3] = 0
            page[y_current + 6][x_current + 4] = color_rand
            page[y_current + 6][x_current + 5] = color_rand

        if letter_upper == 'B':
            pass

        # add a space -> this is the length of the letter plus one
        x_current+=7

    # TODO: add a check to ensure that text is shorter than the page
    # TODO: add ability for multiple lines of text
    print('text length = {}'.format(total_length))
    print('page x = {}'.format(x_page))
    print('page y = {}'.format(y_page))

    return page, text_svg, rect_id, circle_id


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


def return_svg_header(w, h, units, filename):
    text = '''
    <?xml version="1.0" encoding="UTF-8" standalone="no"?>

    <svg
       xmlns:dc="http://purl.org/dc/elements/1.1/"
       xmlns:cc="http://creativecommons.org/ns#"
       xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
       xmlns:svg="http://www.w3.org/2000/svg"
       xmlns="http://www.w3.org/2000/svg"
       xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
       xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
       width="{}{}"
       height="{}{}"
       viewBox="0 0 0 0"
       id="svg13695"
       version="1.1"
       inkscape:version="0.91 r13725"
       sodipodi:docname="{}">

    <defs
       id="defs13697">
    '''.format(w, units, h, units, filename)

    return text


def return_svg_mid():
    text = '''
    </defs>

     <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.35"
     inkscape:cx="-942.14286"
     inkscape:cy="520"
     inkscape:document-units="px"
     inkscape:current-layer="layer1"
     showgrid="false"
     inkscape:window-width="1474"
     inkscape:window-height="841"
     inkscape:window-x="54"
     inkscape:window-y="-8"
     inkscape:window-maximized="1"
     showborder="false" />
  <metadata
     id="metadata13700">
     <rdf:RDF>
     <cc:Work
     rdf:about="">
     <dc:format>image/svg+xml</dc:format>
     <dc:type
     rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
     <dc:title></dc:title>
     </cc:Work>
     </rdf:RDF>
  </metadata> 

  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1">'''

    return text


def return_svg_footer():
    text = '''
    </g>
    </svg>
    '''
    return text


def return_square(id, color, w, h, w_offset, h_offset):
    # matrix(-1,0,0,-1, x, y) flips the shadow from upper-left to lower-right
    #   x = move in the x-direction
    #   y = move in the y-direction
    text = '''
       <rect
       style="display:inline;opacity:1;fill:#{};fill-opacity:1;stroke:#000000;stroke-width:2;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1;filter:url(#filter7480)"
       id="rect{}"
       width="{}"
       height="{}"
       x="0"
       y="0"
       transform="matrix(-1,0,0,-1,{},{})" />
    '''.format(color, id, w, h, w + w_offset, h + h_offset)
    return text


def return_circle(id, color, x, y):
    text = '''
        <circle
       style="display:inline;opacity:1;fill:#{};fill-opacity:1;stroke:none;stroke-width:3;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1;filter:url(#filter6011-2-87-0-5-7-1)"
       id="path5981-3-72-0-4-6-0-{}"
       cx="{}"
       cy="{}"
       r="18.0"
       inkscape:transform-center-x="0.0"
       inkscape:transform-center-y="0.0"
       transform="matrix(1.0,0,0,1.0,0,0)" />
    '''.format(color, id, x, y)
    # transform="matrix(0.45156862,0,0,0.45156862,0,0)" />
    # r="38.638336"
    return text


def return_square_filter():
    # square filter id = 7480

    text = '''
    <filter
       style="color-interpolation-filters:sRGB"
       inkscape:label="Drop Shadow"
       id="filter7480">
      <feFlood
         flood-opacity="0.498039"
         flood-color="rgb(0,0,0)"
         result="flood"
         id="feFlood7482" />
      <feComposite
         in="flood"
         in2="SourceGraphic"
         operator="out"
         result="composite1"
         id="feComposite7484" />
      <feGaussianBlur
         in="composite1"
         stdDeviation="3"
         result="blur"
         id="feGaussianBlur7486" />
      <feOffset
         dx="6"
         dy="6"
         result="offset"
         id="feOffset7488" />
      <feComposite
         in="offset"
         in2="SourceGraphic"
         operator="atop"
         result="composite2"
         id="feComposite7490" />
    </filter> '''

    return text


def return_circle_filter():
    text = '''
    <filter
       inkscape:label="Dark And Glow"
       inkscape:menu="Shadows and Glows"
       inkscape:menu-tooltip="Darkens the edge with an inner blur and adds a flexible glow"
       style="color-interpolation-filters:sRGB"
       id="filter6011-2-87-0-5-7-1"
       y="-0.25"
       height="1.5">
      <feGaussianBlur
         stdDeviation="6"
         in="SourceGraphic"
         result="result0"
         id="feGaussianBlur6013-0-7-0-79-4-7" />
      <feDiffuseLighting
         lighting-color="#ffffff"
         diffuseConstant="1"
         surfaceScale="4"
         result="result5"
         id="feDiffuseLighting6015-5-00-0-40-8-9">
        <feDistantLight
           elevation="45"
           azimuth="235"
           id="feDistantLight6017-6-81-7-0-55-4" />
      </feDiffuseLighting>
      <feComposite
         k4="0"
         k3="0"
         k2="0"
         k1="1.4"
         in2="SourceGraphic"
         in="result5"
         result="fbSourceGraphic"
         operator="arithmetic"
         id="feComposite6019-7-5-23-0-70-1" />
      <feGaussianBlur
         result="result0"
         in="fbSourceGraphic"
         stdDeviation="6"
         id="feGaussianBlur6021-6-11-2-0-52-3" />
      <feSpecularLighting
         specularExponent="25"
         specularConstant="1"
         surfaceScale="4"
         lighting-color="#ffffff"
         result="result1"
         in="result0"
         id="feSpecularLighting6023-3-0-0-2-1-4">
        <feDistantLight
           azimuth="235"
           elevation="45"
           id="feDistantLight6025-0-1-39-6-23-1" />
      </feSpecularLighting>
      <feComposite
         k4="0"
         k1="0"
         k3="1"
         k2="1"
         operator="arithmetic"
         in="fbSourceGraphic"
         in2="result1"
         result="result4"
         id="feComposite6027-6-30-62-1-0-5" />
      <feComposite
         operator="in"
         result="fbSourceGraphic"
         in2="SourceGraphic"
         in="result4"
         id="feComposite6029-6-5-5-1-0-2" />
      <feColorMatrix
         result="fbSourceGraphicAlpha"
         in="fbSourceGraphic"
         values="0 0 0 -1 0 0 0 0 -1 0 0 0 0 -1 0 0 0 0 1 0"
         id="feColorMatrix6110-9-7-5-4-2" />
      <feGaussianBlur
         id="feGaussianBlur6112-9-9-4-7-5"
         stdDeviation="5"
         result="result6"
         in="fbSourceGraphic" />
      <feComposite
         id="feComposite6114-9-2-1-91-4"
         in2="result6"
         result="result8"
         in="fbSourceGraphic"
         operator="atop" />
      <feComposite
         id="feComposite6116-50-71-7-8-0"
         in2="fbSourceGraphicAlpha"
         result="result9"
         operator="over"
         in="result8" />
      <feColorMatrix
         id="feColorMatrix6118-87-2-5-7-6"
         values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 "
         result="result10" />
      <feBlend
         id="feBlend6120-0-3-0-37-5"
         in2="result6"
         in="result10"
         mode="normal" />
    </filter>
    '''
    return text


if __name__ == '__main__':
    main()