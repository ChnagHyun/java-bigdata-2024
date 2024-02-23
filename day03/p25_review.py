# file: 25_review.py

#Q1
def is_odd(number):
    if number %2 == 1: 
        return True
    else:
        return False
print(is_odd(3))


#Q2
def avg_numbers(*args):
    result = 0
    for i in args:
        result +=i
        return result/len(args)

avg_numbers(1, 2)
avg_numbers(1,2,3,4,5)


#Q3 
input1 = input('첫 번째 숫자를 입력하세요:')
input2 = input('두 번째 숫자를 입력하세요:')

total = int(input1) + int(input2)
print('두 수의 합은 %s입니다' %total)


#Q4
print('you', 'need', 'python')


#Q5
f1 = open('test1.txt', 'w')
f1.write('Life is too short')
f1.close()

f2 = open('test1.txt', 'r')
print(f2.read())
f2.close() 


#Q6
user_input = input('저장할 내용을 입력하세요:')
f = open('test1.txt',mode='a',encoding='utf-8')
f.write(user_input)
f.write('\n')
f.close()