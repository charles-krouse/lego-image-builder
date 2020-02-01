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