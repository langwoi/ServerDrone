import socket
import random
import time

host = '127.0.0.1'
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind((host,port))
server.listen(1)


try:
    while True:
        print("Server Jalan {host}:{port}",host,port)
        conn,addr = server.accept()
        print(f"Terhubung Dengan Client : {addr}")

        try:
            alt = 0
            while True:
                alt +=10
                temp = round(random.uniform(25.0,30.0),2)
                pressure = round(random.uniform(1.000,8.000),3)
                telemetry_Data = f"ALT : {alt} | TEMP : {temp} | PRESSURE:{pressure}\n"
                conn.send(telemetry_Data.encode('utf-8'))
                print(f"Mengirim Data {telemetry_Data.strip()}")
                time.sleep(3)
        except(ConnectionError,ConnectionAbortedError,BrokenPipeError):
            print(f"Client {addr}")
        finally:
            conn.close()
except KeyboardInterrupt:
    print("\nServer Dihentikan Manual Oleh User CTRL C  ")
finally:
    server.close()
    print("Server Berhenti Total")

