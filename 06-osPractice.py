import os

print(os.getcwd())
print(os.listdir())

# os.mkdir('./test')

# os.makedirs('./test2/test3')

# os.rename('./test', './test_new')
# os.renames('./test2/test3', './test2_new/test3_new')
# os.remove('test2.txt')
# os.remove('test_new')
os.removedirs('test2_new/test3_new')