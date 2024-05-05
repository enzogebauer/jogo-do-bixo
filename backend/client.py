import xmlrpc.client

# Conectando-se ao servidor RPC
quiz_client = xmlrpc.client.ServerProxy("http://localhost:8000")

# Função para exibir a lista de perguntas disponíveis
def display_questions():
    print("Lista de Perguntas Disponíveis:")
    questions = quiz_client.get_list()
    for idx, question in enumerate(questions):
        print(f"{idx + 1}. {question['question_text']}")

def answer_question():
    question_number = int(input("Escolha o número da pergunta que deseja responder: "))
    questions = quiz_client.get_list()
    
    # Verifica se o número da pergunta está dentro do intervalo válido
    if 1 <= question_number <= len(questions):
        question = questions[question_number - 1]
        print(f"Pergunta: {question['question_text']}")
        print("Opções:")
        for idx, option in enumerate(question['options']):
            print(f"{idx + 1}. {option}")
        answer_index = int(input("Escolha a opção correta (digite o número correspondente): "))
        correct_option = question['correct_option']
        selected_option = question['options'][answer_index - 1]

        # Verifica se a resposta está correta e atualiza a pontuação
        if selected_option == correct_option:
            quiz_client.check_answer(question['question_text'], correct_option)
            print("Resposta correta!")
        else:
            print("Resposta incorreta!")

    else:
        print("Número de pergunta inválido.")


# Função para exibir a pontuação total
def display_total_points():
    total_points = quiz_client.get_total_points()
    print(f"Sua pontuação total é: {total_points}")

# Loop para interagir com o servidor
while True:
    print("\nEscolha uma opção:")
    print("1. Ver Lista de Perguntas")
    print("2. Responder uma Pergunta")
    print("3. Ver Pontuação Total")
    print("4. Sair")
    choice = int(input("Escolha uma opção: "))
    
    if choice == 1:
        display_questions()
    elif choice == 2:
        answer_question()
    elif choice == 3:
        display_total_points()
    elif choice == 4:
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")
