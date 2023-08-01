import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

df = pd.read_csv("dataminingodev.csv", header=0, sep=",")
print(df.describe())
'''
for col in df.columns:
    
    if col=="longitude":
        x=1
    else:
        
            print("Statistics for column: ",col)
            h_mean = statistics.harmonic_mean(df[col])
            print("statistics.harmonic_mean: ", h_mean)
            h_mean = statistics.mean(df[col])
            print("statistics.mean: ", h_mean)
            h_mean = statistics.median(df[col])
            print("statistics.median: ", h_mean)
            h_mean = statistics.median_grouped(df[col])
            print("statistics.median_grouped: ", h_mean)
            h_mean = statistics.median_high(df[col])
            print("statistics.median_high: ", h_mean)
            h_mean = statistics.median_low(df[col])
            print("statistics.median_low: ", h_mean)
            h_mean = statistics.mode(df[col])
            print("statistics.mode: ", h_mean)
            h_mean = statistics.pstdev(df[col])
            print("statistics.pstdev: ", h_mean)
            h_mean = statistics.stdev(df[col])
            print("statistics.stdev: ", h_mean)
            h_mean = statistics.pvariance(df[col])
            print("statistics.pvariance: ", h_mean)
            h_mean = statistics.variance(df[col])
            print("statistics.variance: ", h_mean)
            print("\n")
'''
        
        
    
    
'''
#kaç satır ve sürunla başladığıma baktım
rowsayisi=df.shape[0]
columsayisi=df.shape[1]
print("satır sayısı= ",rowsayisi)
print("sütun sayısı= ",columsayisi)

#sütunların türüne baktım değiştirmedim
print(df.info())

#aynı olan verileri sildim
df.drop_duplicates(inplace=True)

#kaç tane aynı veri olduğuna baktım
print(df.shape)

#boş olan verileri sildim
df.dropna(axis=0,inplace=True)
print("\n")
print("\n",df.describe)

#kaç satır silindiğini bulmak için baktım
print(df.shape)

#istatistiksel metodlar



#tüm özet işlemleri yazdırdım
print("\n")
print(df.describe())
print("\n")

#veri tipini düzenleme
df["longitude"]=df["longitude"].astype(float)
df["latitude"]=df["latitude"].astype(float)
df["housingMedianAge"]=df["housingMedianAge"].astype(float)
df["totalRooms"]=df["totalRooms"].astype(float)
df["totalBedrooms"]=df["totalBedrooms"].astype(float)
df["population"]=df["population"].astype(float)
df["households"]=df["households"].astype(float)
df["medianIncome"]=df["medianIncome"].astype(float)
df["medianHouseValue"]=df["medianHouseValue"].astype(float)


#Korelasyon(Corr) alma işlemi
print("\n")
print("\n")

print("1)Sadece Corr ile yapılan: \n",df.corr(),"\n")

df1=df.corr(method='kendall',numeric_only=True)
print('2)Kendall ile yapılan: \n',df1,"\n")

df1=df.corr(method='pearson',numeric_only=True)
print('3)Pearson ile yapılan: \n',df1,"\n")

df1=df.corr(method='spearman',numeric_only=True)
print('4)Spearman ile yapılan: \n',df1,"\n")
print("\n")

'''