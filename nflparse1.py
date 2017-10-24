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

def find_week_games():
    nflsite_1 = open('test.html', 'r')
    my_string = nflsite_1.read()

    save_file(directory_data + 'nf1.txt', my_string)

    soup = BeautifulSoup(my_string, 'html.parser')
    week_scores = soup.find(id="score-boxes")
    
    game_team = week_scores.find_all(class_="new-score-box")
    tonight = game_team[0]
    #print(tonight.prettify())

    away_team = tonight.find(class_="away-team")
    period = away_team.find(class_="team-name").get_text()
    short_desc = away_team.find(class_="total-score").get_text()
    temp = away_team.find(class_="team-record").get_text()

    print(period)
    print(short_desc)
    print(temp)

    home_team = tonight.find(class_="home-team")
    period = home_team.find(class_="team-name").get_text()
    short_desc = home_team.find(class_="total-score").get_text()
    temp = home_team.find(class_="team-record").get_text()

    print(period)
    print(short_desc)
    print(temp)


if __name__ == '__main__':
    ensure_dir(directory_data)
    #GetUrl()
    find_week_games()
