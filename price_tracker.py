from bs4 import BeautifulSoup
from email_alert import notify
from threading import Timer
import requests

URL = input("Enter the Amazon Product Link :\n")
affordable_price = int(input("Enter the price at which you are willing to buy : "))
User_Email_ID = input("E-mail id at which you would be notify : ")
print()
print(f"You will be notified on {User_Email_ID} when price drops ")
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"}

def check_price():
    r = requests.get(URL, headers=header)
    soup = BeautifulSoup(r.content, 'lxml')
    product_title = soup.find('span',id="productTitle").text.strip()
    product_price = soup.find('span', class_ = 'a-price-whole').text.replace(".", "")
    product_price = product_price.replace(",", "")
    product_price = float(product_price)

    if product_price <= affordable_price:
        notify(product_title, URL, User_Email_ID)
        return
    
    else:
        print("You cannot afford this item")

    Timer(60, check_price).start()

check_price()