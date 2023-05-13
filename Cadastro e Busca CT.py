import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    cpf = entry_cpf.get()
    nome_mae = entry_nome_mae.get()
    cpf_mae = entry_cpf_mae.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    data = {'Nome': [nome],
            'Idade': [idade],
            'CPF': [cpf],
            'Nome da Mãe': [nome_mae],
            'CPF da Mãe': [cpf_mae],
            'Telefone': [telefone],
            'Endereço': [endereco]}

    df = pd.DataFrame(data)

    try:
        try:
            existing_df = pd.read_excel('cadastro.xlsx')
            df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            pass

        df.to_excel('cadastro.xlsx', index=False)
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        limpar_campos()
    except:
        messagebox.showerror("Erro", "Ocorreu um erro ao cadastrar.")

def buscar():
    valor_busca = entry_busca.get()
    campo_busca = combo_campos.get()

    try:
        df = pd.read_excel('cadastro.xlsx')
        resultado = df[df[campo_busca].astype(str).str.contains(valor_busca, case=False)]

        if not resultado.empty:
            messagebox.showinfo("Resultado", "Busca realizada com sucesso!")
            treeview.delete(*treeview.get_children())

            for _, row in resultado.iterrows():
                treeview.insert("", tk.END, values=row.tolist())
        else:
            messagebox.showinfo("Resultado", "Nenhum resultado encontrado.")
    except FileNotFoundError:
        messagebox.showinfo("Resultado", "Nenhum dado cadastrado.")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_nome_mae.delete(0, tk.END)
    entry_cpf_mae.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

# Criar a janela principal
window = tk.Tk()
window.title("Cadastro de Atendimento")
window.geometry("300x350")

# Criar o TabControl
tab_control = ttk.Notebook(window)

# Aba de Cadastro
tab_cadastro = ttk.Frame(tab_control)
tab_control.add(tab_cadastro, text="Cadastro")

# Criar os campos de entrada
label_nome = tk.Label(tab_cadastro, text="Nome da Criança/Adolescente:")
label_nome.pack()
entry_nome = tk.Entry(tab_cadastro)
entry_nome.pack()

label_idade = tk.Label(tab_cadastro, text="Idade da Criança/Adolescente:")
label_idade.pack()
entry_idade = tk.Entry(tab_cadastro)
entry_idade.pack()

label_cpf = tk.Label(tab_cadastro, text="CPF da Criança/Adolescente:")
label_cpf.pack()
entry_cpf = tk.Entry(tab_cadastro)
entry_cpf.pack()

label_nome_mae = tk.Label(tab_cadastro, text="Nome do Responsável:")
label_nome_mae.pack()
entry_nome_mae = tk.Entry(tab_cadastro)
entry_nome_mae.pack()

label_cpf_mae = tk.Label(tab_cadastro, text="CPF do Responsável:")
label_cpf_mae.pack()
entry_cpf_mae = tk.Entry(tab_cadastro)
entry_cpf_mae.pack()

label_telefone = tk.Label(tab_cadastro, text="Telefone do Responsável:")
label_telefone.pack()
entry_telefone = tk.Entry(tab_cadastro)
entry_telefone.pack()

label_endereco = tk.Label(tab_cadastro, text="Endereço:")
label_endereco.pack()
entry_endereco = tk.Entry(tab_cadastro)
entry_endereco.pack()

# Botão para cadastrar
button_cadastrar = tk.Button(tab_cadastro, text="Cadastrar", command=cadastrar)
button_cadastrar.pack()

# Aba de Busca
tab_busca = ttk.Frame(tab_control)
tab_control.add(tab_busca, text="Busca")

# Criar os campos de busca
label_busca = tk.Label(tab_busca, text="Valor de busca:")
label_busca.pack()
entry_busca = tk.Entry(tab_busca)
entry_busca.pack()

label_campos = tk.Label(tab_busca, text="Buscar em:")
label_campos.pack()
combo_campos = ttk.Combobox(tab_busca, values=["Nome", "Idade", "CPF", "Nome da Mãe", "CPF da Mãe", "Telefone", "Endereço"])
combo_campos.pack()

# Botão para buscar
button_buscar = tk.Button(tab_busca, text="Buscar", command=buscar)
button_buscar.pack()

# Criar a tabela para exibir o resultado da busca
treeview = ttk.Treeview(tab_busca, columns=["Nome", "Idade", "CPF", "Nome da Mãe", "CPF da Mãe", "Telefone", "Endereço"])
treeview.heading("Nome", text="Nome")
treeview.heading("Idade", text="Idade")
treeview.heading("CPF", text="CPF")
treeview.heading("Nome da Mãe", text="Nome da Mãe")
treeview.heading("CPF da Mãe", text="CPF da Mãe")
treeview.heading("Telefone", text="Telefone")
treeview.heading("Endereço", text="Endereço")
treeview.pack()

# Adicionar as abas ao TabControl
tab_control.pack(expand=1, fill="both")

# Iniciar a interface gráfica
window.mainloop()
