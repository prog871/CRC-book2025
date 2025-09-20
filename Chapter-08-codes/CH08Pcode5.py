#This code plots the PDF 
#and CDF for a dam problem
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# Step 1: Input the sample data
data=np.array([450,620,700,350,480,\
520,550,600,730,400,530,610,580,\
490,720,510,650,470,380,560,640,\
390,460,590,710,370,540,500,620,\
670,510,680,420,570,630,460,\
690,580,410,530])
mu = np.mean(data)  # Mean
sigma=np.std(data,ddof=1)  #St dev
# Step 3: Define flood threshold
flood1=700  #Flood threshold (m3/s)
# Step 4: Flood risk probability
z_flood=(flood1-mu)/sigma  #z-score
p_flood=1-norm.cdf(z_flood) #P(X>700)
flood_prcnt = p_flood * 100
cdf_at_700=norm.cdf(z_flood) #CDF@700
# Step 5: Display results
print(f"Mean ={mu:.2f} m3/s")
print(f"St Dev={sigma:.2f} m3/s")
print(f"Flood Risk (P(X>700))=\
{flood_prcnt:.2f}%")
# Define x values for plotting
x=np.linspace(mu-4*sigma,mu+4*sigma,500)
# Compute PDF and CDF
pdf = norm.pdf(x, mu, sigma)
cdf = norm.cdf(x, mu, sigma)
# Subplot 1: Plot PDF
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(x,pdf,'k-',linewidth=2.5)
plt.fill_between(x,pdf,where=\
(x >=flood1), color='m', 
alpha=0.3,label=f'P(X>700)=\
{flood_prcnt:.2f}%')
plt.axvline(flood1,color='b',\
linestyle='--',linewidth=2)
plt.ylim([0, 0.0041])
plt.grid(True, linewidth=1.5)
# Subplot 2: Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf, 'k-', linewidth=2.5)
plt.axvline(flood1,color='b',\
linestyle='--',linewidth=2)
plt.axhline(cdf_at_700,xmin=0,xmax=flood1,\
color='b',linestyle='--',linewidth=2)
plt.ylim([0, 1.05])
plt.grid(True, linewidth=1.5)
# Show plots
plt.tight_layout()
plt.show()
# End of Python code.
