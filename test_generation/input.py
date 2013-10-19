'''
Created on Oct 15, 2013

@author: Thuy
'''
# Determine    if    input    is    a    triangle    using    triangle    inequality    function
def is_triangle(a, b, c):
    return True if (a < b + c and b < a + c and c < a + b) else False
def is_equilateral(a, b, c):
    return True if a == b == c else False
def is_isosceles(a, b, c):
    return True if a == b or b == c or a == c else False
#Triangle determiner:
# Input: length of the 3 edges
# Output: Not a triangle | type of triangle
def main(a, b, c):
    '''
    a: [0;2][11;20][21;22]
    b: [1;10]
    c: [8;15][100;900]
    '''
    if is_triangle(a, b, c):
        if is_equilateral(a, b, c):
            return 'Equilateral triangle'
        elif is_isosceles(a, b, c):
            return 'Isosceles triangle'
        else:
            return 'Triangle'
    else:
        return 'Not a triangle'