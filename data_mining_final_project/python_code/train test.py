import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("dataminingodev.csv", header=0, sep=",")

sütun_çiftleri = [('longitude', 'latitude'),
                ('totalRooms', 'totalBedrooms'),
                ('totalRooms', 'population'),
                ('totalRooms', 'households'),
                ('totalBedrooms', 'population'),
                ('totalBedrooms', 'households'),
                ('population', 'households'),
                ('medianIncome', 'medianHouseValue')]


for sütun_1, sütun_2 in sütun_çiftleri:
    x = df[[sütun_1]]
    y = df[sütun_2]
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)
   
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    
    
    y_pred = lr.predict(x_test)
    

    r2 = r2_score(y_test, y_pred)
    
    print(f"{sütun_1}-{sütun_2} R2 değeri: {r2}")
    
    plt.plot(x_test, y_test, color='blue',marker='.',linestyle="solid")
    plt.plot(x_test, y_pred, color='red', linewidth=3)
    plt.xlabel(sütun_1)
    plt.ylabel(sütun_2)
    plt.title(f"{sütun_1}-{sütun_2} Linear Regrasyonu Test Train")
    plt.show()
    


