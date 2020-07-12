def createFile(name):
    try:
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except FileNotFoundError as e:
        print(e)
        name = name.replace('/', '-')
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except OSError as e:
        print(e.args)
        name = 'ttttttt'
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except Exception as e:
        print(e)
        pass


createFile('test')
createFile('test1/test')
createFile('test?')