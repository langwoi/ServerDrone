import socket

class TelemetryReceiver:
    def __init__(self,host:str,port:int):
        self.host = host
        self.port = port
        self.client = None
    def connected(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((self.host,self.port))
        print("Terhubung Ke {self.port}")
    def receiveData(self,buffer_size : int = 1024)->str:
        if not self.client:
            raise ConnectionError("Belum Terhubung Ke Server")
        return self.client.recv(buffer_size).decode('utf-8')
    def disconect(self):
        if self.client:
            self.client.close()
            print("Koneksi Terputus")

receiver = TelemetryReceiver('localhost',8080)
receiver.connected()

try:
    while True:
        data = receiver.receiveData()
        if not data:
            break
        print("Data Ditrima :",data.strip())
except KeyboardInterrupt:
    print("\nMenerima Data Dihentikan manual")
finally:
    receiver.disconect