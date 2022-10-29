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
    """ Loads Data

    Args:
        LOADDATES (Any): Dates
        data_path (Any): Data Path
        filename (Any): Filename
        cols (int, optional): Columns. Defaults to None.

    Returns:
        Series: pandas data
    """
    data = []
    return data