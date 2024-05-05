# Aplicativo de Quiz com XML-RPC

Este README explica a importância da Chamada de Procedimento Remoto (RPC) e fornece uma visão geral dos componentes cliente e servidor utilizados em uma aplicação simples de Quiz implementada com XML-RPC em Python.

## Chamada de Procedimento Remoto (RPC)

RPC é um protocolo que permite que um programa de computador invoque um procedimento (sub-rotina) em outro espaço de endereço (comumente em outro sistema de computador) como se fosse uma chamada de procedimento local, sem o programador codificar explicitamente os detalhes para essa interação remota. RPC permite comunicação transparente entre sistemas distribuídos, permitindo que diferentes processos se comuniquem e executem procedimentos remotamente.

## Cliente

O lado cliente da aplicação de Quiz é responsável por fornecer uma interface gráfica ao usuário (GUI) usando Tkinter e interagir com um servidor remoto via XML-RPC. Aqui estão as principais funcionalidades do cliente:

### `display_questions()`
- Recupera uma lista de perguntas disponíveis do servidor usando `quiz_client.get_list()`.
- Atualiza a GUI exibindo essas perguntas em uma caixa de lista (`question_listbox`) para o usuário visualizar e selecionar.

### `answer_question()`
- Recupera a pergunta selecionada da GUI (`question_listbox`).
- Exibe a pergunta juntamente com suas opções em uma nova janela.
- Permite que o usuário selecione uma resposta usando botões de rádio (`QRadioButton`) e envie sua resposta.
- Comunica-se com o servidor para verificar se a resposta está correta e atualiza o usuário com o resultado.

### `display_total_points()`
- Recupera os pontos totais acumulados pelo usuário do servidor usando `quiz_client.get_total_points()`.
- Exibe os pontos totais em uma caixa de mensagem.

## Servidor

O lado servidor da aplicação de Quiz hospeda as perguntas, lida com as respostas dos usuários e mantém o controle dos pontos totais. Aqui está uma visão geral da funcionalidade do servidor:

### Classe `Quiz`
- Inicializa com uma lista de perguntas do quiz, cada uma contendo o texto da pergunta, opções e resposta correta.
- Registra as perguntas respondidas e os pontos totais ganhos pelo usuário.

### `get_list()`
- Retorna uma lista de perguntas que ainda não foram respondidas.

### `check_answer(question_text, answer)`
- Verifica se a `answer` fornecida corresponde à resposta correta para o `question_text` dado.
- Atualiza os pontos totais conforme necessário.

### `get_total_points()`
- Retorna os pontos totais acumulados pelo usuário.

### Configuração do Servidor XML-RPC
- Configura um servidor XML-RPC (`SimpleXMLRPCServer`) em `localhost` na porta `8000`.
- Registra uma instância da classe `Quiz` no servidor, permitindo que os clientes invoquem seus métodos remotamente.

### Executando a Aplicação

Para executar a aplicação de Quiz:
1. Certifique-se de que o script do servidor está em execução (`server.py`) para lidar com as solicitações dos clientes.
2. Execute o script do cliente (`client.py`) para abrir a interface gráfica do Quiz e interagir com o servidor.
3. Use a GUI para visualizar perguntas, respondê-las e verificar seus pontos totais.

**Observação**: Este README fornece uma visão geral da aplicação de Quiz usando XML-RPC. Para uma implementação completa e implantação, certifique-se de que todas as dependências necessárias estejam instaladas (`tkinter`, `xmlrpc.client`, `xmlrpc.server`). 
