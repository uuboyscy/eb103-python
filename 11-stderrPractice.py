import sys

a = [1,2,3]
sys.stderr = open('testerr.txt', 'w')
# print(a[3])
print(sys.stderr)
sys.stderr = sys.__stderr__
print(sys.stderr)