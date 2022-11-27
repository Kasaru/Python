n = int(input())
while len(str(n)) != 2:
    n = n // 10
print(n % 10)