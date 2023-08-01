import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("dataminingodev.csv",header=0, sep=",")

df.plot(x="medianIncome",y="medianHouseValue",linestyle="none",kind="line",linewidth = '0.5',marker="x")

#Max_Pulse= df["medianIncome"]

#percentile10 = np.percentile(Max_Pulse, 10)

#print(percentile10)



def func(slope):
    #a3=slope[2]
    a2=slope[1]
    a1=slope[0]
    x = np.arange(-1, 20, 0.3)
    y = a1*x + a2
    
    plt.plot(x, y)
    plt.grid()
    plt.show()
    
#temizlik için dropna
df.dropna(inplace=True)

#title başlığını düzeltir grafiğin
plt.title("medianIncome ve medianHouseValue Tablosu")
#xlabel x ekseninin adını
plt.xlabel("medianIncome")
#ylabel y ekseninin adını gösterir
plt.ylabel("medianHouseValue")


x = df['medianIncome']
y = df['medianHouseValue']
#burda denklem bulmak için
slope_intercept = np.polyfit(x,y,1)
print(slope_intercept)
func(slope_intercept)