stroka = input("Введите строку: ")

stroka = stroka.lower().replace(" ", "")

palindrom = True

for i in range(len(stroka) // 2):
    if stroka[i] != stroka[len(stroka) - (i + 1)]:
        palindrom = False
        break

if palindrom:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
