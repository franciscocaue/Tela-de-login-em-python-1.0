import tkinter as tk

#Mini banco de dados para testes
contas = [
    ('teste', '1234'),
    ('teste2', '1357')
]


janela= tk.Tk()
janela.title ('Painel')
janela.geometry('550x500')

# Lmebrar sempre de colocar o pack()
pagina_login = tk.Frame(janela)
pagina_login.pack()

#label seria o margen onde fica o texto
tk.Label(pagina_login, text='Usuário').pack()
usuario_entry = tk.Entry(pagina_login)
usuario_entry.pack()

#sempre criar uma variavel nova mesmo sendo dentro do mesmo Label 
# ex: tk.label '().pack()'

tk.Label(pagina_login, text='Senha').pack()
senha_entry = tk.Entry(pagina_login)
senha_entry.pack()

#variavel para fazer dentro do login () são chaves de escrita onde fica pra digitar = ()
#def é uma função sempre fecha com ():
 
def login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()

    if (usuario, senha) in contas:
        #esse forget serve para tirar o item
        
        pagina_login.pack_forget()
        pagina_sistema.pack(),
    
    else:
        mensagem_label['text'] = 'As credenciais são invalidas!'
        

tk.Button(pagina_login, text='login', command=login).pack()


mensagem_label = tk.Label(pagina_login)
mensagem_label.pack()

pagina_sistema = tk.Frame()
tk.Label(pagina_sistema, text='logando com sucesso').pack()


janela.mainloop()

