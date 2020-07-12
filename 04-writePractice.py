a = '測試'
file = open('./test2.txt', 'w', encoding='utf-8')

file.write(a)

file.close()

file = open('./test2.txt', 'a', encoding='utf-8')
file.write(a)
file.write(a)
file.write(a)
file.write(a)
file.write(a)
file.write(a)
file.close()
