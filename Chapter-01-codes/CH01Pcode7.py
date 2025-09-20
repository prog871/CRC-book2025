# Python script to plot a bar chart
# of materials for beach nourishment
import matplotlib.pyplot as plt
# Define materials and volumes
mat = [
    'Sand', 'Gravel', 'Shells', 
    'Silt', 'Rock', 'Clay', 
    'Geotextiles'
]
vol = [70,20,35,74,62,25,66]#Volumes(m^3)
# Create a bar chart
plt.figure()  #Open a new figure
plt.bar(mat, vol, color='b')#Blue color
plt.xlabel('Materials', fontsize=30)
plt.ylabel('Volume (m^3)', fontsize=30)
plt.xticks(fontsize=25)  # Set fontsize
plt.yticks(fontsize=25)
plt.grid(True)  # Add grids 
plt.ylim([0, 90])# Limit of y-axis
plt.gca().spines['top'].set_linewidth(2.0)  
plt.gca().spines['right'].set_linewidth(2.0)  
plt.gca().spines['left'].set_linewidth(2.0)  
plt.gca().spines['bottom'].set_linewidth(2.0)  
# Show the plot
plt.tight_layout()  #Adjust layout to fit 
plt.show()
# End of Python code.
