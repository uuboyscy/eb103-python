import json

tmpDict = {
    '001': {
        'name': 'Allen',
        'age': 22,
        'interest': ['music', 'programing']
    },
    '002': {
        'name': 'Ted',
        'age': 25,
        'interest': ['music', 'programing', 'sport']
    }
}

tmpJsonStr = json.dumps(tmpDict)
with open('tmpJson.json', 'w', encoding='utf-8') as f:
    f.write(tmpJsonStr)

with open('tmpJson.json', 'r', encoding='utf-8') as f:
    tmpJsonStr2 = f.read()

print(tmpJsonStr2)
print(type(tmpJsonStr2))

tmpDict2 = json.loads(tmpJsonStr2)
print(tmpDict2)
print(type(tmpDict2))
print(tmpDict2['002']['interest'][2])
