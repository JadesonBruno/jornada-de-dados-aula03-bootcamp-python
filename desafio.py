# Integre no desafio anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas.
""" valid_name = False
valid_salary = False
valid_bonus = False

while not valid_name:
    try:
        name = input("Type your name: ")

        if not name:
            raise ValueError("Name cannot be empty.")
        elif name.isspace():
            raise ValueError("Name cannot contain only spaces.")
        elif any(char.isdigit() for char in name):
            raise ValueError("Name cannot contain digits.")
        else: 
            print("Your name is valid.")
            valid_name = True

    except ValueError as e:
        print(f"Error: {e}")

while not valid_salary:
    try:
        salary = float(input("Type your salary: "))

        if salary < 0:
            raise ValueError("Salary cannot be less than zero.")
        else: 
            print("Salary is valid.")
            valid_salary = True

    except ValueError as e:
        print(f"Error: {e}")

while not valid_bonus:
    try:
        bonus = float(input("Type your bonus: "))
        
        if bonus < 0:
            raise ValueError("Bonus cannot be less than zero.")
        else:
            print("Bonus is valid.")
            valid_bonus = True

    except ValueError as e:
        print(f"Error: {e}")

CONSTANTE_BONUS = 1000

final_bonus = CONSTANTE_BONUS + salary * bonus

print(f'''###============###\nMr./Mrs. {name},\nYour salary is: {salary}\nAnd your final bonus is: {final_bonus}\n###============###''') """