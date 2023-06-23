""" Questão 5: Determine o n-ésimo termo e a soma dos termos de uma progressão aritmética 
onde n, primeiro termo e a razão são dados pelo usuário."""



# Atribuição


#Entrada
primeiroTermo = int(input("Qual é o primeiro termo? "))
n = int(input("Qual é o n? "))
razao = int(input("Qual é a razão? "))


# Processamento
nesimoTermo = primeiroTermo + ((n-1) * razao)
nesimoTermoString = str(nesimoTermo)

somaProgressaoAritmetica = (primeiroTermo + nesimoTermo) * (n / 2)
somaProgressaoAritmeticaString = str(somaProgressaoAritmetica)


# Saída
print("O n-ésimo termo é: " + nesimoTermoString)
print("A soma dos termos da progressão é: " + somaProgressaoAritmeticaString)


