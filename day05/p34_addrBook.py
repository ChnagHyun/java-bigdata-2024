# file: p34_addrBook.py
# desc: 콘솔 주소록 프로그램
import os


class Contact: #주소록 클래스
    # 생성자
    def __init__(self,name, phoneNumber, eMail, addr) -> None:
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__eMail = eMail
        self.__addr = addr

# 사용자가 원하는 형태로 출력
    def __str__(self) -> str: #
        res = (f'이  름 : {self.__name}\n'    # 원래 출력 <__main__.Contact object at 0x0000016B505E2150>
               f'핸드폰 : {self.__phoneNumber}\n'
               f'이메일 : {self.__eMail}\n'
               f'주  소 : {self.__addr}')
        return res
    
def setContact(): # 사용자 입력으로 주소록 받기함수
    (name, phoneNumber, eMail, addr) = input('주소록 입력(이름, 핸드폰, 이메일, 주소[구분자/] >)').split('/')
    name=name.strip()
    phoneNumber=phoneNumber.strip()
    eMail=eMail.strip()
    addr=addr.strip()
    # print(f'"{name}","{phoneNumber}","{eMail}","{addr}"')
    contact = Contact(name, phoneNumber, eMail, addr) #매개변수명과 동일하게 로컬변수 이름 지정
    return contact

def clearConsole():
    cmd = 'clear' # macOS, Linux, Unix 명령어
    if os.name in('nt', 'dos'): # window
        cmd = 'cls' #window 명령어

def displayMenu():
    menu = ('주소록 프로그램\n'
            '1. 연락처 추가\n'
            '2. 연락처 출력\n'
            '3. 연락처 삭제\n'
            '4. 종료\n')
    print(menu)
    sel = int(input('메뉴입력 : '))
    return sel

def getContacts(lst):
    for item in lst:
        print(item)

def run():
    #연락처담을 주소록 리스트
    lstContact = []

    clearConsole() # 화면을 클리어
    while True:
        selMenu = displayMenu()
        if selMenu ==1: #연락처 추가라면
            clearConsole()
            contact = setContact()
            lstContact.append(contact)
            #print(lstContact)
            input(); clearConsole()
        elif selMenu == 4:
            break
        else:
            clearConsole()

# def run():
#     first = Contact(name='홍길동', phoneNumber='010-9999-5555', eMail='hgd@naver.com', addr='경성')
#     print(first)

if __name__=='__main__': #메인 엔트리
    print('프로그램 시작')
    run() #메인함수 실행

print('프로그램 종료')