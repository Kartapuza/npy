import os
import requests
from bs4 import BeautifulSoup

#Создание структуры каталогов
current_dir = os.getcwd()
directory_data = (current_dir + '\data')

def ensure_dir(directory):
 if not os.path.exists(directory):
    os.makedirs(directory)

def save_file(name_file, lines):
 save_changes = open(name_file, 'w')
 save_changes.writelines(lines)
 save_changes.close()

def GetUrl():
 url = 'http://www.nfl.com/scores'
 headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
 }
 r = requests.get(url, headers=headers)
 with open('test.html', 'w') as output_file:
  output_file.write(r.text)


def startGrab():
 nflsite_1 = open('test.html', 'r')
 my_string = nflsite_1.read()

 print(len(my_string))
 save_file(directory_data + 'nf1.txt', my_string)

 soup = BeautifulSoup(my_string, 'html.parser')

 letters = soup.find('div', {'class': 'new-score-box'})
 print(len(letters))

 ListP1=list(soup.find_all('p'))
 #print(ListP1)
 print(len(ListP1))

 seven_day = soup.find('div', {'class': 'new-score-box'})
 forecast_items = seven_day.find_all(class_="new-score-box")

 short_descs = [sd.get_text() for sd in seven_day.select(".new-score-box .team-name")]
 temps = [t.get_text() for t in seven_day.select(".new-score-box .team-record")]
 #descs = [d["title"] for d in seven_day.select(".new-score-box img")]

 new_score = soup.find('p', {'class': 'team-name'})

 team11 = soup.find('div', {'class': 'new-score-box'})
 team12 = soup.find('div', {'class': 'new-score-box'})

 if team11 == team12:
    print('ok')

 team11_away = team11.find('div', {'class': 'away-team'}).find('a').get('href')
 team12_home = team12.find('p', {'class': 'team-name'}).find('a').text
 team12_home_stat = team12.find('p', {'class': 'team-record'}).text


if __name__ == '__main__':
    ensure_dir(directory_data)
    GetUrl()
    startGrab()