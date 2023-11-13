user_input = input("Ievadi skaitli: ")

number = int(user_input)

if number % 2 != 0:
    print(f"{number} Ir nepāra skaitlis.")
else:
    print(f"{number} Ir pāra skaitlis.")