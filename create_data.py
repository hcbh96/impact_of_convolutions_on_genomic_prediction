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
model_epistatic = pd.read_csv('model_epistatic.csv', index_col=0)

simulated_dataset = []
epistatic_dataset = []
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

# Create a a matrix of inputs and generate outputs
bar = Bar('Processing...', max=n_samples)
for i in range(n_samples):
    temp_model = model_epistatic.copy()
    # Create sample
    split = rand.randrange(temp_model.shape[1])
    # rand var inputs 0 or 1
    inputs = np.ones(temp_model.shape[1])
    split = rand.randrange(temp_model.shape[1])
    inputs[:split] = 0
    rand.shuffle(inputs)

    temp_model.loc[3] = np.ones(temp_model.shape[1])
    # Calc many to one epistatic multiplications and add them to model
    #for j in range(model_epistatic.shape[1]):
        # Add multipliers together for each row and then save mul sum
     #   multiplier = 1
     #   current_snp = model_epistatic.columns[j]
     #   for k in range(model_epistatic.shape[1]):
     #       to_include = inputs[k]
     #       snp = model_epistatic.iloc[2,k]
     #       if snp == current_snp and to_include == 1:
     #           multiplier = multiplier + float(model_epistatic.iloc[1,k])
     #       bar.next()
     #   model_epistatic.iloc[3,j] = multiplier
     #   bar.next()
    # bar.next()
    for j in range(model_epistatic.shape[1]):
        if inputs[j] == 1:
            snp = temp_model.iloc[2,j]
            mul = temp_model.iloc[1,j]
            temp_model.loc[3,snp] = temp_model.loc[3,snp] + float(mul)

    # replace original with orig * multiplier
    originals = temp_model.iloc[0,:].to_numpy().astype(np.float)
    multipliers = temp_model.iloc[3,:].to_numpy().astype(np.float)

    temp_model.iloc[0,:] = np.multiply(originals, np.transpose(multipliers))

    # Calc output + noise to output
    effects_arr = temp_model.iloc[0,:].to_numpy().astype(np.float)
    output = np.dot(effects_arr, np.transpose(inputs))

    output = output + rand.gauss(mu_noise, sigma_noise)
    inputs = np.append(inputs,output)
    epistatic_dataset.append(inputs)
    bar.next()
bar.finish()

columns = model.columns
columns = np.append(columns, 'phenotype')
epistatic_dtfm = pd.DataFrame(data=epistatic_dataset, columns=columns)
epistatic_dtfm.to_csv('simulated_epistatic_data.csv')
