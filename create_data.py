import pandas as pd
import random as rand
import numpy as np
from progress.bar import Bar
# Set seed
SEED = 500; rand.seed(SEED)
mu_noise = 0
sigma_noise = 100
n_samples = 200 # number of members of the population to generate

# Generate a dataset from the model with gaussian random inputs and the addition of noise drawn randomly from a gaussian distribution applied to the output
model = pd.read_csv('model.csv', index_col=0)

simulated_dataset = []

# Create a matrix of inputs and generate outputs using the model on each output add an element of noise to the output
bar = Bar('Processing...', max=n_samples)
for i in range(n_samples):
    # Create sample
    split = rand.randrange(model.size)
    # rand var inputs 0 or 1
    inputs = np.ones(model.size)
    split = rand.randrange(model.size)
    inputs[:split] = 0
    rand.shuffle(inputs)

    # Calc output + noise to output
    output = np.dot(model.loc[0,:].to_numpy(), np.transpose(inputs))
    output = output + rand.gauss(mu_noise, sigma_noise)
    inputs = np.append(inputs,output)
    simulated_dataset.append(inputs)
    bar.next()
bar.finish()



columns = model.columns
columns = np.append(columns, 'phenotype')
simulated_dtfm = pd.DataFrame(data=simulated_dataset, columns=columns)
simulated_dtfm.to_csv('simulated_data.csv')
