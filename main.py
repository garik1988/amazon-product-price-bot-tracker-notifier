import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
from datetime import datetime
import lxml
time_now=datetime.now()
hour_now=int (time_now.hour) #Time right now
minutes_now=int (time_now.minute) #minutes right now
what_hour_to_check_and_send_email=14 #currently set to 14pm
what_minutes_to_check_and_send_email=00
if hour_now==what_minutes_to_check_and_send_email and what_minutes_to_check_and_send_email == what_minutes_to_check_and_send_email:
        my_email = "your smtp login email"
        passw = "your smtp app password"
        reciever_email="the email that notifications will go"
        connection =SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=passw)

        # PRODUCT URL
        AMAZON_PRODUCT_URL= "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
        #Http request header
        header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                "Accept-Language":"en-US,en;q=0.5"}
        #get request
        response=requests.get(url=AMAZON_PRODUCT_URL, headers=header)

        response.raise_for_status()

        html=response.text

        #initialise BS4
        soup=BeautifulSoup(html,'lxml')

        #PRICE HOLDER
        product_price=soup.find(name="span", class_="a-offscreen")
        #PRICE TO FLOAT
        product_price=float (product_price.string[1::])
        #PRODUCT NAME HOLDER & CONVERT TO STRING
        product_title=soup.find(name="span", id="productTitle").string
        # FIXING ENCODING ISSUES
        product_title=product_title.encode("ascii", errors='ignore')
        product_title=product_title.decode("ascii")

        desired_price_target=100 #at what maximum price send the email
        if product_price<desired_price_target:
                connection.sendmail(from_addr=my_email, msg=f"Subject:Price is {product_price} buy now!\n\n{product_title.strip()} is now:${product_price}\n{AMAZON_PRODUCT_URL}",
                                    to_addrs=reciever_email)
