#file: 07_variable.py
#desc: 변수에 대하여
from copy import copy

a = [1,2,3]
print(id(a))
b = a
print(id(b))

#del b[2] 
#print(a)  

d= copy(a) # 복사하는데 분리해서 복사해서 참조값이 다르게 나옴
print(id(d))
del d[2]
print(a)