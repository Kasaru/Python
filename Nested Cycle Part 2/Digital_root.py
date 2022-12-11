n = int(input())
digit = 0
if n > 9:
    while n // 10 != 0:
        while n != 0:
            digit += n % 10
            n //= 10
        digit += n
        if digit // 10 !=0:
            n = digit
            digit = 0
else:
    digit = n
print(digit)