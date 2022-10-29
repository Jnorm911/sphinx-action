import os
# import pandas as pd

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
    datals = []
    
    # for t, dt in enumerate(LOADDATES):
    #     FNAME = os.path.join(train_data_path, 'claim_l_{}.csv.gz'.format(dt))
    #     try:
    #         datals.append(pd.read_csv(FNAME, usecols = cols, low_memory=False).fillna('Unknown'))
    #     except:
    #         logger.info('File {} missing'.format( FNAME))
    #         continue
    #     logger.info('{} of {}, file {}'.format(t+1, len(LOADDATES), FNAME))
    
    data = pd.read_csv(os.path.join(data_path, filename)).fillna("Unknown")
    # data = pd.concat(datals, 0)
    # logger.info('check patient before sorting {}'.format(data[['PatientId','BegDateOfService','LineId']].head(20)))
    # data = data.sort_values(['PatientId','BegDateOfService','LineId'])
    # logger.info('check patient sorting {}'.format(data[['PatientId','BegDateOfService','LineId']].head(20)))
    # data = data.head(100000)
    data = data[cols]
    # logging.info(data.shape)
    return data