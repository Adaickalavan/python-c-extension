# Automatic temporary setup of PYTHONPATH variable
import os
import sys
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
ROOT = os.getenv("ROOT")
sys.path.append(ROOT)

# Libraries
from lib import feature
import numpy as np

# ------------------------------------------------------------------------------

def process(row, col):
    # Create a dummy 2d array 
    mat_in = np.arange(row*col, dtype=np.uint8).reshape(row,col)
    
    # Call the Python function which will call  
    mat_out = feature.synthesize_matrix(mat_in, row, col)
    
    # Print the complete before and after Numpy matrices without truncation
    np.set_printoptions(threshold=sys.maxsize)
    print("Matrix In:\n",mat_in)
    print("Matrix Out:\n",mat_out)

if __name__ == '__main__':
    row = 10
    col = 10
    process(row, col)
