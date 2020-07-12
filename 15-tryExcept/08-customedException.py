class CustomException(Exception):
    pass

def add(x, y):
    if x < 0 or y < 0:
        raise CustomException('x y 必須大於 0')

try:
    add(1, -5)
except CustomException as e:
    print(e)