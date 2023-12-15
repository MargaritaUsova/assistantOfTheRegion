import requests
from bs4 import BeautifulSoup
import pickle

def parse_website(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Ошибка при получении страницы. Код ответа: {response.status_code}")
        return None
    soup = BeautifulSoup(response.content, 'html.parser')
    resolutions_blocks = soup.find_all('div', class_='postanovlenie')
    resolutions_dict = {}
    for block in resolutions_blocks:
        itemsList = block.find_all('div', class_='item')
        for item in itemsList:
            title = item.find('div', class_= 'title').text.strip()
            page_link = "https://www.алмазный-край.рф"+item.find('a')['href']
            resolutions_dict[title] = f"{page_link}"
    return resolutions_dict

url = "https://www.алмазный-край.рф/administratsiya-mo/postanovleniya-i-rasporyazheniya-glavy-mr/"
resolutions = parse_website(url)
# if resolutions:
#     for title, link in resolutions.items():
#         print(f"{title}: {link}")


with open('data.txt', 'w') as file:
    for key, value in resolutions.items():
        file.write(f'{key}, {value}\n')