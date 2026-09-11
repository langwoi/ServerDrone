import socket
import sys
from datetime import datetime
import csv
import os

class telemetryDrone:
    def __init__(self,ip:str,port:int):
        self.ip = ip
        self.port = port
        self.client = None
    def connect(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            print(f"Menungggu Terhubung Server GCS({self.ip}:{self.port})")
            self.client.connect((self.ip,self.port))
            print(f"Terhubung Ke Server GCS: {self.port}")
        except (ConnectionResetError,ConnectionRefusedError):
            print(f"\n[!] [DRONE ERROR] Gagal terhubung ke GCS!")
            print(f"[!] Server GCS ({self.ip}:{self.port}) belum aktif atau offline.")
            print("[!] Batalkan penerbangan / Nyalakan Server GCS terlebih dahulu.\n")
            sys.exit()
            
    def receiveTelemetry(self,bufferSize:int=1024)->str:
        if not self.client:
            raise ConnectionError("Tidak Dapat Terhubung Server......")
        return self.client.recv(bufferSize).decode('utf-8')
    def disconect(self):
        if self.client:
            self.client.close()
            print("Koneksi Terputus")

receiver = telemetryDrone('127.0.0.1',9000)
receiver.connect()
log_file = None
#waktuNow=datetime.now().strftime('%Y-%M-%D_%H-%M-%S')
ang=1

try:
    fileCek=f'Telemetry_Drone {ang}.csv'
    while os.path.exists(fileCek):
        ang+=1

    log_file = open(fileCek, mode='a', newline='',encoding='utf-8')
    writer= csv.writer(log_file)

    writer.writerow(['Timestamp','Altitude','Pressure','Baterai'])
    log_file.flush()
    while True:
        data = receiver.receiveTelemetry()
        if not data:
            print("\n[!] Koneksi ditutup oleh Drone Server (Baterai Habis / Standby).")
            break
        print(f"Menerima Data Drone  :",data.strip())

        parts=data.strip().split('|')
        alt=parts[0].split(':')[1]
        temp=parts[1].split(':')[1]
        press=parts[2].split(':')[1]
        bat=parts[3].split(':')[1]
        timestamp=datetime.now().strftime("%H:%H:%S")

        writer.writerow([parts,alt,temp,press,bat,timestamp])
        log_file.flush()
except KeyboardInterrupt:
    print("\nServer Terhenti Manual")
finally:
    if log_file:
        log_file.close()
        print("Data Berhasil Disimpan")
    receiver.disconect()