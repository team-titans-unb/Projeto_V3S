# Arquivo principal de execução

from config import CONFIG
from controllers.pid_controller import PIDController
from communication.vision_receiver import VisionReceiver
from communication.robot_sender import RobotSender
from robot.corobeu import Corobeu

def main():
    # Inicializa os componentes do sistema
    pid_controller = PIDController()
    vision_receiver = VisionReceiver()
    robot_sender = RobotSender()
    robot = Corobeu()

    # Inicia o sistema
    print("Iniciando o sistema...")
    robot.initialize()
    
    # Loop principal
    try:
        while True:
            # Recebe dados de visão
            vision_data = vision_receiver.receive_data()
            # Processa os dados e controla o robô
            control_signal = pid_controller.compute(vision_data)
            robot_sender.send_command(control_signal)
    except KeyboardInterrupt:
        print("Sistema encerrado.")

if __name__ == "__main__":
    main()