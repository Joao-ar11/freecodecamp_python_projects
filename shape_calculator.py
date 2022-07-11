class Rectangle:
    w = 0
    h = 0
    def __init__(self, width, height):
        self.w, self.h = width, height
    
    
    def set_width(self, new_value):
        self.w = new_value
    
    
    def set_height(self, new_value):
        self.h = new_value
    
    
    def get_area(self):
        return self.w * self.h
    
    
    def get_perimeter(self):
        return self.w * 2 + self.h * 2
    
    
    def get_diagonal(self):
        return (self.w ** 2 + self.h ** 2) ** 0.5
    
    
    def get_picture(self):
        if self.w > 50 or self.h > 50:
            return 'Too big for picture.'
        else:
            picture = ''
            for line in range(0, self.h):
                picture += '*' * self.w + '\n'
            return picture
    
    
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()
    
    
    def __str__(self):
        return f'Rectangle(width={self.w}, height={self.h})'


class Square(Rectangle):
    s = 0 
    def __init__(self, side):
        self.s = side
        super().__init__(side, side)
    
    
    def set_side(self, side):
        self.set_height(side)

    
    
    def set_width(self, new_value):
        self.w = new_value
        self.h = new_value
        self.s = new_value
    
    
    def set_height(self, new_value):
        self.h = new_value
        self.w = new_value
        self.s = new_value
    
    
    def __str__(self):
        return f'Square(side={self.s})'
