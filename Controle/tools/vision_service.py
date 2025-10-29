import time
from vsss.perception.vision_receiver import VisionReceiver
# IMPORTANTE: Aqui importaremos o nosso cliente do bus de mensagens
# from vsss_ai.communication.message_bus_client import MessageBusClient


def main():
    """
    Ponto de entrada para o serviço de processamento de visão.
    Este processo corre continuamente, independente da IA dos robôs.
    """
    vision_receiver = VisionReceiver()
    # message_bus = MessageBusClient() # Exemplo de como seria

    print("Serviço de Visão iniciado. Pressione Ctrl+C para parar.")

    try:
        while True:
            # 1. Recebe o pacote de visão bruto
            packet = vision_receiver.receive_packet()

            if packet:
                # 2. Publica o pacote no bus de mensagens
                # Em vez de ser acedido diretamente, o pacote é "transmitido"
                # para quem quiser ouvir (neste caso, o WorldModeler).
                print(
                    f"Pacote de visão recebido (frame: {packet.detection.frame_number}). Publicando no bus..."
                )
                # message_bus.publish("vision_packet", packet.SerializeToString()) # Exemplo real

            # Pequena pausa para não sobrecarregar a CPU se não houver pacotes
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("Serviço de Visão a ser encerrado.")
    finally:
        vision_receiver.close()


if __name__ == "__main__":
    main()
