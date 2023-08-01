import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("dataminingodev.csv",header=0, sep=",")

print(df.corr())