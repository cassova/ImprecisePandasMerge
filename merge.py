import pandas as pd
import numpy as np
from Levenshtein import distance 
import itertools

def imprecise_exact_merge(df1, df2, left_on, right_on):
    # NOTE: This doesn't yet support multiple columns or joining on indexes
    
    # First create a Levenshtein distance matrix
    lev_mtx = pd.DataFrame({x:np.NaN for x in df1[left_on]}, index=df2[right_on])
    for x,y in list(itertools.product(df1[left_on], df2[right_on])):
        l = distance(x,y)
        lev_mtx.loc[y][x] = l
    
    # Set our column names
    left_name = left_on
    right_name = right_on
    if left_name == right_name:
        left_name += '_x'
        right_name += '_y'
        
    # Create a new dataframe starting with the left values
    new_df = df1.copy(deep=True)
    if left_on != left_name:
        new_df = new_df.rename(columns={left_on: left_name})
    new_df[right_name] = ""
    new_df.set_index(left_name, inplace=True)
    

    # Use our Levenshtein matrix to fill in our right_name column
    for x in lev_mtx.min().sort_values().index.to_list():
        y_match = lev_mtx[x].idxmin()
        new_df.at[x,right_name] = y_match
        lev_mtx.drop(y_match, axis=0, inplace=True)
    new_df = new_df.reset_index()
    
    
    # Do a final merge of the new_df and df2
    new_df = pd.merge(new_df, df2, left_on=right_name, right_on=right_on)
    if right_name != right_on:
        new_df.drop(right_on, axis=1, inplace=True)
    
    return new_df
