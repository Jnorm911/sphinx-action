import os
import pandas as pd

def subtraction(a,b):
   """Simple subtraction function

   Args:
       a (int): int from user input
       b (int): int from user input

   Returns:
       int: c, the subtraction of user input a - b
   """
   c = a-b
   return c


def load_data(LOADDATES, data_path, filename, cols=None):
    """ Hello World
    """
    datals = []  
    data = pd.read_csv(os.path.join(data_path, filename)).fillna("Unknown")
    data = data[cols]
    datals.info(data.shape)
    return data