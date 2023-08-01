import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# csv dosyasındaki verileri yükle
df = pd.read_csv("dataminingodev.csv", header=0, sep=",")

def plot_regression(df, x_col, y_col):
    # Boş değerleri çıkar
    df.dropna(inplace=True)
    
    # x ve y değişkenlerini belirle
    x = df[x_col]
    y = df[y_col]
    
    # Lineer regresyon analizi yap ve eğim ve kesme noktası değerlerini elde et
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    print(f"{x_col}-{y_col} Slope İntercept: {slope:.4f}, {intercept:.4f}")
    
    # Grafik çizimi
    plt.plot(x, y, '.', label='Veri Noktaları')
    plt.plot(x, slope * x + intercept, '-', label='Lineer Regresyon',color="black")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{x_col}-{y_col} İlişkisi")
    plt.grid()
    plt.legend()
    plt.show()

# Sütun çiftleri için lineer regresyon analizi yap ve grafiği çizdir
sütun_çiftleri = [('totalBedrooms', 'population'),
                ('totalBedrooms', 'households'),
                ('population', 'households'),
                ('medianIncome', 'medianHouseValue')]

for col_pair in sütun_çiftleri:
    plot_regression(df, col_pair[0], col_pair[1])
    
plt.show()
