n = int(input("Введите число долек в высоту: "))
m = int(input("Введите число долек в длинну: "))
k = int(input("Введите число долек которые необходимо отломить: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')