import tkinter as tk
from tkinter import messagebox
import xmlrpc.client

# Conexão com o servidor RPC
quiz_client = xmlrpc.client.ServerProxy("http://localhost:8000")

# Função para exibir a lista de perguntas disponíveis
def display_questions():
    questions = quiz_client.get_list()
    if questions == "finished":
        messagebox.showinfo("Quiz Concluído", "Você respondeu a todas as perguntas!")
        return
    
    question_listbox.delete(0, tk.END)  # Limpa a lista atual
    for idx, question in enumerate(questions):
        question_listbox.insert(tk.END, f"{idx + 1}. {question['question_text']}")

import tkinter as tk
from tkinter import messagebox
import xmlrpc.client

# Conexão com o servidor RPC
quiz_client = xmlrpc.client.ServerProxy("http://localhost:8000")

# Função para exibir a lista de perguntas disponíveis
def display_questions():
    questions = quiz_client.get_list()
    if questions == "finished":
        messagebox.showinfo("Quiz Concluído", "Você respondeu a todas as perguntas!")
        return
    
    question_listbox.delete(0, tk.END)  # Limpa a lista atual
    for idx, question in enumerate(questions):
        question_listbox.insert(tk.END, f"{idx + 1}. {question['question_text']}")

def answer_question():
    selected_indices = question_listbox.curselection()
    if not selected_indices:
        messagebox.showinfo("Erro", "Selecione uma pergunta para responder.")
        return
    
    # Obter o índice da primeira seleção
    question_index = selected_indices[0]
    question_number = question_index + 1
    questions = quiz_client.get_list()

    if questions == "finished":
        messagebox.showinfo("Quiz Concluído", "Você respondeu a todas as perguntas!")
    elif 1 <= question_number <= len(questions):
        question = questions[question_index]
        answer_window = tk.Toplevel(root)
        answer_window.title("Responder Pergunta")
        
        tk.Label(answer_window, text=f"Pergunta: {question['question_text']}").pack()
        tk.Label(answer_window, text="Opções:").pack()
        
        option_var = tk.StringVar(answer_window)
        for idx, option in enumerate(question['options']):
            tk.Radiobutton(answer_window, text=option, variable=option_var, value=idx).pack(anchor=tk.W)
        
        def submit_answer():
            selected_option_index = int(option_var.get())  # Converter para número inteiro
    
            # Obter a opção correta
            correct_option = question['correct_option']
            
            # Verificar se a opção selecionada pelo usuário corresponde à resposta correta
            if question['options'][selected_option_index] == correct_option:
                quiz_client.check_answer(question['question_text'], correct_option)
                messagebox.showinfo("Resposta", "Resposta correta!")
            else:
                messagebox.showinfo("Resposta", "Resposta incorreta!")
            
            answer_window.destroy()
            display_total_points()
                
        submit_button = tk.Button(answer_window, text="Responder", command=submit_answer)
        submit_button.pack()

    else:
        messagebox.showinfo("Erro", "Número de pergunta inválido.")

def display_total_points():
    total_points = quiz_client.get_total_points()
    messagebox.showinfo("Pontuação Total", f"Sua pontuação total é: {total_points}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Quiz App")

# Botões e lista
question_frame = tk.Frame(root)
question_frame.pack(pady=10)

question_listbox = tk.Listbox(question_frame, width=50, height=10)
question_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = tk.Scrollbar(question_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

question_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=question_listbox.yview)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

view_button = tk.Button(button_frame, text="Ver Lista de Perguntas", command=display_questions)
view_button.grid(row=0, column=0, padx=10)

answer_button = tk.Button(button_frame, text="Responder Pergunta", command=answer_question)
answer_button.grid(row=0, column=1, padx=10)

score_button = tk.Button(button_frame, text="Ver Pontuação Total", command=display_total_points)
score_button.grid(row=0, column=2, padx=10)

exit_button = tk.Button(button_frame, text="Sair", command=root.quit)
exit_button.grid(row=0, column=3, padx=10)

root.mainloop()


def display_total_points():
    total_points = quiz_client.get_total_points()
    messagebox.showinfo("Pontuação Total", f"Sua pontuação total é: {total_points}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Quiz App")

# Botões e lista
question_frame = tk.Frame(root)
question_frame.pack(pady=10)

question_listbox = tk.Listbox(question_frame, width=50, height=10)
question_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = tk.Scrollbar(question_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

question_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=question_listbox.yview)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

view_button = tk.Button(button_frame, text="Ver Lista de Perguntas", command=display_questions)
view_button.grid(row=0, column=0, padx=10)

answer_button = tk.Button(button_frame, text="Responder Pergunta", command=answer_question)
answer_button.grid(row=0, column=1, padx=10)

score_button = tk.Button(button_frame, text="Ver Pontuação Total", command=display_total_points)
score_button.grid(row=0, column=2, padx=10)

exit_button = tk.Button(button_frame, text="Sair", command=root.quit)
exit_button.grid(row=0, column=3, padx=10)

root.mainloop()
