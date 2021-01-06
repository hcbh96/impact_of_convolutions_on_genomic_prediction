# In this folder I want to convolute my data so that from the parameters that did not contribute to the solution I can convolute some of them together to find new useful parameters
import pandas as pd
import numpy as np
from progress.bar import Bar
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoLarsCV
# Import model
lasso_model = pd.read_csv('lasso_lars_model.csv', index_col=0)
simulated_data = pd.read_csv('simulated_data.csv', index_col=0)

# Retrieve SNPs which are never selected for model
zero_columns = []
non_zero_columns = []
bar = Bar('Processing Empty Columns...', max=np.size(lasso_model.columns))
for label, content in lasso_model.items():
    if np.sum(content) == 0:
        zero_columns = np.append(zero_columns,label)
    else:
        non_zero_columns = np.append(non_zero_columns, label)
    bar.next()
bar.finish()

# Convolute the zero dataset
bar = Bar('Creating Convolutions...', max=np.size(zero_columns)/2)
for i in range(0,np.size(zero_columns), 2):
    col1_name = zero_columns[i]
    col2_name = zero_columns[i+1]
    col1 = simulated_data[[col1_name]]
    col2 = simulated_data[[col2_name]]
    new_name = "{}_{}".format(col1_name, col2_name)
    mapping1 = {col1_name: new_name}
    mapping2 = {col2_name: new_name}
    col1 = col1.rename(columns=mapping1)
    col2 = col2.rename(columns=mapping2)
    col1_col2 = col1.mul(col2)
    simulated_data = simulated_data.drop(labels=[col1_name, col2_name], axis='columns')
    simulated_data[new_name] = col1_col2
    bar.next()
bar.finish()

# Save convoluted data to a dataset
simulated_data.to_csv("convoluted_data.csv")



