import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Samsung-250GB-Internal-Solid-MZ-76E250BW/dp/B079DTMNWC/ref=sr_1_fkmr1_1?keywords=sony+860+evo+250gb+ssd&qid=1563899684&s=gateway&sr=8-1-fkmr1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()

    price = soup.find(id='priceblock_ourprice').get_text()
    price = price.replace(',', '')
    converted_price = int(float(price[1:6]))
    if(converted_price < 3500):
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('sendermail', 'password')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Samsung-250GB-Internal-Solid-MZ-76E250BW/dp/B079DTMNWC/ref=sr_1_fkmr1_1?keywords=sony+860+evo+250gb+ssd&qid=1563899684&s=gateway&sr=8-1-fkmr1 '

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'sendermail',
        'receivermail',
        msg
    )
    print('Hey Email has been sent!!')

    server.quit()


while(True):
    check_price()
    time.sleep(10)
