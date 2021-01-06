# Asses which model selects average parameters of higher importance
import pandas as pd
from sklearn import preprocessing

# Import datasets
actual_model = pd.read_csv("model.csv", index_col=0)
original_model = pd.read_csv("model_simulated_data.csv", index_col=0)
convoluted_model = pd.read_csv("model_convoluted_data.csv", index_col=0)

# Assess models vs actual
print(actual_model)
print(original_model.sum())
print(convoluted_model.sum())

