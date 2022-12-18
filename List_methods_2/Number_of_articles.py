l = input().lower().split(' ')
print(f"Общее количество артиклей: {l.count('a') + l.count('an') + l.count('the')}")