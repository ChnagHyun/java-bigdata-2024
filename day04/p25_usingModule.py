# file: p25_usingModule.py
# desc: 모듈 사용

import calc as c #나는 calc.py를 사용할래       # calc라는 이름이 길어서  c라는 이름을 만들었다
from calc import mul                            #mul()함수명만 쓰면 됨
from calc import mul as mult                    #mult라는 이름을 만듬

from Math import Math                           #from Math는 모듈(파일이름) import Math는 클래스 이름

from day03.p22_carClass import Car              #디렉토리(모듈묶음: 패키지).모듈명

if __name__ =='__main__' :                       ##java void main()과 동일

    result = c.mul(10,7)                            #c라는 이름을 안만들었으면 result = calc.mul(10,7)라고 작성
    result1 = mul(10,7)                             #5행에서 calc에서 mul을 찾기 때문에 mul만 작성해도 값이 출력
    result2 = mult(10,7)                            #5행에서 mul의 이름을 mult라고 만들었다
    print(result)
    print(result1)
    print(result2)

    print(__name__) #__main__ = 나는 메인엔트리야

    myMath=Math()
    print(myMath.solv(10))