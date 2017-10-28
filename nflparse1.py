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
 url_nfl = 'http://www.nfl.com/scores'
 url_powerrankings = 'https://www.cbssports.com/nfl/powerrankings/'
 headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
 }
 r = requests.get(url_nfl, headers=headers)
 with open('scores.html', 'w') as output_file:
  output_file.write(r.text)
 r = requests.get(url_powerrankings , headers=headers)
 with open('power.html', 'w') as output_file:
  output_file.write(r.text)


def find_week_games():
    nflsite_1 = open('scores.html', 'r')
    my_string = nflsite_1.read()

    save_file(directory_data + 'nf1.txt', my_string)

    soup = BeautifulSoup(my_string, 'html.parser')
    week_scores = soup.find(id="score-boxes")
    game_team = week_scores.find_all('div', attrs={"class":"new-score-box"})
    tonight = game_team[0]

    away_team = tonight.find('div', attrs={"class":"away-team"})
    period = away_team.find('p', attrs={"class":"team-name"}).get_text()
    short_desc = away_team.find('p', attrs={"class":"total-score"}).get_text()
    temp = away_team.find('p', attrs={"class":"team-record"}).get_text()

    print(period)
    print(short_desc)
    print(temp)

    home_team = tonight.find('div', attrs={"class":"home-team"})
    period = home_team.find('p', attrs={"class":"team-name"}).get_text()
    short_desc = home_team.find('p', attrs={"class":"total-score"}).get_text()
    temp = home_team.find('p', attrs={"class":"team-record"}).get_text()

    print(period)
    print(short_desc)
    print(temp)

def power_rankings():
    nflsite_1 = open('power.html', 'r')
    my_string = nflsite_1.read()

    soup = BeautifulSoup(my_string, 'html.parser')
    week_power = soup.find("div", attrs={"class":"table-wrapper"})
    game_team = week_power.find_all('tr', attrs={"class":"player-rankings-stats"})

    tonight = game_team[0]

    team_rank = tonight.find('span', attrs={"class":"rank"}).get_text()
    team_name = tonight.find('td', attrs={"class":"cell-left team"}).get_text()
    team_comment = tonight.find('td', attrs={"class":"cell-left dek"}).get_text()

    print(team_rank.strip())
    print(team_name.strip())
    print(team_comment.strip())


if __name__ == '__main__':
    ensure_dir(directory_data)
    #GetUrl()
    power_rankings()
    find_week_games()
