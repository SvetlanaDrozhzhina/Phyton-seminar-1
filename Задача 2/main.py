print("Введите трёхзначное число: ")
n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
print("Сумма цифр в числе: ")
print(a + b + c)