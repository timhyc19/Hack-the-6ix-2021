import mouse


class Cursor:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def modify_position(self):
        self.pos_x, self.pos_y = mouse.get_position()
    