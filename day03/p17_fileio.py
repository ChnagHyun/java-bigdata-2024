# file: p17_fileio.py
# desc : 파일 입출력 학습

# 컴퓨터에서 열면 무조건 닫아야 하는 것
# 1. 파일 open(), close() / 파이썬에서만 안닫아도 크게 지장없다.
# 2. 네트워크 open(), close() 
# 3. DB open(), close()

# 언어체계 추가 ASCII(한글cp949), 유니코드(utf-8)
# 상대경로, 절대경로
# 12행 mode'w'는 매번 새로 파일 생성, 'a'는 기존파일에 내용 추가
# 로그 등을 남길떈 a로 작업해야한다.
f = open('./day03/sample.txt', mode = 'a', encoding='utf-8')
# 파일쓰기 진행
f.write('안녕하세요. 파이썬.\n ') # 한줄 내리기시 \n 붙일것
f.write('모두 화이팅!!\n')
f.close() # 파이썬에서만 옵션, 다른언어에서는 무조건 close()를 해줘야한다.