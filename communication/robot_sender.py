import socket
import json

class RobotSender:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_command(self, command):
        message = json.dumps(command).encode('utf-8')
        self.socket.sendto(message, (self.ip, self.port))

    def close(self):
        self.socket.close()