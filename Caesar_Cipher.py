def encrypt():
    list = []
    alpha = input('알파벳을 입력해주세요.').upper()

    for i in alpha:
        list.append((ord(i)-64)+3)
    for i in list:
        print(chr(i+64), end=' ')
    print('\n')

def decrypt():
    list = []
    alpha = input('알파벳을 입력해주세요.').upper()

    for i in alpha:
        list.append((ord(i)-64)-3)
    for i in list:
        print(chr(i+64), end=' ')
    print('\n')

if __name__ == "__main__":
    print('작업을 선택하세요')

    while True:
        i = input('1.암호화 2.복호화 3.종료')

        if i == '1':
            encrypt()
        elif i == '2':
            decrypt()
        elif i == '3':
            break
        else:
            print('잘못된 입력입니다')


