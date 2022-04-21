import requests
from bs4 import BeautifulSoup
import base64


session = requests.Session()
link = "https://login.kundalik.com/login"

responce = requests.get(link).text
soup = BeautifulSoup(responce)
block = soup.find('div', class_='captcha')
all_images = soup.find_all('div',class_="login__captcha-wrapper col-ms-12 col-xs-12")

for image in all_images:
    image_link = image.find('div').get('id')
    full_link = f'{link}/captcha/true/{image_link}'
    

# url = session.get(f"{full_link}")
# soup2 = BeautifulSoup(url.text)
# block2 = soup2.find('body')
# print(block2)
# imgs = soup2.find('img').get('src')
# print(imgs)

# img_data = bytes(imgs,encoding='utf-8')
# with open("olympus_captcha.jpg","wb") as fh:
#     fh.write(base64.decodestring(img_data))
