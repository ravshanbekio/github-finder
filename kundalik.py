from bs4 import BeautifulSoup
import base64
import requests

session = requests.Session()

url = session.get("https://login.kundalik.com/login")
soup = BeautifulSoup(url.text)
imgs = soup.findAll('img')
for img in imgs:
    print(img)

# payload = {"username":'ravshanbekmadaminov2', "password":'ravshanbekmadaminov123122006'}
# response = session.post("https://login.kundalik.com/login", data = payload)
# print(response.text)
# #save captcha from base64 encoding
# img_data = bytes(imgs[1]['src'][23:],encoding='utf-8')
# with open("olympus_captcha.jpg","wb") as fh:
#     fh.write(base64.decodestring(img_data))
 
# captcha = input("enter captcha:\n")

# #attempt login (password and username removed)
#https:\\login.kundalik.com\captcha\true\id-6b4b92c0450b4a86ba3f8a81a02587f47d
# payload = {"username":'ravshanbekmadaminov2', "password":'ravshanbekmadaminov123122006','captcha':'36625'}
# response = session.post("https://login.kundalik.com/login", data = payload)
# print(response.text)