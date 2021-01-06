import numpy as np
import random as rand
import csv
import pandas as pd
# Set a seed for reproducibility
SEED = 500; rand.seed(SEED)
mu = 0
sigma = 1
length = 1000 # Number of params affecting model 50,000 SNP chip


# Create linear model with parameter weights drawn randomly from a gaussian distribution
effects = np.ones(length)
labels = [None] * length
for i in range(len(effects)):
    effects[i] = abs(rand.gauss(mu, sigma))
    labels[i] = "SNP_{}".format(str(i))

# Save the model
model_dtfm = pd.DataFrame(data=[effects], columns=labels)
model_dtfm.to_csv("model.csv")




