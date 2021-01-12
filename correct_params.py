# Asses which model selects average parameters of higher importance
import pandas as pd
from sklearn import preprocessing
import numpy as np
from heapq import heappop, heappush
from heapsort import heapsort
import re
import matplotlib.pyplot as plt
# Import datasets
actual_model = pd.read_csv("model.csv", index_col=0)
original_model = pd.read_csv("model_simulated_data.csv", index_col=0)
convoluted_model = pd.read_csv("model_convoluted_data.csv", index_col=0)

# Assess models vs actual
original_model = original_model.sum()
convoluted_model = convoluted_model.sum()

# Find length of the original and convoluted model
original_model = original_model.replace(0, np.nan)
original_model = original_model.dropna()
convoluted_model = convoluted_model.replace(0, np.nan)
convoluted_model = convoluted_model.dropna()

l_original = np.size(original_model)
l_convoluted = np.size(convoluted_model)

# Order actual model by most to least important using heap sorting alg
actual_model = heapsort(actual_model, l_original)

# Get col titles from actual model
actual_columns = actual_model.columns

# Scan first n from trained models assess how many keys there exist in set
original_columns = original_model.index
convoluted_columns = convoluted_model.index

# Change convoluted columns into a separated array
n_conv = pd.Index(data = [])
for i in convoluted_columns.values:
    n_conv = n_conv.append(pd.Index(data=re.split('(?<=\d)_',i)))
convoluted_columns = n_conv

# Count the number of columns caught in the original columns
original_causal = []
convoluted_causal = []
shared_causal = []
na_causal = []
for i in actual_columns.values:
    orig_bool = False
    conv_bool = False
    if i in original_columns.values:
        orig_bool = True
        original_causal = np.append(original_causal, i)
    if i in convoluted_columns.values:
        conv_bool = True
        convoluted_causal = np.append(convoluted_causal , i)
    if conv_bool and orig_bool:
        shared_causal = np.append(shared_causal, i)
    if not conv_bool and not orig_bool:
        na_causal = np.append(na_causal, i)


print("Original Length: ", original_columns.size)
print("Convoluted Length: ", convoluted_columns.size)

print("Original Count: ", original_causal.size)
print("Convolouted Count: ", convoluted_causal.size)

print("Ratio length conv/orig: ", convoluted_causal.size/original_causal.size)
print("Ration Causal Loci found conv/orig: ", convoluted_columns.size/original_columns.size)

original_causal_dtfm = pd.DataFrame(columns=original_causal)
for i in original_causal:
    original_causal_dtfm[i] = [actual_model[i][0]]

convoluted_causal_dtfm = pd.DataFrame(columns=convoluted_causal)
for i in convoluted_causal:
    convoluted_causal_dtfm[i] = [actual_model[i][0]]

shared_causal_dtfm = pd.DataFrame(columns=shared_causal)
for i in shared_causal:
    shared_causal_dtfm[i] = [actual_model[i][0]]

na_causal_dtfm = pd.DataFrame(columns=na_causal)
for i in na_causal:
    na_causal_dtfm[i] = [actual_model[i][0]]


print("Original Causal Dtfm: ", original_causal_dtfm)
print("Convoluted Causal Dtfm: ", convoluted_causal_dtfm)
print("Shared Causal Dtfm: ", shared_causal_dtfm)
print("Not Available Causal Dtfm: ", convoluted_causal_dtfm)


print("Original Causal Info: ", original_causal_dtfm.transpose().describe())
print("Convoluted Causal Info: ", convoluted_causal_dtfm.transpose().describe())
print("Shared Causal Info: ", shared_causal_dtfm.transpose().describe())
print("Not Available Causal Info: ", na_causal_dtfm.transpose().describe())

combined_dtfm = pd.DataFrame(data = { "Original": original_causal_dtfm.iloc[0], "Convoluted": convoluted_causal_dtfm.iloc[0], "shared":shared_causal_dtfm.iloc[0], "Not selected": na_causal_dtfm.iloc[0]})

print(combined_dtfm.iloc[:,0].dropna())

fig = plt.figure()
plt.boxplot([original_causal_dtfm.iloc[0],  convoluted_causal_dtfm.iloc[0], shared_causal_dtfm.iloc[0], na_causal_dtfm.iloc[0]], labels=("Original","Convoluted","Shared","Not selected"))
plt.ylabel("Weight of parameter")
plt.savefig("Comparative Boxplot.png")
