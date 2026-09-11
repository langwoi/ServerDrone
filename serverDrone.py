import random
import socket
import time
import csv


ip='127.0.0.1'
port = 9000

serverDrone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverDrone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

serverDrone.bind((ip,port))
serverDrone.listen(1)

try:
    while True:
        print(f"GCS Menunggu Koneksi...... {ip}:{port}")
        conn,addr = serverDrone.accept()
        print(f"Terhubung Dengan IP : {addr}")
        try:
            baterai = 100
            while True:
                baterai -=1
                if baterai <= 0:
                    print(f"Baterai Anda Habis, Memutuskan Koneksi.......")
                    break
                elif baterai <= 10:
                    print(f"Baterai Anda Tersisa {baterai} % Waspada!")

                alt = round(random.uniform(0.0,900.00),2)
                pressure = round(random.uniform(0.0,500.00),2)
                temp = round(random.uniform(0.0,90.0),2)

                if alt >700.00:
                    alt_display = "ERORRR"
                else:
                    alt_display = alt
                if pressure > 400.00:
                    pressure_display = "ERORRRR"    
                else:
                    pressure_display = pressure

                telemetryData = f"ALT : {alt_display} | PRESSURE : {pressure_display} | TEMP : {temp} | BATERAI : {baterai}\n"
                conn.send(telemetryData.encode('utf-8'))
                print(f"Mengirim Data Drone {telemetryData.strip()}")
                time.sleep(0.5)

        except(ConnectionError,ConnectionAbortedError,BrokenPipeError):
            print(f"CLient {addr}")
        finally:
            conn.close()
except KeyboardInterrupt:
    print("\nServer Telah Terhenti Manual")
finally:
    serverDrone.close()
    print("Server Telah Dimatikan")
                
