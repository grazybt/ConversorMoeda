#janela
#título
#campos para selecionar as moedas de origem e destino
#botão para converter
#lista de exibição com os nomes das moedas

#importar biblioteca que vai fazer a janela
import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

#criar e configurar a janela
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
janela = customtkinter.CTk()
janela.geometry("600x600")
janela.title("Conversor de Moedas")
janela.iconbitmap("calculator.ico")

dic_conversoes_disponiveis = conversoes_disponiveis()

#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("Perpetua Titling MT", 20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("Palatino Linotype", 16))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("Palatino Linotype", 16))

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino, font=("Palatino Linotype", 14))
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= ["Selecione uma moeda de "], font=("Palatino Linotype", 14))

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text= f"1 {moeda_origem} = {cotacao} {moeda_destino}")


botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda, font=("Perpetua Titling MT", 14))

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="", font=("", 20))

moedas_disponiveis = nomes_moedas()

for codigo_moeda in moedas_disponiveis:
    nomes_moedas = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nomes_moedas}", font=("Palatino Linotype", 14))
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
texto_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

#rodar a janela
janela.mainloop()




