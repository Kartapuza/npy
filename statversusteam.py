import os
import requests  #__version__ = '2.18.4'
from bs4 import BeautifulSoup #__version__ = "4.0.0b"
import re
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def Load_Settings():
    global url_scores_stat, url_team_stat, url_team_game_logs
    url_scores_stat = url_team_stat = url_team_game_logs = 'none'
    settings_1 = open('settingsstat.txt', 'r')
    my_string = settings_1.readlines()
    if my_string[0].strip() == '1':
        url_scores_stat = my_string[1].strip()
    else: url_scores_stat = 'none'

    if my_string[2].strip() == '1':
        url_team_stat = my_string[3].strip()
    else:
        url_team_stat = 'none'

    if my_string[4].strip() == '1':
        url_team_game_logs = my_string[5].strip()
    else:
        url_team_game_logs = 'none'

def GetUrl():
 headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
 }
 if len(url_scores_stat) > 5:
    r = requests.get(url_scores_stat, headers=headers)
    with open('statsall.html', 'w', encoding='utf-8') as output_file:
        output_file.write(r.text)

 if len(url_team_stat) > 5:
     r = requests.get(url_team_stat, headers=headers)
     with open('statsteam.html', 'w', encoding='utf-8') as output_file:
         output_file.write(r.text)

 if len(url_team_game_logs) > 5:
     r = requests.get(url_team_game_logs, headers=headers)
     with open('statsteamgamelog.html', 'w', encoding='utf-8') as output_file:
         output_file.write(r.text)

def Read_All_Stats():
    stat_1 = open('statsall.html', 'r')
    my_string = stat_1.read()

    soup = BeautifulSoup(my_string, 'html.parser')
    stat_all_read = soup.find("div", attrs={"id": "chalk_stats"})
    allgame_stats = stat_all_read.find_all('td', attrs={"class": re.compile('(team|score|time)')})
    allgame_team_name =  stat_all_read.find_all('td', attrs={"class": "team"})
    allgame_team_score = stat_all_read.find_all('td', attrs={"class": "score"})
    allgame_team_time = stat_all_read.find_all('td', attrs={"class": "time"})

    for i in range(0, len(allgame_team_name)):
        team_link1A2B = allgame_team_name[i].find_all('a')
        for j in range(0, len(team_link1A2B)):
            team_link1A = team_link1A2B[0].get('href')
            team_link2B = team_link1A2B[1].get('href')
        print(allgame_team_name[i].get_text().strip())
        print(allgame_team_score[i].get_text().strip())
        print(allgame_team_time[i].get_text().strip())
        print(team_link1A)
        print(team_link2B)
        team_link1A = team_link2B = ''
        print('s--')

def Read_Stats_Team():
    stat_2 = open('statsteam.html', 'r')
    my_string2 = stat_2.read()
    soup = BeautifulSoup(my_string2, 'html.parser')
    team_city = soup.find('div', attrs={"class": "team-city"}).get_text()
    team_nickname = soup.find('div', attrs={"class": "team-nickname"}).get_text()
    team_record = soup.find('div', attrs={"class": "team-record"}).get_text()
    print(team_city)
    print(team_nickname)
    print(team_record)
    print('ls-')
    last5games = soup.find("table", attrs={"class": "chalk last5 base-table base-table-sortable"})
    last5_game_date = last5games.find_all('td', attrs={"class": "game_date"})
    last5_result = last5games.find_all('td', attrs={"class": "result"})
    last5_line = last5games.find_all('td', attrs={"class": "line"})
    last5_total = last5games.find_all('td', attrs={"class": "total"})
    last5_ats_result = last5games.find_all('td', attrs={"class": "ats_result"})
    last5_ou_result = last5games.find_all('td', attrs={"class": "ou_result"})
    for i in range(0, len(last5_result)):
        print(last5_game_date[i].get_text().strip(), ';', last5_result[i].get_text().strip(), ';',
              last5_line[i].get_text().strip(), ';', last5_total[i].get_text().strip(), ';',
              last5_ats_result[i].get_text().strip(), ';', last5_ou_result[i].get_text().strip())
    print('st-')
    big_statistic_team = soup.find("table", attrs={"class": "chalk team-stats base-table base-table-sortable"})
    big_statistic_team_title =  big_statistic_team.find_all('td', attrs={"class": "title"})
    big_statistic_team_stat1 = big_statistic_team.find_all('td', attrs={"class": "stat1"})
    big_statistic_team_stat1_rank = big_statistic_team.find_all('td', attrs={"class": "stat1_rank"})
    for i in range(0, len(big_statistic_team_title)):
        print(big_statistic_team_title[i].get_text().strip(), ';', big_statistic_team_stat1[i].get_text().strip(), ';',
              big_statistic_team_stat1_rank[i].get_text().strip())

def Read_Team_games_log():
    stat_3 = open('statsteamgamelog.html', 'r')
    my_string3 = stat_3.read()
    soup = BeautifulSoup(my_string3, 'html.parser')

    event_data_list = soup.find_all('td', attrs={"class": "event_date"})
    event_data_Opponent = soup.find_all('td', attrs={"class": "opponent"})
    event_data_Type = soup.find_all('td', attrs={"class": "game_type"})
    event_data_Result = soup.find_all('td', attrs={"class": "result"})
    event_data_Score = soup.find_all('td', attrs={"class": "score"})
    event_data_ATS = soup.find_all('td', attrs={"class": "ats_result"})
    event_data_closing_spread = soup.find_all('td', attrs={"class": "closing_spread"})
    event_data_ou_result = soup.find_all('td', attrs={"class": "ou_result"})
    event_data_closing_total = soup.find_all('td', attrs={"class": "closing_total"})
    event_data_preview_available = soup.find_all('td', attrs={"class": "preview_available"})
    event_data_preview_recap_available = soup.find_all('td', attrs={"class": "recap_available"})
    for i in range(0, len(event_data_list)):
        print(event_data_list[i].text, ';',event_data_Opponent[i].text.strip(), ';',event_data_Type[i].text, ';',
              event_data_Result[i].text, ';',event_data_Score[i].text, ';',event_data_ATS[i].text, ';',
              event_data_closing_spread[i].text, ';',event_data_ou_result[i].text, ';',event_data_closing_total[i].text, ';',
              event_data_preview_available[i].text, ';',event_data_preview_recap_available[i].text)

if __name__ == '__main__':
    Load_Settings()
    GetUrl()
    if len(url_scores_stat) > 5:
        sys.stdout = open('resultstat.out', 'w')
        Read_All_Stats()
    if len(url_team_stat) > 5:
        sys.stdout = open('resultstatteam.out', 'w')
        Read_Stats_Team()
    if len(url_team_game_logs) > 5:
        sys.stdout = open('resultstatteamgamelogs.out', 'w')
        Read_Team_games_log()
