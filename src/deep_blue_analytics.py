# Import modules
import numpy as np
from input import Input

def main():
    input_obj = Input(4,5)
    input_obj.get_vals()
    input_obj.set_vals(6,7)

if __name__ == '__main__':
    main()
    
