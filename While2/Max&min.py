n = int(input())
max,min = 0,9
while n!=0:
    if max<n%10:
        max = n%10
    if min>n%10:
        min = n%10
    n = n//10
print("Максимальная цифра равна " + str(max) + "\nМинимальная цифра равна " + str(min))