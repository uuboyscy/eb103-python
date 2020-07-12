def createFile(name):
    try:
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except FileNotFoundError:
        name = name.replace('/', '-')
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except OSError:
        name = 'ttttttt'
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except:
        pass


createFile('test')
createFile('test1/test')
createFile('test?')