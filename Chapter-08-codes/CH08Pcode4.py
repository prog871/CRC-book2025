#This code plots the CDF
#for normal distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# Parameters
mu=30  #Mean (MPa)
sigma=3  #Standard dev. (MPa)
x=25 #Strength to check (MPa)
z = (x - mu) / sigma
probab = norm.cdf(z)
# Display probability
print(f'The probability that \
compressive strength is less than\
25 MPa = {probab:.4f}')
# Create figure
fig,axes=plt.subplots(1,2,figsize=(12,6))
# Plot PDF with shaded region
x_vals=np.linspace(mu - 4 * sigma,\
    mu + 4 * sigma, 1000)
pdf_vals=norm.pdf(x_vals,mu,sigma)
axes[0].plot(x_vals, \
  pdf_vals,'k',linewidth=2)
axes[0].grid(True)
# Shade area to left of x = 25
x_fill=np.linspace(mu-4*sigma,x,100)
y_fill=norm.pdf(x_fill,mu,sigma)
axes[0].fill_between(x_fill,\
  y_fill,color='r',alpha=0.3)
# A vertical dashed line at x=25
axes[0].axvline(x,color='k',\
   linestyle='--',linewidth=2)
# Formatting
axes[0].set_ylim([0, 0.14])
axes[0].set_xlabel('Strength (MPa)')
axes[0].set_ylabel('Probab. Density')
axes[0].tick_params(axis='both',\
            labelsize=14)
# plot CDF with reference lines
cdf_vals=norm.cdf((x_vals-mu)/sigma)
axes[1].plot(x_vals,cdf_vals,\
    'k',linewidth=2)
axes[1].grid(True)
# Add dashed reference lines
axes[1].axvline(x, color='k',\
  linestyle='--', linewidth=2)
axes[1].axhline(probab,xmin=0,\
xmax=(x-(mu-4*sigma))/(8*sigma),\
color='k',linestyle='--',linewidth=2)
# Formatting
axes[1].set_ylim([0, 1.05])
axes[1].set_xlabel('Strength (MPa)')
axes[1].set_ylabel('Cumulative Probab.')
axes[1].tick_params(axis='both',labelsize=14)
plt.tight_layout()
plt.show()
