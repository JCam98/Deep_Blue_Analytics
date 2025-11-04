class Input:
    def __init__(self, x, y):
        if not isinstance(x, (int, float, type(None))) or not isinstance(y, (int, float, type(None))):
            raise TypeError("Both x and y must be numeric or None (int, float, or None)")
        self.x = x
        self.y = y
    def get_vals(self):
        print(self.x, self.y)
    def set_vals(self, x, y):
        if not isinstance(x, (int, float, type(None))) or not isinstance(y, (int, float, type(None))):
            raise TypeError("Both x and y must be numeric or None (int, float, or None)")
        self.x = x
        self.y = y
            
    
