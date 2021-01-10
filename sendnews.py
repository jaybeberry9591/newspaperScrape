import pywhatkit
import requests
from bs4 import BeautifulSoup
import urllib3
import re
from datetime import datetime
import time
import pywhatkit
import json

# Opening JSON file
with open('scraped_english_articles.json') as access_json:
    read_content = json.load(access_json)

# print(type(read_content.get('newspapers').get('bbc').get('articles')))
newspapers = ['bbc', 'thedailystar','banglatribune']

article_list = []


# article_list = read_content.get('newspapers').get('bbc').get('articles')
# print(article_list)
# print(article_list[0])

def sendnews():
    result = []

    for i in article_list:
        values = i.values()
        values_list = list(values)
        listToStr = '\n\n'.join(map(str, values_list))
        result.append(listToStr)
        # for item in result:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        l = current_time.split(':')

        current_hour = l[0]
        current_min = l[1]
        print("Your message will be deliverd @ ", current_hour, " : ", int(current_min) + 3)
        pywhatkit.sendwhatmsg("put phone number", listToStr, int(current_hour), (int(current_min) + 3))
        print("going to sleep for ", (1.1 * 60), " sec\n")
        time.sleep(1.1 * 60)


for newspaper in newspapers:
    article_list = read_content.get('newspapers').get(newspaper).get('articles')
    sendnews()

