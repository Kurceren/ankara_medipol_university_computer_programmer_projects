import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("dataminingodev.csv",header=0, sep=",")

df.plot(x="totalRooms",y="totalBedrooms",linestyle="solid",kind="line",linewidth = '0.5',marker="x")

#Max_Pulse= df["totalRooms"]

#percentile10 = np.percentile(Max_Pulse, 10)

#print(percentile10)



def func(slope):
    #a3=slope[2]
    a2=slope[1]
    a1=slope[0]
    x = np.arange(-1300, 40000, 0.3)
    y = a1*x + a2
    
    plt.plot(x, y)
    plt.grid()
    plt.show()
    
#temizlik için dropna
df.dropna(inplace=True)

#title başlığını düzeltir grafiğin
plt.title("totalRooms ve totalBedrooms Tablosu")
#xlabel x ekseninin adını
plt.xlabel("totalRooms")
#ylabel y ekseninin adını gösterir
plt.ylabel("totalBedrooms")


x = df['totalRooms']
y = df['totalBedrooms']
#burda denklem bulmak için
slope_intercept = np.polyfit(x,y,1)
print(slope_intercept)
func(slope_intercept)