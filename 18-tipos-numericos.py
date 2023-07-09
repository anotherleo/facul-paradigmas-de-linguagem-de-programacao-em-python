"""
    Diferentemente de outras linguagens, como C ou Java, a linguagem Python não limita
    o tamanho de uma variável de qualquer tipo, logo, não existe um valor inteiro máximo definido.
    O limite depende da quantidade de memória disponível no computador.
"""

# int
print(type(1_000_000))

# float (Devemos usar o ponto para separar a parte inteira da parte decimal)
print(type(50.0)) 

# exponenciação
print (2**3)
print (type(2**3)) # int
print (type(2.0**3)) # float

# divisão
print (type(5/2)) # float
print (type(5%2)) # int

# tipo complex
w = 2+5j
print (type(w))

# tipo bool e operador not
x = 2 > 3
print (type(x), x, not(x))

