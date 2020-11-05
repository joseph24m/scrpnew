from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests
import time
import datetime
#import telepot
import telegram

token = '1467390691:AAHbu2FapGkiXhRyNAGdi00wcK2IzAO1Clk'
#bot = telepot.Bot(token)
bot = telegram.Bot(token=token)

def get_data():
    global prev_date_time
    site = 'http://www.televideo.rai.it/televideo/pub/rss102.xml'
    op = urlopen(site)
    rd = op.read()
    op.close()
    sp_page = soup(rd, 'xml')
    news_list = sp_page.find_all('item')
    for news in news_list:
                         
        if prev_date_time and prev_date_time >= datetime.datetime.strptime(news.pubDate.text, '%a, %d %b %Y %H:%M:%S %z'):
            break
        print(news.title.text)
        bot.send_message('-1001335964270', news.title.text)
        #bot.sendMessage('1012894664', news.title.text)
        #print(news.pubDate.text)
        #print('-'*60)

    if news_list:
        prev_date_time = datetime.datetime.strptime(news_list[0].pubDate.text, '%a, %d %b %Y %H:%M:%S %z')

prev_date_time = None 
                                                                                                    
while True:
    get_data()
    time.sleep(100)
