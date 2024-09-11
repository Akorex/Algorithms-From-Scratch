"""
Solution to Leetcode problem pandas #175 - Combine Two Tables

https://leetcode.com/problems/combine-two-tables/description/?lang=pythondata
"""

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    res = person.merge(address, how = 'left', on = 'personId')
    res = res[['firstName', 'lastName', 'city', 'state']]

    return res