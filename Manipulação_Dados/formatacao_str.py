# Método formato f-string

from datetime import datetime
nome = "João"

minha_string = "Olá, " + nome + "."
minha_string1 = f"Olá, {nome}."
minha_string2 = f"Olá, {nome.upper()}."
minha_string3 = f"Quantos anos você tem? {10 + 8}."
minha_string4 = f"O número 2 é maior que o número 1? {2 > 1}."
minha_string5 = f"O número 2 está contido na lista [4, 5, 6]? {2 in [4, 5, 6]}."

print(minha_string)
print(minha_string1)
print(minha_string2)
print(minha_string3)
print(minha_string4)
print(minha_string5)

# Exemplo 2


frutas = ['Jabuticaba', 'laranja', 'uva', 'Banana']
for fruta in frutas:
    minha_fruta = f"Nome: {fruta:12} - Número de letras: {len(fruta): 3}"
    print(minha_fruta)

print()

pi = 3.1415
meu_numero = f'Valor de pi é: {pi:.1f}'
meu_numero_deslocado = f'O número pi deslocado é: {pi:6.1f}'
meu_numero_preciso = f'O número pi com mais precisão é: {pi:.4f}'
print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)

print()

data = datetime.now()
minha_data = f'A data de hoje é: {data}'
minha_data_formatada = f'A data de hoje formatada é: {data:%d/%m/%Y}'
print(minha_data)
print(minha_data_formatada)
