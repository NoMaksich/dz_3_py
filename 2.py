massiv = []

a = input("Введите числа в строку: ")
b = a.split(' ')
for i in b:
    massiv.append(int(i))
    
max_number = massiv[0]
for i in massiv:
    if i > max_number:
        max_number = i
    else:
        continue

print(max_number)