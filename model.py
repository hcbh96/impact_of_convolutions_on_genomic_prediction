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


# Create episttic model with two fold dynamics

effects_1 = np.ones(length)
effects_2_size = np.ones(length)
effects_2_position = [None] * length
labels = [None] * length
for i in range(len(effects)):
    effects_1[i] = abs(rand.gauss(mu, sigma))
    # Additive effects twice as important as epistatic
    effects_2_size[i] = rand.gauss(mu, sigma/20)
    pos = int(np.round_(np.mod(rand.gauss(i, len(effects)/10), length-1)))
    effects_2_position[i] = 'SNP_{}'.format(pos)
    labels[i] = "SNP_{}".format(str(i))

# For each trait create between 0 and 10 epistatic interactions
epistatic_model_dtfm = pd.DataFrame(data=[effects_1, effects_2_size, effects_2_position], columns=labels)
epistatic_model_dtfm.to_csv("model_epistatic.csv")

