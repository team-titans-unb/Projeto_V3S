# Corobeu Project

Este projeto é uma aplicação para controle e comunicação com um robô, utilizando um controlador PID para regular seu comportamento. Abaixo estão as informações sobre a estrutura do projeto e como utilizá-lo.

## Estrutura do Projeto

```
corobeu_project/
├── main.py                       # Ponto de entrada principal da aplicação
├── config.py                     # Parâmetros globais (IP, portas, PID)
├── requirements.txt              # Dependências do projeto
├── controllers/
│   └── pid_controller.py         # Implementação do controlador PID
├── communication/
│   ├── vision_receiver.py        # Processamento da visão e multicast
│   └── robot_sender.py           # Envio de comandos para o robô
├── robot/
│   └── corobeu.py                # Classe principal do robô com controle
├── utils/
│   ├── plotter.py                # Funções para gráficos e logs
│   └── draw_field.py             # Função de desenho do campo (já existente)
└── proto/
    └── wrapper_pb2.py            # Arquivo gerado pelo protobuf
```

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando:

```
pip install -r requirements.txt
```

## Uso

Para iniciar a aplicação, execute o arquivo `main.py`:

```
python main.py
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias e correções. Para isso, faça um fork do repositório e envie suas alterações através de um merge request.

## Licença

Este projeto ainda não possui licença de código aberto.
