# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
n = int(input('inter N '))
lst=[round((1+1/n)**n,2) for i in range (n+1)]
print (lst)
print (sum(lst))
