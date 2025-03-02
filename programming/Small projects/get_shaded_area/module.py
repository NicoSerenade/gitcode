import math as m

def get_area_square(square_side):
    area = square_side**2
    return area

def get_area_circle(square_side):
    radius = square_side/2
    return m.pi*(radius**2)

def get_shaded_area(square_side):
    area_square = get_area_square(square_side)
    area_circle = get_area_circle(square_side)
    shaded_area = area_square - area_circle
    return shaded_area
