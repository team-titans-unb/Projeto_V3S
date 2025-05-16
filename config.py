# Arquivo de configuração global do projeto

# Endereço IP do robô
ROBOT_IP = "192.168.1.100"

# Porta para comunicação com o robô
ROBOT_PORT = 5000

# Identificador de processo (PID)
PROCESS_ID = 12345

# Configurações do controlador PID
PID_CONFIG = {
    "Kp": 1.0,  # Ganho proporcional
    "Ki": 0.1,  # Ganho integral
    "Kd": 0.05  # Ganho derivativo
}