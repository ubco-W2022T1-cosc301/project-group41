import pandas as pd
import numpy as np

def load_and_process():

    return df
    
    df = (
        pd.read_csv(
    r"C:\Users\remit\Downloads\2015 (2).csv", 
    usecols = ['Country', 'Happiness Rank', 'Happiness Score', 'Standard Error', 'Family', 'Freedom', 'Dystopia Residual']
)
.drop('Family', axis = 1)
.assign(
        testColumn = lambda x: x['Happiness Score'] + x['Standard Error']
    )
.rename(columns = {'Happiness Rank': 'Happy Rank'}) 
) 
    
    df
