s = input()
countstar = 0
countplus = 0
for i in range(len(s)):
    if s[i] == "*":
        countstar += 1
    if s[i] == "+":
        countplus += 1
print("Символ + встречается " + str(countplus) + " раз")
print("Символ * встречается " + str(countstar) + " раз")