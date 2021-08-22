import requests
import pyautogui
import pyperclip
from bs4 import BeautifulSoup
import json

def scrape_page(url):

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    r = requests.get(url, headers=headers)
    html = BeautifulSoup(r.content, 'html.parser')
    links = []
    for a in html.find_all('a', href=True):
        if (not a['href'].startswith("#")):
            if a['href'].startswith("https://"):
                a['href'] = a['href'][8:]
                
            links.append(a['href'])
            
           
    # json_format = json.dumps(links)
    
    return links


    # print(json_format)

# scrape_page("https://stackoverflow.com") 

# def remove_href(links): #to send to cloud functions
#     for a in links: 
#         a.removeprefix('https://')
# print(json.dumps(links))
# remove_href(links)

