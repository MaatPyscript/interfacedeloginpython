from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# Cores
cor0 = '#030303'  # Preto
cor1 = '#c0c2c4'  # Branco
cor2 = '#6e9afa'  # Azul pastel
cor3 = '#47f58a'  # valor
cor4 = '#6e9afa'  # letras

# Criando janela
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

# Dividindo a janela
frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=cor1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando frame cima
l_nome = Label(frame_cima, text='LOGIN', anchor=NE,
               font=('Ivy 25 bold'), bg=cor1, fg=cor0)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=275, anchor=NW,
                font=('Ivy 1'), bg=cor4, fg=cor0)
l_linha.place(x=10, y=45)

credenciais = ['Matheus', '123456789']

# Função para verificar senha


def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login bem sucedido', 'Seja bem vindo !')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login bem sucedido',
                            'Seja bem vindo de volta !')

        # Deletar itens presentes no frame baixo e frame cima
        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_cima.winfo_children():
            widget.destroy()

        nova_janela()

    else:
        messagebox.showwarning(
            'Login incorreto', 'Verifique o usuário e a senha')

# Função após verificação


def nova_janela():
    # Configurando frame cima
    l_nome = Label(frame_cima, text='Usuario : ' + credenciais[0], anchor=NE,
                   font=('Ivy 20'), bg=cor1, fg=cor0)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text='', width=275, anchor=NW,
                    font=('Ivy 1'), bg=cor4, fg=cor0)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_baixo, text='Seja bem vindo ' + credenciais[0], anchor=NE,
                   font=('Ivy 20'), bg=cor1, fg=cor0)
    l_nome.place(x=5, y=105)


# Configurando frame baixo
l_nome = Label(frame_baixo, text='USUÁRIO: ', anchor=NE,
               font=('Ivy 11'), bg=cor1, fg=cor0)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=(
    '', 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)

l_pass = Label(frame_baixo, text='SENHA: ', anchor=NE,
               font=('Ivy 11'), bg=cor1, fg=cor0)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=25, justify='left', show='*', font=(
    '', 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)

b_confirmar = Button(frame_baixo, command=verificar_senha, text='ENTRAR', width=39, height=2, font=(
    'Ivy 8 bold'), bg=cor2, fg=cor0, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)

janela.mainloop()
