# Manipulando arquivos e diretórios com o módulo shutil
import os  # Importando o módulo os para manipulação de arquivos e diretórios
import shutil  # Importando o módulo shutil para manipulação de arquivos e diretórios

# Função para criar um diretório


def criar_diretorios(diretorios):
    for diretorio in diretorios:
        try:
            os.makedirs(diretorio)  # Criando diretório
            print(f"Diretório '{diretorio}' criado com sucesso.")
        except PermissionError:
            print(f"Sem permissão para criar o diretório '{diretorio}'.")
        except Exception as e:
            print(f"Erro ao criar o diretório '{diretorio}': {e}")
    print("Operação de criação concluída.")

# Função para mover arquivos com base na extensão


def mover_arquivos(diretorio_origem):
    # Listando arquivos no diretório de origem
    for arquivo in os.listdir(diretorio_origem):
        # Caminho completo do arquivo
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)
        if os.path.isfile(caminho_arquivo):  # Verificando se é um arquivo
            # Obtendo a extensão do arquivo
            extensao = arquivo.split('.')[-1].lower()
            if extensao in ['pdf', 'txt', 'jpg']:
                diretorio_destino = os.path.join(diretorio_origem, extensao)
                try:
                    # Movendo o arquivo
                    shutil.move(caminho_arquivo, diretorio_destino)
                    print(
                        f"Arquivo '{arquivo}' movido para '{diretorio_destino}'.")
                except PermissionError:
                    print(f"Sem permissão para mover o arquivo '{arquivo}'.")
                except Exception as e:
                    print(f"Erro ao mover o arquivo '{arquivo}': {e}")
            else:
                print(
                    f"Extensão '{extensao}' não suportada para o arquivo '{arquivo}'.")


def main():  # Função principal para executar as operações
    diretorio_trabalho = 'diretorio_trabalho'
    diretorios = [os.path.join(diretorio_trabalho, ext)
                  for ext in ['pdf', 'txt', 'jpg']]
    criar_diretorios(diretorios)  # Criando diretórios

    mover_arquivos(diretorio_trabalho)  # Movendo arquivos
    print("Operação de movimentação concluída.")

    # # Removendo o diretório de trabalho e seu conteúdo
    # try:
    #     shutil.rmtree(diretorio_trabalho)
    #     print(f"Diretório '{diretorio_trabalho}' removido com sucesso.")
    # except PermissionError:
    #     print(
    #         f"Sem permissão para remover o diretório '{diretorio_trabalho}'.")
    # except Exception as e:
    #     print(f"Erro ao remover o diretório '{diretorio_trabalho}': {e}")
    # print("Operação de remoção concluída.")


if __name__ == "__main__":
    main()  # Executando a função principal
