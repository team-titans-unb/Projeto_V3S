import socket
import struct
from vsss.protos import wrapper_pb2 as wr


class VisionReceiver:
    """
    Uma classe dedicada a gerir a conexão com o socket de visão VSSS.
    Encapsula a inicialização e a recepção de pacotes de visão.
    """

    def __init__(self, vision_ip: str = "224.5.23.2", vision_port: int = 10015):
        """
        Inicializa o objeto e configura o socket multicast.
        """
        self.vision_ip = vision_ip
        self.vision_port = vision_port
        self.sock = self._init_vision_socket()
        print(
            f"Socket de visão inicializado e ouvindo em {self.vision_ip}:{self.vision_port}"
        )

    def _init_vision_socket(self) -> socket.socket:
        """
        Configura e retorna um socket UDP para receber dados de visão multicast.
        Esta é a sua função original, agora como um método privado.
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 128)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

        # Juntar-se ao grupo multicast
        membership_request = struct.pack(
            "=4sl", socket.inet_aton(self.vision_ip), socket.INADDR_ANY
        )
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership_request)

        sock.bind((self.vision_ip, self.vision_port))
        return sock

    def receive_packet(self) -> wr.SSL_WrapperPacket | None: # type: ignore
        """
        Ouve o socket, recebe um pacote e o desserializa usando Protocol Buffers.
        Retorna o pacote desserializado ou None em caso de erro.
        """
        try:
            data, _ = self.sock.recvfrom(2048)  # Aumentar o buffer para segurança
            packet = wr.SSL_WrapperPacket()
            packet.FromString(data)
            return packet
        except socket.timeout:
            print("Timeout ao receber pacote de visão.")
            return None
        except Exception as e:
            print(f"Erro ao receber ou desserializar pacote de visão: {e}")
            return None

    def close(self):
        """Fecha o socket de forma limpa."""
        if self.sock:
            self.sock.close()
            print("Socket de visão fechado.")
