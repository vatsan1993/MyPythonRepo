import requests
from bs4 import BeautifulSoup
import smtplib
import time

def checkPrice():
    #url of the product page
    url= "https://www.amazon.in/iBall-Compbook-Aer3-Pentium-13-3-inch/dp/B075K953LQ/ref=sr_1_1?keywords=iball+aer3&qid=1562114894&s=electronics&sr=1-1"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"}

    r= requests.get(url,headers= headers)
    soup= BeautifulSoup(r.content,"html.parser")

    title= soup.find(id="productTitle").get_text()
    print(title.strip())
    price= soup.find(id="priceblock_ourprice").get_text()
    price=price.strip("₹ ")
    price= price.replace(",", "")
    price=(float(price))
    if price<22000: # price threshold that you want
        sendmail()



def sendmail():
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # remember to create a two step authentication in gmail.
    server.login("youremail@gmail.com","password generated from google app passwords")

    # subject and body of mail
    subject= "Price Dropped"
    body = "Check the link https://www.amazon.in/iBall-Compbook-Aer3-Pentium-13-3-inch/dp/B075K953LQ/ref=sr_1_1?keywords=iball+aer3&qid=1562114894&s=electronics&sr=1-1"

    msg= f"Subject:{subject}\n\n {body}"

    server.sendmail("sendermail@gmail.com","yourmail@gmail.com", msg)
    print("Mail sent")

# keeps running for ever but only checks the condition once in a day
while True:
    checkPrice()

    time.sleep(24*60*60)

