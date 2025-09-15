import socket
import threading

class Server:
    def __init__(self, port):
        self.port = port
        self.server = None
        self.conn = None
        self.addr = None

    def start(self, on_receive):
        def server_thread():
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(('0.0.0.0', self.port))
            self.server.listen(1)
            self.conn, self.addr = self.server.accept()
            self.receive(on_receive)
        threading.Thread(target=server_thread, daemon=True).start()

    def receive(self, on_receive):
        while True:
            try:
                data = self.conn.recv(1024).decode('utf-8')
                if data:
                    on_receive(data)
            except Exception as e:
                print("Server receive error:", e)
                break

    def send(self, data):
        try:
            self.conn.sendall(data.encode('utf-8'))
        except Exception as e:
            print("Server send error:", e)

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = None

    def start(self, on_receive):
        def client_thread():
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.host, self.port))
            self.receive(on_receive)
        threading.Thread(target=client_thread, daemon=True).start()

    def receive(self, on_receive):
        while True:
            try:
                data = self.client.recv(1024).decode('utf-8')
                if data:
                    on_receive(data)
            except Exception as e:
                print("Client receive error:", e)
                break

    def send(self, data):
        try:
            self.client.sendall(data.encode('utf-8'))
        except Exception as e:
            print("Client send error:", e)
