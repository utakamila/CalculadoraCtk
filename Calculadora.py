#Projeto Calculadora CTK
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Função para calcular os valores
def calcular():
    n1 = float((campo_n1.get()))
    n2 = float((campo_n2.get()))
    op = operacao.get()



    if op == "+":
        resultado = n1 + n2
        lbl_resultado.configure(
            text = f"Resultado Final - {resultado:.2f}",
            text_color = "#FFFFFF"
        )
    elif op == "-":
        resultado = n1 - n2
        lbl_resultado.configure(
            text = f"Resultado Final - {resultado:.2f}",
            text_color = "#FFFFFF"
        )
    elif op == "*":
        resultado = n1 * n2
        lbl_resultado.configure(
            text = f"Resultado Final - {resultado:.2f}",
            text_color = "#FFFFFF"
        )
    elif op == "/":
        if n2 == 0:
            lbl_resultado.configure(
                text = "Não é permitido dividir por 0",
                text_color = "#FF0000"
            )
        else:    
            resultado = n1 / n2
            lbl_resultado.configure(
                text = f"Resultado Final - {resultado:.2f}",
                text_color = "#FFFFFF"
            )
    else:
        lbl_resultado.configure(
            text = "Escolha uma opção",
            text_color = "#FF0000"
        )

#Criaçao da janela principal
janela = ctk.CTk()
janela.geometry("500x450")
janela.title("Calculadora")

#Titulo da calculadora
lbl_titulo = ctk.CTkLabel(janela, text= "Calculadora", font=("Arial", 22, "bold"))
lbl_titulo.pack(pady=20)

#Campos de entrada para os números
campo_n1 = ctk.CTkEntry(janela, placeholder_text = "Primeiro numero aqui", width = 250)
campo_n1.pack(pady=10)
campo_n2 = ctk.CTkEntry(janela, placeholder_text = "Segundo numero aqui", width = 250)
campo_n2.pack(pady=10)

#Aqui Inicia a variavel "Operacao" que vai receber o valor da operação escolhida pelo usuário
operacao = ctk.StringVar(value="Nothing")

#Aqui Inicia os RadioButtons para escolher a operação
radio1 = ctk.CTkRadioButton(
    janela,
    text="Soma",
    variable = operacao,
    value="+"
)

radio2 = ctk.CTkRadioButton(
    janela,
    text="Subtração",
    variable= operacao,
    value= "-"
)

radio3 = ctk.CTkRadioButton(
    janela,
    text="Multiplicação",
    variable= operacao,
    value="*"
)

radio4 = ctk.CTkRadioButton(
    janela,
    text="Divisão",
    variable= operacao,
    value="/"
)

radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)
radio4.pack(pady=5)

#Botão para calcular o resultado
btn_calcular = ctk.CTkButton(
    janela,
    text= "Calcular",
    command=calcular,
    corner_radius = 12,
    width = 200
)
btn_calcular.pack(pady=15)

#Label para mostrar o resultado
lbl_resultado = ctk.CTkLabel(janela, text="", font=("Arial", 16, "bold"))
lbl_resultado.pack(pady=20)

janela.mainloop()