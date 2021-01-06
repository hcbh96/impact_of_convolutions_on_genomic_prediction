import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoLarsCV
from progress.bar import Bar
# Import data
simulated_data = pd.read_csv('simulated_data.csv', index_col=0)
convoluted_data = pd.read_csv('convoluted_data.csv', index_col=0)
actual_model = pd.read_csv('model.csv', index_col=0)
score_dtfm = pd.DataFrame()

"""
Evaluate dataset, gets a filename, and reporter dataframes as input and outputs null but updated the passed in arrays
"""
def evaluate_dataset(dataset_name, score_dtfm=score_dtfm, actual_model=actual_model):
    data = pd.read_csv(dataset_name, index_col=0)
    # Loop from here to compare over multiple runs
    score_arr = []
    coef_arr = np.array([])
    input_data = data.drop(labels='phenotype', axis='columns')
    output_data = np.ravel(data[['phenotype']])
    dtfm_coef = pd.DataFrame(columns=input_data.columns)
    bar = Bar('Evaluating dataset: {}...'.format(dataset_name), max=30)
    for i in range(30):
        # Split data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(input_data, output_data, test_size=0.33, random_state=i)
        # Train a ridge regression model using the training set with CV
        model = LassoLarsCV(positive=True).fit(X_train, y_train)
        # Test the model on a testing set - calculate residual squared and save to array
        score = model.score(X_test, y_test)
        score_arr = np.append(score_arr, score)

        dtfm_coef.loc[i] = model.coef_
        #new_coef = pd.DataFrame(data=model.coef_, columns=input_data.columns)
        #dtfm_coef = dtfm_coef.append(new_coef)
        bar.next()
    bar.finish()
    coef_name = "model_{}".format(dataset_name)
    dtfm_coef.to_csv(coef_name)
    score_dtfm[dataset_name] = score_arr


evaluate_dataset('simulated_data.csv', score_dtfm=score_dtfm)
evaluate_dataset('convoluted_data.csv', score_dtfm=score_dtfm)
score_dtfm.to_csv('score_dataset.csv')





