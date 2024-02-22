# file :p15_function.py
# desc : 함수 학습


def funcName():
    pass

def plus(a,b): #매개변수도 리턴값도 있다.
    res = a+b
    return res

def minus(a,b): #매개변수는 있고 리턴값은 없다
    res = a-b
    print(res)

def multi(): #매개 변수는 없고 리턴값은 있다
    global a,c #밖에 있는 전역 변수 a와 c를 사용하겠다
    res = a * c
    return res

def devide():
    global a,c
    print(a/c)



def power(a,b=10):
    res = a**b
    return res

#def power(a=2,b): 이건 안 됨. 기본 인수를 지정할 떄는 뒤에서부터

## 동적 매개 변수
def plus_many(*items):
    result =0
    for item in items:
        result += item
    return result

print(power(2,3))
print(power(2,))
a = 10
c = 4
print(plus(a,c))

print(multi())

devide()

print(plus_many(1,2))
print(plus_many(1,2,3))


def calcurator(mode, *args):
    if mode == 'a':
        result = 0
        for i in args:
            result += i
    elif mode == 'n':
        result = args[0]
        for i in args[1:]:
            result -= i
    elif mode == 'm':
        result = 1
        for i in args:
            result *= i
    elif mode == 'd':
        result = args[0]
        for i in args[1:]:
            result /= i
    return result

print(calcurator('a',1,2,3,45))
print(calcurator('n',100,10,10,5,5,4))
print(calcurator('m',2,2,2,2,2))
print(calcurator('d',100,5,4,5))

def print_kwargs(**items): #키워드 매개변수. 딕셔너리를 생성
    print(items)

print_kwargs(name='Peter Parker', age =18, weapon='web shooter')

#리턴을 한번에 여러개(두개이상) 리턴할수 있다. 튜플로 리턴한다.
def calc2(a,b):
    res1 = a+ b
    res2 = a-b
    res3 = a*b
    res4 = a/b
    return res1, res2, res3, res4
a, b, c, d = calc2(3, 4)

print(a, b, c, d)

## 익명함수 람다함수
add = lambda a, b : a+b #람다함수 끝
print(add(5,4))

