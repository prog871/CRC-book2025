# This Python code calculates stress inside a 
# column and determines if it is safe
A = 2250000  # cross section area (mm^2)
F = 42000 * 1000  # force in N
allow_str = 30  # allowable stress (MPa = N/mm^2)
# Calculations
str = F / A  # calculate stress in MPa
# Display the stress value
print(f'stress = {str}')  #calculated stress
# Check if stress exceeds allowable limit
if str > allow_str:
    print('str > allowable stress; column fails')
else:
    print('str < allowable stress; column is safe')
# End of code.  
