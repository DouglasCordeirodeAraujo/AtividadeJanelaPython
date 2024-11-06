# Incluir Biblioteca tkinter
import tkinter as tk
# Importa a função messagebox para exibir mensagens de alerta ou informação
from tkinter import messagebox
# Importa a biblioteca PIL para manipular a imagem
from PIL import Image, ImageTk

# Função para adicionar uma tarefa a listaTarefa pelo botao_Adicionar
def botao_Adicionar():
    texto = entrada_tarefa.get()
    if texto:
        listaTarefa.insert(tk.END, texto)
        entrada_tarefa.delete(0, tk.END)
        messagebox.showinfo("Gerenciador",message="Tarefa Adicionada!")
    else:
        messagebox.showinfo("Atenção!",message="Digite uma Tarefa!")
# Função para concluir uma tarefa na listaTarefa pelo botao_Concluir   
def botao_Concluir():
    if tarefa_selecionada := listaTarefa.curselection():
        tarefa = listaTarefa.get(tarefa_selecionada)
        listaTarefa.delete(tarefa_selecionada)
        listaTarefa.insert(tarefa_selecionada,f"{tarefa} - (Concluida!)")
        messagebox.showinfo("Gerenciador",message="Tarefa Concluida!")
    else:
        messagebox.showinfo("Atenção!",message="Selecione uma Tarefa!")
# Função para remover uma tarefa na listaTarefa pelo botao_Remover
def botao_Remover():
    if tarefa_selecionada := listaTarefa.curselection():
        listaTarefa.delete(tarefa_selecionada)
        messagebox.showinfo("Gerenciador",message="Tarefa Removida!")
    else:
        messagebox.showinfo("Atenção!",message="Selecione uma Tarefa!")

# Criando Janela Principal
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.configure(bg="black")
janela.geometry("500x500")

# Carregando imagem "Fundo.jpg" e sua dimensão
imagem_fundo = Image.open("Fundo.jpg")
imagem_fundo = imagem_fundo.resize((500, 500),Image.LANCZOS)
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)
# Imagem no fundo da janela
label_fundo = tk.Label(janela, image=imagem_fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Adiciona um rotulo escrito "Adicionar Tarefas:", e suas configurações
rotulo_texto = tk.Label(janela, text="Adicionar Tarefas:",fg="yellow",font=("Arial", 12,"bold"),bg="#194168")
rotulo_texto.pack(pady=10)
# Local para escrever a tarefa adicionada e suas configurações
entrada_tarefa = tk.Entry(janela, font=("Arial", 12,"bold"),fg="white",width=40,bg="black")
entrada_tarefa.place(x=66,y=40)
# Adicionaa um rotulo escrito "Tarefas Adicionadas:" e suas configurações
rotulo_texto = tk.Label(janela, text="Tarefas Adicionadas:",fg="yellow",font=("Arial", 12,"bold"),bg="#194168")
rotulo_texto.pack(pady=25)
# Local onde a tarefa escrita pelo usuário será armazenada
listaTarefa = tk.Listbox(janela,font=("Arial", 12,"bold"),fg="white", height =16, width =40,bg="black")
listaTarefa.place(x=66,y=100)

# Cria botão para "adicionar tarefa" e suas configurações
botao_Adicionar = tk.Button(janela, text="Adicionar Tarefa",fg="green", command=botao_Adicionar, width=15, height=2,font=("Arial", 10, "bold"),bg="black")
botao_Adicionar.place(x=40,y=430)
# Cria botão para "concluir tarefa" e suas configurações
botao_Concluir = tk.Button(janela, text="Concluir Tarefa",fg="yellow", command=botao_Concluir, width=15, height=2,font=("Arial", 10, "bold"),bg="black")
botao_Concluir.place(x=180,y=430)
# Cria botão para "remover tarefa" e suas configurações
botao_Remover = tk.Button(janela, text="Remover Tarefa",fg="red", command=botao_Remover, width=15,height=2,font=("Arial", 10, "bold"),bg="black")
botao_Remover.place(x=320,y=430)

#loop da janela
janela.mainloop()