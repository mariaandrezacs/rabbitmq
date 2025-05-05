# O que é RabbitMQ?
- é um sistema de mensageria (message broker) de código aberto, amplamente utilizado para enviar, receber e rotear mensagens entre diferentes serviços ou aplicações. 

Diferenças entre HTTP e RABBITMQ

1. Modo de comunicação 
HTTP - serviço direto de uma aplicacao para outra
RABBITMQ - é adicionado um intermediario que pode comunicar-se com ns servicos.

HTTP - síncrono
RABBITMQ - assíncrono 

------------------------------------------------------------------------------------------------------------------------
AMQP (RABBITMQ)
Finalidade 
    - É um protocolo de mensageria usado para comunicação assíncrona entre sistemas distribuidos.

Modo Operacional
    - Seu principal objetivo é garantir o envio confiável de mensagens entre produtores e consumidores, mesmo que esses componentes não estejam disponíveis ao mesmo tempo.

Cenário
    - É ideal para cenários onde a comunicação precisa ser resiliente e tolerante a falhas, como em filas de mensagens.

HTTP (FLASK, FASTAPI, DJANGO)
Finalidade
    - É um protocolo de comunicação síncrono voltado para a transferência de informações entre clientes e servidores na web.

Modo Operacional
    - Usado principalmente para fazer requisições e receber respostas (ex.: APIs RESTful), sendo adequado para transações rápidas e com retorno imediato.

Cenário 
    - É ideal para interações que requerem navegação web ou chamadas de API.
    Sincronismo.

------------------------------------------------------------------------------------------------------------------------

- Publisher 
    * Produtor / publicador: responsavel por enviar a mensagem
    * scrip pyton 

RABBITMQ
- Exchange
    * Gerencia a mensagem do publisher para sua(s) devidas filas
- Fila 
    * Recebe a mensagem e gerencia sua entrega para o Consumer 


- Consumer 
    * Consumidor / Receptor: responsavel por consumir (receber) a mensagem do publisher 
    * script pyhton