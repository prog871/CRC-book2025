#This Python script, named CH01Pcode5.py, calculates
#time taken to fill Craig Goch reservoir
V = 9.2 * (10**6)  #reservoir volume (m^3)
q = 5  # river discharge (m^3/s)
volume = 0  #reservoir starting volume
time = 0  #Time (seconds)

# while loop for time taken to fill reservoir
while volume < V:
    volume += q  # Add discharge per sec
    time += 1  # Increment time by 1 sec
# Convert time from seconds to days
time_days = time / (60 * 60 * 24)
# Display result
print(time_days)
