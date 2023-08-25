import re
import sys

entrada = input('CPF: ')
cpf = re.sub(r'[^0-9]', '', entrada)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Voce enviou dados sequenciais')
    sys.exit()

nove_primeiros = cpf[:9]  
contador_regressivo_1 = 10 
resultado_1 = 0

for numero in nove_primeiros:
    resultado_1 += int(numero) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = resultado_1 *10 % 11

digito_1 = digito_1 if digito_1 <= 9 else 0
#print(digito_1)


nove_primeiros_2 = cpf[:10]
contador_regressivo_2 = 11
resultado_2 = 0

for nuemero_2 in nove_primeiros_2:
    resultado_2 += int(nuemero_2) * contador_regressivo_2
    contador_regressivo_2 -=1

digito_2 = resultado_2 * 10 % 11

digito_2 = digito_2 if digito_2 <=9 else 0
#print(digito_2)

novo_cpf = f'{nove_primeiros}{digito_1}{digito_2}'
#print(novo_cpf)

if cpf == novo_cpf:
    print(f'{novo_cpf} é válido')
else:
    print('esse cpf não é valido')

