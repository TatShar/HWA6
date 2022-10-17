#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n=int(input('inter N '))
lst=[i for i in range(1,n)]
print (lst)
y=1
lst1=[]
y=1
for z in range (1,n+1):
    lst1.append(z*y)
    y=z*y
print(lst1)