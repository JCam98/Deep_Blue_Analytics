class Input:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_vals(self):
        print(self.x, self.y)
    def set_vals(self, x, y):
        try:
            self.x = x
            self.y = y
        except TypeError as e:
            print(f"Error: {e}")
            
    
