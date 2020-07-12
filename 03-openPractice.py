print('read() :')
file = open('./test.txt', 'r', encoding='utf-8')

testStr = file.read()
print(testStr)

file.close()

print('readline() :')

file = open('./test.txt', 'r', encoding='utf-8')
line = file.readline()
print('第一列', line)
line = file.readline()
print('第二列', line)

print('readlines() :')

file = open('./test.txt', 'r', encoding='utf-8')
line = file.readlines()
print(line)
