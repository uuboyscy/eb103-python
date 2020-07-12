def add(x, y):
    try:
        sum = x + y
    except TypeError:
        try:
            x = int(x)
            y = int(y)
            sum = x + y
        except:
            sum = 0
    else:
        print('try successfully')
    finally:
        print('fcvbnhtcjvytgtchdhgfcvbgfhgcvnb')

    return sum

print(add(5, 8))
print('===================')
print(add(5, '8'))
print('===================')
print(add(5, 'asasdasd'))