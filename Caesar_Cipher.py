


alpha = input('알파벳을 입력해주세요.').upper()
list = []
for i in alpha:
    list.append((ord(i)-64)+3)
    #print((ord(i)-64)+3, end=' ')
print(list)

for i in list:
    print(chr(i+64), end=' ')
de_list = []
for i in list:
    print(chr(i+64-3), end=' ')





