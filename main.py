# Controle de fluxo
""" print("Esse é o primeiro comando")

x = 5

print("Esse é o segundo comando")

x = 6

print("Esse é o terceiro comando")

print(x) """

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