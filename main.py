#janela
#título
#campos para selecionar as moedas de origem e destino
#botão para converter
#lista de exibição com os nomes das moedas

#importar biblioteca que vai fazer a janela
import customtkinter

#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
janela = customtkinter.CTk()
janela.geometry("600x600")

#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("", 28))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("", 16))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("", 16))
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"], font=("", 14))
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"], font=("", 14))

def converter_moeda():
    print("Converter moeda")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda, font=("", 17))

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD: Dólar americano", "EUR: Euro", "BRL: Real brasileiro", "BTC: Bitcoin"]
for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()

#moeda1 = customtkinter.CTkLabel(lista_moedas, text= "USD: Dólar americano")
#moeda2 = customtkinter.CTkLabel(lista_moedas, text= "EUR: Euro")
#moeda3 = customtkinter.CTkLabel(lista_moedas, text= "BRL: Real brasileiro")
#moeda4 = customtkinter.CTkLabel(lista_moedas, text= "BTC: Bitcoin")
#moeda1.pack()
#moeda2.pack()
#moeda3.pack()
#moeda4.pack()

#colocar os elementos criados na tela
titulo.pack(padx=10, pady=20)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10, pady=10)
botao_converter.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

#rodar a janela
janela.mainloop()




