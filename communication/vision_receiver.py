import socket
import struct
import numpy as np

class VisionReceiver:
    def __init__(self, multicast_group, port):
        self.multicast_group = multicast_group
        self.port = port
        self.sock = self.create_socket()

    def create_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', self.port))
        group = socket.inet_aton(self.multicast_group)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        return sock

    def receive_data(self):
        while True:
            data, address = self.sock.recvfrom(1024)
            self.process_data(data)

    def process_data(self, data):
        # Process the received data (e.g., convert to numpy array)
        # This is a placeholder for actual processing logic
        processed_data = np.frombuffer(data, dtype=np.float32)
        print(f"Received data from {address}: {processed_data}")

if __name__ == "__main__":
    multicast_group = '224.0.0.1'  # Example multicast group
    port = 5000  # Example port
    receiver = VisionReceiver(multicast_group, port)
    receiver.receive_data()