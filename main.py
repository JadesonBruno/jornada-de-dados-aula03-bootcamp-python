# Controle de fluxo
""" print("Esse é o primeiro comando")

x = 5

print("Esse é o segundo comando")

x = 6

print("Esse é o terceiro comando")

print(x) """

# IF
# Provavelmente o mais conhecido comando de controle de fluxo é o if. Por exemplo:
""" x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More') """

# Lógica construída de formar que nunca chegará na 2ª condição p x = negativo, 
# apesar de também atender a condição
""" x = int(input("Please enter an integer: "))

if x < 0:
    print('Number is less than zero')
elif x <= 2:
    print('Number is less than two')
else:
    print('More') """

# FOR

# Measure some strings:
""" words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w)) """

# Measure some strings: (print the list element)
""" nome = ['Luciano']
for letra in nome:
    print(letra) """

# Measure some strings: (print the characters of string)
""" nome = 'Luciano'
for letra in nome:
    print(letra) """

# Range generate arithimetic progressions
""" for i in range(5):
    print(i) """

# Start, stop, step
""" list(range(5, 10))
[5, 6, 7, 8, 9]

list(range(0, 10, 3))
[0, 3, 6, 9]

list(range(-10, -100, -30))
[-10, -40, -70] """

# Iteration over list indices
""" a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i]) """

# WHILE

# Example for the While loop structure
""" import time

try:
    while True:
        print("Verificando novos dados...")
        # Aqui você pode adicionar o código para verificar novos dados,
        # por exemplo, checar a existência de novos arquivos em um diretório,
        # fazer uma consulta a um banco de dados ou API, etc.
        
        time.sleep(5)  # Pausa o loop por 10 segundos

except KeyboardInterrupt:
    print("Error: User interrupted the program.") """