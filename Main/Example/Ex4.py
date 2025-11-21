st = input()
b = False
for i in st:
    if i == 'a' or i == 'o':
        b = True
    if i == 'i' or i == 'e':
        b = False
        break
print(b)