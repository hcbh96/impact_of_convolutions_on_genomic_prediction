import pytest
import pandas as pd
from heapsort import heapsort,add_to_heap
# File to for tests relating to correct_params.py

def test_heap_sort_exists():
    assert heapsort

def test_add_to_heap():
    # Arrange
    sorted_in = pd.DataFrame(data=[[1, 202, 31, 22], ["S1", "S202", "S31", "S22"]], columns = ["S1", "S202", "S31", "S22"])
    col_in = "S2"
    val_in = 2
    num = 4
    # Act
    sorted_out = add_to_heap(sorted_in, col_in, val_in, num)
    # Assert
    assert sorted_out.iloc[0,0] == 2
    assert sorted_out.shape[1] == 4
    assert sorted_out.columns[0] == 'S2'




