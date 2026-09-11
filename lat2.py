import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Telemetry_Drone2.csv')
df.columns = [col.strip() for col in df.columns]
df['timestamp'] = pd.to_datetime(df['timestamp'])

print("Dokumentasi TroubleShooting")
erorrs = df[df['status'] != 'oke']
for _, row in erorrs.iterrows():
    print(f"[{row['timestamp']}] Alert :  {row['status']} | Temp: {row['temperature']} | Pressure: {row['pressure']}")

df.loc[
    (df['temperature'] < -50) | (df['temperature'] > 80), 'temperature'
] = np.nan

df['temperature_clean'] = df['temperature'].interpolate(method='linear')
df['pressure_clean'] = df['pressure'].interpolate(method='linear')

plt.figure(figsize=(12,6))
plt.subplot(2,1,1)

plt.plot(
    df['timestamp'],
    df['temperature_clean'],
    color = 'blue',
    linestyle = '--',
    marker = 'o',
    label = 'Temp(Cleaned)',
)
plt.title('Telemetry Analysis Device')
plt.ylabel('Temperature(C)')
plt.legend()
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(
    df['timestamp'],
    df['pressure_clean'],
    color = 'green',
    linestyle = '--',
    marker = 'o',
    label = 'Pressure Clean',
)
plt.xlabel('TimeStamp')
plt.ylabel('Pressure (Clean)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()