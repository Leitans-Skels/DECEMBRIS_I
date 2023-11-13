try:
    skaitlis = int(input("Ievadiet skaitli: "))
except ValueError:
    print(" Ievadītais skaitlis nav derīgs. ")
    exit()

for i in range(1, skaitlis + 1):
    print(i)