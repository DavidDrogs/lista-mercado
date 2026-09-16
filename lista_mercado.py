lista_compra = []

def mostrar_lista(lista):
    contador = 1
    for lista_compras in lista:
        print(str(contador) + " - " + lista_compras["produto"] + " ( " + lista_compras["quantidade"] + " unidade)")
        contador = contador + 1

while True:
    produto = input("digite o nome do produto (ou 'sair'): ")
    if produto == "sair":
        break
    quantidade = input("digite a quantidade ")

    nova_lista = { "produto": produto, "quantidade": quantidade }
    lista_compra.append(nova_lista)

mostrar_lista(lista_compra)
