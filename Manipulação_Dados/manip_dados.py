# Operações de arquivos em python: Removendo e renomenado com precisão

import os  # Importando o módulo os para manipulação de arquivos

with open('manip_dados.txt', 'w') as file:  # Criando o arquivo para escrita
    file.write("\nExemplo de manipulação de dados.\n")  # Escrevendo no arquivo
    file.write("Segunda linha do arquivo.\n")  # Escrevendo no arquivo
with open('manip_dados.txt', 'r') as arquivo:  # Lendo o arquivo
    conteudo = arquivo.read()
    print(conteudo)


try:  # Removendo o arquivo
    os.remove('manip_dados.txt')
    print("Arquivo removido com sucesso.")
except FileNotFoundError:  # Adicionando tratamento de erro
    print("Arquivo não encontrado.")
except Exception as e:  # Tratando outros erros
    print("Erro ao remover o arquivo:", e)
print("Operação concluída.")
