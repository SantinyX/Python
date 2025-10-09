# Tratamento de exceções ao manipular arquivos e diretórios usando o módulo os
import os  # Importando o módulo os para manipulação de arquivos e diretórios

try:  # Criando diretório
    os.mkdir('diretorio_teste')  # Tentando criar um diretório
    print("Diretório criado com sucesso.")
except FileExistsError:  # Tratando erro de diretório já existente
    print("Diretório já existe.")
except PermissionError:  # Tratando erro de permissão
    print("Sem permissão para criar o diretório.")
except Exception as e:  # Tratando outros erros
    print(f"Erro ao criar o diretório: {e}")

# Criando um arquivo dentro do diretório
try:
    with open('diretorio_teste/arquivo_teste.txt', 'w', encoding='utf-8') as file:  # Criando arquivo
        file.write("Conteúdo de teste.")  # Escrevendo no arquivo
    print("Arquivo criado com sucesso.")
except FileNotFoundError:  # Tratando erro de diretório não encontrado
    print("Diretório não encontrado.")
except PermissionError:  # Tratando erro de permissão
    print("Sem permissão para criar o arquivo.")
except Exception as e:  # Tratando outros erros
    print(f"Erro ao criar o arquivo: {e}")
