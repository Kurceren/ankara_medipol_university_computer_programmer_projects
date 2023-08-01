
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#Verilerin yüklenmesi
df = pd.read_csv("dataminingodev.csv",header=0, sep=",")
x = df[['longitude']] # x değişkeni bir dizi olarak tanımlanmalı
y = df['latitude']

#Verilerin eğitim-test kümelerine ayrılması
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#Linear regresyon modeli oluşturma ve eğitim
model = LinearRegression()
model.fit(X_train, y_train)

#Test kümesi üzerinde modelin performansının ölçülmesi
y_pred = model.predict(X_test)

#Grafik çizdirme


plt.title('Linear Regresyon')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.show()

#R2 değerinin hesaplanması
r2 = r2_score(y_test, y_pred)


x_train = X_train.sort_index()
y_train = y_train.sort_index()

#Sonuçların yazdırılması
print('Eğitim kümesi R2 değeri:', model.score(X_train, y_train))
print('Test kümesi R2 değeri:', r2)
plt.plot(X_train,y_train)
plt.plot(X_test,y_pred)
plt.show()
