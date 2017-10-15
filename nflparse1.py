import os
import requests
from bs4 import BeautifulSoup

#Создание структуры каталогов
current_dir = os.getcwd()
directory_data = (current_dir + '\data')

def ensure_dir(directory):
 if not os.path.exists(directory):
    os.makedirs(directory)


def startGrab():
 #подгрузка ресурсов
 url = 'http://www.nfl.com/scores'
 headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
      }
 # времено убрал загрузку 1
 #r = requests.get(url, headers = headers)

 # времено убрал загрузку 1
 #with open('test.html', 'w') as output_file:
 #  output_file.write(r.text)

 #использование локального файла
 nflsite_1 = open('test.html', 'r')
 my_string = nflsite_1.read()

 print(len(my_string))

 # Beautiful Soup
 soup = BeautifulSoup(my_string, 'html.parser')

 letters = soup.find('div', {'class': 'new-score-box'})
 print(len(letters))

 ListP1=list(soup.find_all('p'))
 print(ListP1)
 print(len(ListP1))
 print(soup.find_all('p')[0].get_text())

 new_score = soup.find('p', {'class': 'team-name'})

 # Команды 1 _ 2
 team11 = soup.find('div', {'class': 'new-score-box'})
 team12 = soup.find('div', {'class': 'new-score-box'})

 if team11 == team12:
    print('ok')

 # Beatiful Soup

 team11_away = team11.find('div', {'class': 'away-team'}).find('a').get('href')
 team12_home = team12.find('p', {'class': 'team-name'}).find('a').text
 team12_home_stat = team12.find('p', {'class': 'team-record'}).text

 #print(team12,team11)

 letters = {}
 for element in letters:
    print(element)


if __name__ == '__main__':
    ensure_dir(directory_data)
    startGrab()