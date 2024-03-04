# file : p57_mailReceive.py
# desc : 메일 수신

import imaplib
import email
from email import policy
import requests
import json

slack_url = 'https://hooks.slack.com/services/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' #깃헙 업로드전 삭제 필요

def sendToSlack(msg):
    header = {'Content-type' : 'application/json'}
    data = {'text' : msg}
    res = requests.post(slack_url, headers=header, data=json.dumps(data))
    if res.status_code == 200: return 'OK'
    else: return 'ERROR'

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject,encode = info[0]
    return subject,encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = 'karlll'
pwd = 'ckdgus1324%%'
res = imap.login(id,pwd)


if res[0] == 'OK':
    imap.select('INBOX')
    resp, data = imap.uid('search',None,'All')
    allEmails = data[0].split()
    lastEmails = allEmails[-5:]

    for mail in lastEmails:
        result, data = imap.uid('fetch',mail,'(RFC822)') # RFC822 : 메시지 표준형식
        rawEmail = data[0][1]
        emailMessage = email.message_from_bytes(rawEmail,policy=policy.default)
        #콘솔출력대신 슬랙메시지로 전송
        emailFrom = str(emailMessage['From'])
        emailDate = str(emailMessage['Date'])
        subject, encode = find_encoding_info(emailMessage['Subject'])
        subject = str(subject)
        if subject.find('중요') >=0:
            slackMessage = f'{emailFrom}\n{emailDate}\n{subject}'
            ret = sendToSlack(slackMessage)
            if ret == 'OK':
                print(f'{subject}메일 슬랙전송 성공!')
            else:
                print(f'{subject}메일 슬랙전송 실패!')
        else:
            print('보낼메시지 없음.')

        # print('=' * 80)
        # print(f'From: {emailMessage['From']}' )
        # print(f'To : {emailMessage['To']}')
        # print(f'Date : {emailMessage['Date']}')
        # subject, encode = find_encoding_info(emailMessage['Subject'])
        # print(f'Subject: {subject}')
        # print('내용 : ')
        # msg = ''
        # if emailMessage.is_multipart(): #첨부파일까지 포함된 메일인가
        #     for part in emailMessage.get_payload():
        #         if part.get_content_type() in ['text/plain','text/html']: #plain과 html 모두 변경되도록 수정!!!
        #             bytes = part.get_payload(decode=True)
        #             encode = part.get_content_charset()
        #             msg = msg+ str(bytes,encode) # 인코딩을 자신의 언어맞춰서 변경
        # else: # multipart 형식이 아닌경우
        #     part = emailMessage.get_payload()     

        # print(msg)

    imap.close()
    imap.logout() #파이썬이 아닌 다른언어에서는 close(), logout()이 필수