### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
""" try:
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    if quantity > 0 and price > 0:
        print("Valid data")
    else:
        print("Error: Invalid data")

except ValueError as e:
    print(f"Error, invalid input: {e}") """

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'
""" try:
    temperature = float(input("Enter a temperature: "))

    if temperature < 18:
        print("Temperature is low.")
    elif 18 <= temperature <= 26:
        print("Temperature is normal.")
    else:
        print("Temperature is high.")
except ValueError as e:
    print(f"Error, invalid input: {e}") """

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
""" try:
    log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

    if log['level'] == 'ERROR':
        print(f"{log['message']}")
except KeyboardInterrupt as e:
    print("Error: {e}") """

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
""" try:
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")

    if not 18 <= age <= 65:
        raise ValueError ("Age not allowed!")
    elif "@" not in email or "." not in email:
        raise ValueError ("Invalid email.")
    else:
        print("Valid user!")
    
except ValueError as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nProcess interrupted by user.") """

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
""" transacao = {'valor': 1000, 'hora': 20}

if transacao["valor"] > 10000:
    raise ("Error: Value is abouve allowed.")
elif not 9 <= transacao["hora"] <= 18:
    raise ("Error: operation outside permitted time.") """

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
""" phrase = input("Enter a phrase: ")

words = phrase.split()
count_words = dict()

for word in words:
    if word in count_words.keys(): # or "if word in count_words"
        count_words[word] += 1
    else:
        count_words[word] = 1

print(count_words) """

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
""" try:
    numbers = input("Enter the numbers to be normalized separated for space: ")

    numbers_list = list(map(float, numbers.split()))

    min_numbers = min(numbers_list)
    max_numbers = max(numbers_list)

    normalized = [(x - min_numbers) / (max_numbers - min_numbers) for x in numbers_list]

    print(normalized)

except ValueError as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print(f"\nError: User interrupt the program.") """

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
# With list comprehension
""" users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": ""},
    {"name": "Carol", "email": "carol@example.com"}
]

invalid_users = [user for user in users if not user["email"]]

print(invalid_users) """

# without list comprehension
""" users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": ""},
    {"name": "Carol", "email": "carol@example.com"}
]

invalid_users = list()

for user in users:
    if not user["email"]:
        invalid_users.append(user)

print(invalid_users) """

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
""" numbers = range(0, 100)

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers) """

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
""" vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

sales_category = dict()

for venda in vendas:
    category = venda["categoria"]
    value = venda["valor"]

    if venda["categoria"] in sales_category:
        sales_category[category] += value
    else:
        sales_category[category] = value

print(sales_category) """

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
""" while True:
    key_word = input("Enter a key_word: ").lower()
    print(key_word)

    if key_word == "exit":
        break """

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
""" while True:
    input_number = float(input("Enter a number: "))
    
    if not (1 <= input_number <= 10):
        print (f"Error: Entry out of range")
    else:
        print("Entry is valid.")
        break """

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
""" import time

current_page = 1
total_pages = 5  # Simulação, na prática, isso viria da API

while current_page <= total_pages:
    print(f"Processing {current_page}th page of {total_pages}.")
    current_page += 1

    time.sleep(2)

print("Finally processing.") """

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
""" import time

maximum_attempts = 5
attempt = 1

while attempt <= maximum_attempts:
    print(f"Making {attempt}th attempt of {maximum_attempts}.")
    attempt += 1

    time.sleep(2)

print("Attempts exhausted.") """

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
""" import time

items = [1, 2, 3, "break", 4, 5]

for item in items:
    print(item)

    if item == "break":
        print("Halt condition encountered. Halting the system.")
        break

    time.sleep(2) """