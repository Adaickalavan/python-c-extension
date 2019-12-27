import numpy as np
import os
import ctypes

feature_file = os.getenv("ROOT") + "lib/cpp/out/libfeature.so"
libfeature = ctypes.CDLL(feature_file) 
libfeature.synthesize_matrix.restypes = None # Return type
libfeature.synthesize_matrix.argtypes = [ # Argument type 
    ctypes.c_int,
    ctypes.c_int, 
    np.ctypeslib.ndpointer(dtype=np.uint8, ndim=2, flags=['C', 'A']),
    np.ctypeslib.ndpointer(dtype=np.float32, ndim=2, flags=['C', 'A', 'W'])]

# @profiler.profile_line
def synthesize_matrix(mat_in, row, col):
    """
    Generates a new synthesized matrix from the original matrix.
    
    Parameters
    ----------
    mat_in : ndarray[row,col], dtype numpy.uint8
        A 2D array (i.e., matrix) with data type numpy.uint8.
    row : int
        Number of rows in the mat_in argument
    col : int    
        Number of columns in the mat_in argument

    Returns
    -------
    mat_out: ndarray[row,col], dtype numpy.float32
        A new synthesized 2D array (i.e., matrix) with data type numpy.float32.
    """

    mat_out = np.zeros((row,col), dtype=np.float32)
    libfeature.synthesize_matrix(row, col, mat_in, mat_out)

    return mat_out
