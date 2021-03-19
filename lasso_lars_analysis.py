import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import models
dt = pd.read_csv("model_simulated_data.csv", index_col=0)
dt = dt.replace(0., np.nan)
dt = dt.count()

# Plot Frequency of selection of SNPs to illustrate which info we will be focussing on
plt.figure();
color_arr = ['#F50C0C']
color_arr = np.append(color_arr, '#0C0CF5')
n, bins, patches = plt.hist(dt, range=(1,25))
patches[0].set_fc("red")
plt.ylabel("Number of SNPs")
plt.xlabel("Frequency of selection for Lasso")
plt.savefig("Frequency of SNP selection original")

# import models
dt = pd.read_csv("model_simulated_epistatic_data.csv", index_col=0)
dt = dt.replace(0., np.nan)
dt = dt.count()

# Plot Frequency of selection of SNPs to illustrate which info we will be focussing on
plt.figure();
color_arr = ['#F50C0C']
color_arr = np.append(color_arr, '#0C0CF5')
n, bins, patches = plt.hist(dt, range=(1,25))
patches[0].set_fc("red")
plt.ylabel("Number of SNPs")
plt.xlabel("Frequency of selection for Lasso")
plt.savefig("Frequency of SNP selection original epistatic")

# import models
dt = pd.read_csv("model_convoluted_data.csv", index_col=0)
dt = dt.replace(0., np.nan)
dt = dt.count()

# Add colour to help track the movement of samples
dt_conv = dt.filter(regex='^SNP_\d{1,3}_SNP_\d{1,3}')
dt_orig = dt.drop(labels=dt_conv.index)


# Plot Frequency of selection of SNPs to illustrate which info we will be focussing on
plt.figure();
color_arr = ['#F50C0C']
color_arr = np.append(color_arr, '#0C0CF5')
n, bins, patches = plt.hist((dt_orig, dt_conv), range=(1,25), stacked=True, label=["Original SNPs", "Convoluted SNPs"])
plt.ylabel("Number of SNPs")
plt.xlabel("Frequency of selection for Lasso")
plt.legend()
plt.savefig("Frequency of SNP selection convoluted")

# import models
dt = pd.read_csv("model_convoluted_epistatic_data.csv", index_col=0)
dt = dt.replace(0., np.nan)
dt = dt.count()

# Add colour to help track the movement of samples
dt_conv = dt.filter(regex='^SNP_\d{1,3}_SNP_\d{1,3}')
dt_orig = dt.drop(labels=dt_conv.index)


# Plot Frequency of selection of SNPs to illustrate which info we will be focussing on
plt.figure();
color_arr = ['#F50C0C']
color_arr = np.append(color_arr, '#0C0CF5')
n, bins, patches = plt.hist((dt_orig, dt_conv), range=(1,25), stacked=True, label=["Original SNPs", "Convoluted SNPs"])
plt.ylabel("Number of SNPs")
plt.xlabel("Frequency of selection for Lasso")
plt.legend()
plt.savefig("Frequency of SNP selection epistatic convoluted")

