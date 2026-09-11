import pandas as pd
import datetime

df = pd.read_csv(r"C:\Users\User\Documents\BERKAS PENTING\EEPISATLATIAN\python\Telemetry_Drone 1.csv")
tinggiRoket=df['Altitude'] > 500.00
temp=df['Pressure'] < 500.00
rataKetinggian=df.groupby('Pressure')['Altitude'].mean()
print(rataKetinggian)