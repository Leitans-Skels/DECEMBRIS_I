def atrodi_pirmo_kvadrātsakni_virs_1000():
    number = 1

    while number ** 2 <= 1000:
        number += 1

    return number

result = atrodi_pirmo_kvadrātsakni_virs_1000()
print(f" Pirmais skaitlis kuram kvadrāts ir lielāks par 1000 ir: {result}")