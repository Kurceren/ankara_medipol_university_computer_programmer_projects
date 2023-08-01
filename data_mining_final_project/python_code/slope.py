import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data from the CSV file
df = pd.read_csv("dataminingodev.csv", header=0, sep=",")

def func(slope):
    #a3=slope[2]
    a2=slope[1]
    a1=slope[0]
    x = np.arange(-130, -110, 0.3)
    y = a1*x + a2
    
    plt.plot(x, y)
    plt.grid()
    

# Define column pairs
column_pairs = [('longitude', 'latitude'),
                ('totalRooms', 'totalBedrooms'),
                ('totalRooms', 'population'),
                ('totalRooms', 'households'),
                ('totalBedrooms', 'population'),
                ('totalBedrooms', 'households'),
                ('population', 'households'),
                ('medianIncome', 'medianHouseValue')]

# Find slope and intercept values for each column pair
print("\n")
print("\n")
for pair_1,pair_2 in column_pairs:
    xx = df[pair_1]
    yy = df[pair_2]
    
    
    df.plot(xx,yy,linestyle="none",kind="line",linewidth = '0.5')
    plt.grid()
    plt.show()
    

func(slope)   
print("\n")