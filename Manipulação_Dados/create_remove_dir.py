# Criando um diretório e removendo-o em Python
import os  # Importando o módulo os para manipulação de diretórios

try:  # Criando o diretório
    os.mkdir('novo_diretorio')  # Criando um novo diretório
    print("\nDiretório criado com sucesso.")
except PermissionError as erro:  # Tratando erro de permissão
    print("Sem permissão para criar o diretório:")
    print("Erro de permissão:", erro)
except FileExistsError as erro:  # Tratando erro de diretório já existente
    print("Diretório já existe:")
    print("Erro de existência:", erro)
print("Operação de criação concluída.")

try:  # Removendo o diretório
    os.rmdir('novo_diretorio')  # Removendo o diretório
    print("Diretório removido com sucesso.")
except PermissionError as erro:  # Tratando erro de permissão
    print("Sem permissão para remover o diretório:")
    print("Erro de permissão:", erro)
except FileNotFoundError as erro:  # Tratando erro de diretório não encontrado
    print("Diretório não encontrado:")
    print("Erro de não encontrado:", erro)
except Exception as e:  # Tratando outros erros
    print("Erro ao remover o diretório:", e)
print("Operação de remoção concluída.")
