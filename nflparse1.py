import os
import requests  #__version__ = '2.18.4'
from bs4 import BeautifulSoup #__version__ = "4.0.0b"
import re

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
 #url_nfl = 'http://www.nfl.com/scores'
 url_nfl = 'http://www.nfl.com/scores/2017/REG9'

 url_powerrankings = 'https://www.cbssports.com/nfl/powerrankings/'

 url_espn = 'http://www.espn.com/nfl/picks/_/week/8'
 url_cbs = 'https://www.cbssports.com/nfl/features/writers/expert/picks/straight-up/8'


 url_bwin = 'https://www.bwin.com/'
 headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
 }
 r = requests.get(url_nfl, headers=headers)
 with open('scores.html', 'w') as output_file:
  output_file.write(r.text)
 r = requests.get(url_powerrankings , headers=headers)
 with open('power.html', 'w') as output_file:
  output_file.write(r.text)
 r = requests.get(url_espn, headers=headers)
 with open('espn.html', 'w') as output_file:
  output_file.write(r.text)

 try:
  r = requests.get(url_cbs, headers=headers, verify=False, timeout=(10, 1))
 except requests.exceptions.ReadTimeout:
    print('Oops. Read timeout occured')
 except requests.exceptions.ConnectTimeout:
    print('Oops. Connection timeout occured!')
 with open('cbs.html', 'w') as output_file:
  output_file.write(r.text)

def find_week_games():
    nflsite_1 = open('scores.html', 'r')
    my_string = nflsite_1.read()

    save_file(directory_data + 'nf1.txt', my_string)

    soup = BeautifulSoup(my_string, 'html.parser')
    week_scores = soup.find(id="score-boxes")
    game_team = week_scores.find_all('div', attrs={"class":"new-score-box"})

    for i in range(0, len(game_team)):
        tonight = game_team[i]

        away_team = tonight.find('div', attrs={"class":"away-team"})
        away_name = away_team.find('p', attrs={"class":"team-name"}).get_text()
        away_score = away_team.find('p', attrs={"class":"total-score"}).get_text()
        away_record = away_team.find('p', attrs={"class":"team-record"}).get_text()

        if away_team.find('p', attrs={"class": "quarters-score"}) is None:
            quarters_score = 0
        else:
            quarters_score = 1
            score_first_qt = away_team.find('span', attrs={"class": "first-qt"}).get_text()
            score_second_qt = away_team.find('span', attrs={"class": "second-qt"}).get_text()
            score_third_qt = away_team.find('span', attrs={"class": "third-qt"}).get_text()
            score_fourth_qt = away_team.find('span', attrs={"class": "fourth-qt"}).get_text()
            score_ot_qt = away_team.find('span', attrs={"class": "ot-qt"}).get_text()

        print(away_name)
        print(away_record.strip())
        print(away_score.strip())
        if int(quarters_score) > 0:
          print(score_first_qt + ' ' + score_second_qt + ' ' + score_third_qt + ' ' + score_fourth_qt + ' ' + score_ot_qt )
        else:
          print('_ ' + '_ ' + '_ ' + '_ ')

        home_team = tonight.find('div', attrs={"class":"home-team"})
        home_name =  home_team.find('p', attrs={"class":"team-name"}).get_text()
        home_score =  home_team.find('p', attrs={"class":"total-score"}).get_text()
        home_record = home_team.find('p', attrs={"class":"team-record"}).get_text()

        if home_team.find('p', attrs={"class": "quarters-score"}) is None:
            quarters_score = 0
        else:
            quarters_score = 1
            score_first_qt = home_team.find('span', attrs={"class": "first-qt"}).get_text()
            score_second_qt = home_team.find('span', attrs={"class": "second-qt"}).get_text()
            score_third_qt = home_team.find('span', attrs={"class": "third-qt"}).get_text()
            score_fourth_qt = home_team.find('span', attrs={"class": "fourth-qt"}).get_text()
            score_ot_qt = home_team.find('span', attrs={"class": "ot-qt"}).get_text()

        print(home_name)
        print(home_record.strip())
        print(home_score.strip())
        if int(quarters_score) > 0:
          print(score_first_qt + ' ' + score_second_qt + ' ' + score_third_qt + ' ' + score_fourth_qt + ' ' + score_ot_qt )
        else:
          print('_ ' + '_ ' + '_ ' + '_ ')

def power_rankings():
    nflsite_1 = open('power.html', 'r')
    my_string = nflsite_1.read()

    soup = BeautifulSoup(my_string, 'html.parser')
    week_power = soup.find("div", attrs={"class":"table-wrapper"})
    game_team = week_power.find_all('tr', attrs={"class":"player-rankings-stats"})

    for i in range(0, len(game_team)):
        tonight = game_team[i]

        team_rank = tonight.find('span', attrs={"class":"rank"}).get_text()

        if tonight.find('td', attrs={"class": "cell-left change-up"}) is None:
             team_rank_up = 0
        else:
             team_rank_up = tonight.find('td', attrs={"class": "cell-left change-up"}).get_text()

        if tonight.find('td', attrs={"class": "cell-left change-down"})  is None:
             team_rank_down = 0
        else:
             team_rank_down = tonight.find('td', attrs={"class": "cell-left change-down"}).get_text()

        team_stats = tonight.find_all('td', attrs={"class": "cell-left"})
        team_stat = team_stats[1].get_text()

        team_name = tonight.find('td', attrs={"class":"cell-left team"}).get_text()
        team_comment = tonight.find('td', attrs={"class":"cell-left dek"}).get_text()

        print(team_rank.strip())

        if int(team_rank_up) > 0:
            print('+' + team_rank_up.strip())
        elif int(team_rank_down) > 0:
            print('-' + team_rank_down.strip())
        else:
            print('`')
        print(team_name.strip())
        print(team_stat.strip())
        print(team_comment.strip())

def espn_read():
    espn_1 = open('espn.html', 'r')
    my_string = espn_1.read()

    soup = BeautifulSoup(my_string, 'html.parser')
    week_pick_espn = soup.find("table", attrs={"class": "tablehead"})
    game_pick = week_pick_espn.find_all('tr', attrs={"class": re.compile("row team-")})

    for i in range(0, len(game_pick)):
        tonight = game_pick[i]
        game_day_pick = tonight.find_all('div', attrs={"class": re.compile("teampick logo")})
        for j in range(0, len(game_day_pick)):
            topick = game_day_pick[j]
            print(game_day_pick[j].get_text())
        print('---')


if __name__ == '__main__':
    ensure_dir(directory_data)
    #GetUrl()
    power_rankings()
    find_week_games()
    espn_read()

