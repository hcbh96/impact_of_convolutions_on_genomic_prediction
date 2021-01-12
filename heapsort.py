import pandas as pd
import numpy as np

"""
Call: add_to_heap(sorted_dtfm, col, val, num)

ARGS:
    sorted_dtfm - dataframe containing heap
    col - title of col being sorted
    val - title of value being sorted
    num - size of the heap

RETURN:
    sorted_dtfm - sorted dtfm
"""
def add_to_heap(sorted_dtfm, col, val, num):
    # If heap is too long remove the last value from the heap
    if sorted_dtfm.shape[1] == num:
        sorted_dtfm = sorted_dtfm.drop(sorted_dtfm.columns[0], axis='columns')
    # Swap the new value up the heap until it is in the correct position
    added = False
    i = 0
    length = sorted_dtfm.shape[1]
    upper_bound = sorted_dtfm.shape[1]
    if upper_bound < num : upper_bound = num
    while i < upper_bound and added == False:
        # Set the current foot of the array
        current = 0
        if length > 0 and i < length:
            current = sorted_dtfm.iat[0, i]
        # If the current position is > new value add col here
        if current > val and i < length:
            added = True
            sorted_dtfm.insert(i, col, [val, col])
        # If we are at the end of dtfm add col
        elif length == i:
            added = True
            sorted_dtfm[col] = [val, col]
        # Increment i by one
        i = i+1
    return sorted_dtfm

# Heap sort algorithm


"""
CALL: heapsort(dtfm)

INPUTS:
    dtfm: Dataframe to sort
    by: row to sort by
    num: size of the heap to store

RETURNS: sorted dtfm

DESCRIPTION: heap_sort should return a dtfm of set size containing sorted values.
"""
def heapsort(dtfm, num, by="column", add_to_heap=add_to_heap):
    heap = []
    col_dtfm = pd.DataFrame()
    sorted_dtfm = pd.DataFrame()
    sorted_min = 0
    # Start running through the dataframe and adding values to the heap as I go
    for i in range(dtfm.size):
        col = dtfm.columns[i]
        val = dtfm.iloc[0,i]

        if val > sorted_min or sorted_dtfm.shape[1] < num:
            sorted_dtfm = add_to_heap(sorted_dtfm, col, val, num)
            sorted_min = sorted_dtfm.iloc[0,0]

    return sorted_dtfm


