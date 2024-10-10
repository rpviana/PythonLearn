    # EXERCICIOS PROF MARCELO

'''________________________________________________________________________________________________________________________'''


# 1. Função para somar valores entre 5 e 10
def somaEntre5e10(*args):
    # A função recebe um número variável de argumentos (args)
    # Utiliza uma compreensão de lista para filtrar os valores entre 5 e 10
    return sum(valor for valor in args if 5 <= valor <= 10)

# 1. Exemplo de soma de valores entre 5 e 10
print(somaEntre5e10(3, 7, 8, 2, 10, 12, 5))  # Saída seria 25 considerando que o 10 nao faria parte

'''________________________________________________________________________________________________________________________'''


# 2. Função anônima para verificar se o número é positivo ou não
verificaPositivo = lambda x: 'P' if x > 0 else 'N'
# A função retorna 'P' se x for positivo e 'N' se x for zero ou negativo

# 2. Verifica se um número é positivo ou não
print(verificaPositivo(10))  # Saída: 'P' (10=positivo)
print(verificaPositivo(-5))  # Saída: 'N' (-5=negativo)

'''________________________________________________________________________________________________________________________'''


# 3. Função para retornar o reverso de um número inteiro
def reversoNum(num):
    # Converte o número em string, inverte a string e converte de volta para inteiro
    return int(str(num)[::-1]) #forma que encontrei para fazer isso

# 3. Reverso de um número
print(reversoNum(127))  # Saída: 721

'''________________________________________________________________________________________________________________________'''


# 4. Função anônima para contar a quantidade de dígitos de um número inteiro
contaDigitos = lambda x: len(str(abs(x)))
# A função conta a quantidade de caracteres do número

# 4. Conta a quantidade de dígitos
print(contaDigitos(12345))  # Saída: 5

'''________________________________________________________________________________________________________________________'''


# 5. Função para verificar se um número é perfeito
def numeroPerf(n):
    # Verifica se o número é menor que 1; se sim, não é perfeito
    if n < 1:
        return False
    # Calcula a soma dos fatores do número, que são os divisores de n
    soma_fatores = sum(i for i in range(1, n) if n % i == 0)
    # Retorna True se a soma dos fatores for igual ao número; caso contrário, retorna False
    return soma_fatores == n

# 5. Verifica se um número é perfeito
print(numeroPerf(6))  # Saída: True
print(numeroPerf(28))  # Saída: True
print(numeroPerf(12))  # Saída: False

'''________________________________________________________________________________________________________________________'''








