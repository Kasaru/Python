l = [print(int(m) ** 2, end = ' ') for m in input().split(' ') if int(m) % 2 == 0 and int(m) ** 2 % 10 != 4]
