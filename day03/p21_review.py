# file: p21_review.py

# Q7
f = open('test.txt','w')
f.write('Life is too short\n you need java')
f.close() 

f= open('test.txt','r') 
body = f.read()
f.close()
body =body.replace('java','python')
f = open('test.txt','w')
f.write(body)
f.close()

#Q7 같은 문제 (메모장으로 test.txt를 만들었을 경우)
f = open('./day03/test.txt', mode ='r',encoding='utf-8')
body = f.read() #문자열로 리턴(단 read는 텍스트가 길면 문장이 잘려서 나온다)        #body=f.readlines()             #결과 리스트로 리턴
f.close()
body = body.replace('java','python')                                                 #body =[body[0],body[1].replace('java,'python')]
f=open('./day03/test.txt',mode='w',encoding='utf-8')
f.write(body)                                                                        #f.write(body[0]+body[1])
f.close()
