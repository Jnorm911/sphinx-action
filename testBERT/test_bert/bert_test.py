import os
import pandas as pd
import logging



def load_data(LOADDATES, data_path, filename, cols=None):
    """
    Loads ICDC / ODES data

    Args:
        LOADDATES (Date): Loads dates
        data_path (path): The location of the file
        filename (String): The name of the file
        cols (int): number of columns.

    Returns:
        Series: "data", a pandas series of data 
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
    logging.info(data.shape)
    return data