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

    return sum

print(add(5, 8))
print(add(5, '8'))
print(add(5, 'asasdasd'))