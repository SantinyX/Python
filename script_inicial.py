# Manipulação de arquivos em Python
# Este script cria um arquivo de texto, escreve algumas frases nele, lê o conteúdo e depois cria um novo arquivo com o conteúdo modificado.

def main():
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")
    frases = []
    while True:
        entrada = input(">.")
        if entrada.lower() == "sair":
            break
        frases.append(entrada)

    with open("frases.txt", "w", encoding="utf-8") as arquivo:
        for frase in frases:
            arquivo.write(frase + "\n")

    print("Arquivo original criado. Agora vamos manipular os dados.")
    dados_modificados = []
    with open("frases.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            # Exemplo de manipulação: converter para maiúsculas
            dados_modificados.append(linha.strip().upper())

    with open("frases_modificadas.txt", "w", encoding="utf-8") as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + "\n")
    print("Arquivo modificado criado com sucesso.")


if __name__ == "__main__":
    main()
