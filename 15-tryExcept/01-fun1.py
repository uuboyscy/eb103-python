def createFile(name):
    with open(name, 'w', encoding='utf-8') as f:
        f.write('123')

createFile('test')
createFile('test1/test')