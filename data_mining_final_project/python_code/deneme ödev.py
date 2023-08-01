'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# csv dosyasındaki verileri yükle
df = pd.read_csv("dataminingodev.csv", header=0, sep=",")

# doğrusal regresyon eğimi ve kesme noktası değerlerini hesapla
eğim, kesme_noktası, r_değeri, p_değeri, hata_std = linregress(df['longitude'], df['latitude'])

# grafiği çiz
plt.plot(df['longitude'], df['latitude'], 'o', label='Veriler')
plt.plot(df['longitude'], eğim * df['longitude'] + kesme_noktası, 'r-', linewidth=3.5, label='Doğru')

# grafiği süsleme
plt.xlabel('Boylam')
plt.ylabel('Enlem')
plt.title('Enlem-Boylam İlişkisi')
plt.legend()
plt.grid()
# grafiği göster
plt.show()

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# csv dosyasındaki verileri yükle
df = pd.read_csv("dataminingodev.csv", header=0, sep=",")

# sütun çiftlerini belirle
sütun_çiftleri = [('longitude', 'latitude'),
                  ('totalRooms', 'totalBedrooms'),
                  ('totalRooms', 'population'),
                  ('totalRooms', 'households'),
                  ('totalBedrooms','population'),
                  ('totalBedrooms','households'),
                  ('population','households')
                  ('medianIncome', 'medianHouseValue')]

# her bir sütun çifti için doğrusal regresyon eğimi ve kesme noktası değerlerini hesapla
for sütun_1, sütun_2 in sütun_çiftleri:
    
    
    # grafiği çiz
    plt.plot(df[sütun_1], df[sütun_2], 'o', label='Veriler', color="black", markersize=1.5)
    

    # grafiği süsleme
    plt.xlabel(sütun_1.capitalize())
    plt.ylabel(sütun_2.capitalize())
    plt.title('{}-{} İlişkisi'.format(sütun_1.capitalize(), sütun_2.capitalize()))
    
    #slope_intercept
    xx=df[sütun_1]
    yy=df[sütun_2]
    slope_intercept= np.polyfit(xx,yy,1)
    print(sütun_1,"ve",sütun_2,"slope intercept: ",slope_intercept)
    
    # grafiği göster
    plt.grid()
    plt.show()


'''
def plot_regression(df, x_col, y_col):
    # Boş değerleri çıkar
    df.dropna(inplace=True)
    
    # x ve y değişkenlerini belirle
    x = df[x_col]
    y = df[y_col]
    
    # Lineer regresyon analizi yap ve eğim ve kesme noktası değerlerini elde et
    slope_intercept = np.polyfit(x, y, 1)
    print(f"{x_col}-{y_col} Slope İntercept: {slope_intercept}")
    
    # Grafik çizimi
    x_range = np.arange(df[x_col].min(), df[x_col].max(), 0.3)
    y_range = slope_intercept[0] * x_range + slope_intercept[1]
    
    df.plot(x=x_col,y=y_col, label='Veri Noktaları',marker='.',linestyle="none")
    
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{x_col}-{y_col} İlişkisi")
    plt.grid()
    plt.show()

# Veri setini oku


# Sütun çiftleri için lineer regresyon analizi yap ve grafiği çizdir
sütun_çiftleri = [('longitude', 'latitude'),
                ('totalRooms', 'totalBedrooms'),
                ('totalRooms', 'population'),
                ('totalRooms', 'households'),
                ('totalBedrooms', 'population'),
                ('totalBedrooms', 'households'),
                ('population', 'households'),
                ('medianIncome', 'medianHouseValue')]

for col_pair in sütun_çiftleri:
    plot_regression(df, col_pair[0], col_pair[1])

'''
#1.için fonksiyon hesaplayıcı ve plotting değerini gösteren