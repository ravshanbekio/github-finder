from aiogram import Bot, Dispatcher, executor, types
import re
import requests
from bs4 import BeautifulSoup

API_TOKEN = '1795364385:AAGFhdEubCq_nwH_6YQoHom5hQIg3DQU-EQ'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
urls_list = []

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("🖐Welcome to the bot that easily downloads codes from Github! \nJust type a title to 📥upload the code ")

@dp.message_handler()
async def extract_data(message: types.Message):
    await message.answer("⌛️Wanted on Github ... ")
    reg_ex = re.search('(.+)', message.text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = f'https://github.com/search?q={domain}&type='
        result_link = None
    responce = requests.get(f'{url}').text
    soup = BeautifulSoup(responce, 'lxml')
    block = soup.find('div', class_='position-relative js-header-wrapper ')
    all_topics = soup.find_all('div',class_="f4 text-normal")

    for topic in all_topics:
        topic_link = topic.find('a').get('href')
        print(topic_link)
        url = f'https://github.com/{topic_link}'
        download_storage = requests.get(f'{url}').text
        soup = BeautifulSoup(download_storage, 'lxml')
        download_block = soup.find('span', class_='d-none d-md-flex ml-2')
        code = soup.find_all('li',class_='Box-row Box-row--hover-gray p-0')

        for kod in code:
            result_link = kod.find('a', class_='d-flex flex-items-center color-text-primary text-bold no-underline p-3').get('href')
            file_bytes = requests.get(f'https://github.com/{result_link}').content
            with open(f"codes/{domain}.zip",'wb') as file:
                file.write(file_bytes)
            await message.answer(f'✅The code was loaded successfully  \n\nhttps://github.com/{result_link}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)