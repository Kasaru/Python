s = input()
s = s.lower()
vowel = 0
consonant = 0
for i in range(len(s)):
    if s[i] in "ауоыиэяюёе":
        vowel += 1
    if s[i] in "бвгджзйклмнпрстфхцчшщ":
        consonant += 1
print("Количество гласных букв равно " + str(vowel))
print("Количество согласных букв равно " + str(consonant))