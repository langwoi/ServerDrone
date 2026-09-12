import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\User\Documents\BERKAS PENTING\EEPISATLATIAN\python\Telemetry_Drone 1.csv")
df.columns = [col.strip().lower() for col in df.columns]

# 1. Konversi ke timestamp & hapus data invalid (NaT)
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms', errors='coerce')
df = df.dropna(subset=['timestamp'])

# 2. PERBAIKAN: Timpa ke 'df' langsung agar data yang di-plot terurut
df = df.sort_values(by='timestamp')

df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
df['pressure'] = pd.to_numeric(df['pressure'], errors='coerce')

df.loc[
    (df['temperature'] < -50) | (df['temperature'] > 80), 'temperature'
] = np.nan

df['temperature_clean'] = df['temperature'].interpolate(method='linear').bfill().ffill()
df['pressure_clean'] = df['pressure'].interpolate(method='linear').bfill().ffill()

plt.figure(figsize=(12, 6))

# Plot Suhu
plt.subplot(2, 1, 1)
plt.plot(
    df['timestamp'],  # Menggunakan df yang sudah di-sort
    df['temperature_clean'],
    color='blue',
    linestyle='--',
    marker='o',
    label='Temp(Cleaned)',
)
plt.title('Telemetry Analysis Device')
plt.ylabel('Temperature (C)')
plt.legend()
plt.grid(True)

# Plot Tekanan
plt.subplot(2, 1, 2)
plt.plot(
    df['timestamp'],  # Menggunakan df yang sudah di-sort
    df['pressure_clean'],
    color='green',
    linestyle='--',
    marker='o',
    label='Pressure Clean',
)
plt.xlabel('Timestamp')
plt.ylabel('Pressure (Clean)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
