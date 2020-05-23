import base64, imaplib, email, re, os
import getpass
from bs4 import BeautifulSoup
from bs4 import Comment
import sqlite3
import pandas 
from integration import *

user = 'rakshantha17@gmail.com'
password = 'raksha123*'
imap_url = 'imap.gmail.com'
con = imaplib.IMAP4_SSL(imap_url)  
  
# logging the user in 
con.login(user, password)
con.select('inbox')

result, data = con.uid('search', None, "ALL") # search and return uids instead
latest_email_uid = data[0].split()[-1]
result, data = con.uid('fetch', latest_email_uid, '(RFC822)')
raw_email = data[0][1]
email_message = email.message_from_bytes(raw_email)
#### parsing email
sender = email_message['From']
date = email_message['Date']
subject = email_message['Subject']

print('To:', email_message['To'])
print('Sent from:', email_message['From'])
print('Date:', email_message['Date'])
print ('Subject:', email_message['Subject'])
print('*'*69)
cleantext=email_message.get_payload()[0].get_payload()
def Find(string): 
    # findall() has been used  
    # with valid conditions for urls in string 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
    return url 
url=Find(cleantext)
urls = [] 
for i in url: 
    if i not in urls: 
        urls.append(i)
print(urls)
print('*'*30, 'MESSAGE', '*'*30)
#print(string)
text_prob,text_pred = text_prediction(cleantext)
print(text_prob)
if len(urls) == 0:
	url_prob = 0
	url_pred=0
else:
	url_prob,url_pred = url_prediction(urls)

print(url_prob)
def is_phish(text_pred,url_pred,text_prob,url_prob):
    if(text_pred==1) and (url_pred==1):
        phishing = 1
    elif(text_pred==1) and (url_pred==0):
        if(text_prob>0.97):
            phishing = 1
        else:
            phishing = 0
    elif(text_pred==0) and (url_pred==1):
        if(url_prob>0.97):
            phishing = 1
        else:
            phishing = 0
    else:
        phishing = 0
    return phishing

phishing = is_phish(text_pred,url_pred,text_prob,url_prob)
print("final classify" +str(phishing))
conn = sqlite3.connect('email_db.db')
conn.execute('''INSERT INTO EMAIL (SENDER,SUBJECT,DATE,MESSAGE_BODY,PHISHING,TEXT_PHISHING,URL_PHISHING)
VALUES (?,?,?,?,?,?,?)''',(sender,subject,date,cleantext,int(phishing),int(text_pred),int(url_pred)));
conn.commit()
conn.close()