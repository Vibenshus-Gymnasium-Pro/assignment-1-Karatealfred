style = 'stroke="black" stroke-width="1px" fill="#7CFC00" opacity="0.3"'

def draw_svg(width, height, shapes):
    """Puts svg header and footer around some svg shapes.
    Input:
    - width: int, desired width of the svg drawing in pixels
    - height: int, desired height of the svg drawing in pixels
    - shapes: str, svg code describing the contents of the drawing
    Output:
    - str, the given svg code surrounded by header and footer tags
    """
    viewbox = 'viewBox="0 0 ' + str(width) + ' ' + str(height) + '"'
    xmlns = 'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
    header = '<svg width="' + str(width) + '" height="' + str(height) + '" ' + xmlns + viewbox +  '>'
    footer = '</svg>'
    return header + shapes + footer

def save(svg, filename):
    """Saves some svg code to a file.
    Input:
    - svg: str, the svg code (made with draw_svg)
    - filename: str, name of the file to save in
    """
    with open(filename, 'w') as f:
        f.write(svg)

def draw_circle(x, y, radius):
    """Creates svg code for drawing a circle.
    Input:
    - x: int, x-coordinate of the center of the circle in pixels
    - y: int, y-coordinate of the center of the circle in pixels
    - radius: int, radius of the circle in pixels
    Output:
    - str, svg code describing a circle
    """
    cx = 'cx="' + str(x) + '"'
    cy = 'cy="' + str(y) + '"'
    rad = 'r="' + str(radius) + '"'
    return '<circle ' + cx + ' ' + cy + ' ' + rad + ' ' + style + '/>'

def draw_rectangle(x,y,w,h):
    x = 'x="' + str(x) + '"'
    y = 'y="' + str(y) + '"'
    w = 'width="' + str(w) + '"'
    h = 'height="' + str(h) + '"'
    return '<rect '+x+' '+y+' '+w+' '+h+'/>'

def draw_triangle(x1,y1,x2,y2,x3,y3,color):
    x1=str(x1)
    x2=str(x2)
    x3=str(x3)
    y1=str(y1)
    y2=str(y2)
    y3=str(y3)
    return '<polygon points="'+x1+','+y1+' '+x2+','+y2+' '+x3+','+y3+'" '+'fill="'+color+'" />'

# An example drawing:
shapes = ""
shapes = shapes + draw_circle(220, 220, 200)
shapes = shapes + draw_circle(220, 220, 180)
shapes = shapes + draw_circle(400, 220, 180)
#shapes = shapes + draw_rectangle(5,30,233,372)
shapes = shapes + draw_triangle(30,30,60,30,45,45, '#7CFC00')

# Turn the shapes into a proper SVG drawing, on a 500x500 canvas
drawing = draw_svg(500, 500, shapes)

# Save the example drawing to a file
save(drawing, 'test1.svg')