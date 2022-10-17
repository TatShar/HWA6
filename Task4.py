#Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
#Пример:2+2 => 4;1+2*3 => 7;1-2*3 => -5;

a = input('Enter viragenie: ')
a=a.split()
for i in range(len(a)):
    if a[i].isdigit():
        a[i]=int(a[i])
print (a)
for z in range(len(a)-1):
    if a[z]=='*':
        res = a[z-1]*a[z+1]
        a[z]=res
        a.pop (z+1)
        a.pop(z-1)
for y in range (len(a)-1):
    if a[y]=='/':
        res = a[y-1]/a[y+1]
        a[y]=res
        a.pop (y+1)
        a.pop(y-1)
    # else:
    #     break
for k in range(len(a)-1):
    if a[k]=='+':
        res = a[k-1]+a[k+1]
        a[k]=res
        a.pop (k+1)
        a.pop(k-1)
for t in range (len(a)-1):
    if a[t]=='-':
        res = a[t-1]-a[t+1]
        a[t]=res
        a.pop (t+1)
        a.pop(t-1)
    #else: break
print (a)
    


       

