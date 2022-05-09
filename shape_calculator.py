import math

class Rectangle:

#ATTRIBUTES     
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
        
#METHODS

    def set_width(self, new_width: int):
        self.width = new_width

    def set_height (self, new_height: int):
        self.height = new_height
    
    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
 
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for i in range(self.height):
            for j in range(self.width):
              picture += '*'
              if j == self.width - 1:
                  picture += '\n'
        return picture
      
    def get_amount_inside(self, shape):
        times_in_heigth = round(self.height / shape.height)
        times_in_width = math.floor(self.width / shape.width)
        times = times_in_heigth * times_in_width
        return times

class Square(Rectangle):

#ATTRIBUTES 
    def __init__(self, side: int):
        self.width = side
        self.height = side
      
    def __str__(self):
        return f'Square(side={self.width})'

#SQUARE METHODS
    def set_side(self, new_size: int):
        self.height = new_size
        self.width = new_size

    def set_width(self, new_width: int):
        self.width = new_width
        self.height = new_width
      
    def set_height (self, new_height: int):
        self.height = new_height
        self.width = new_height
