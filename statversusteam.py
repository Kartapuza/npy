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
    global url_scores_stat, url_team_stat
    url_scores_stat = url_team_stat ='none'
    settings_1 = open('settingsstat.txt', 'r')
    my_string = settings_1.readlines()
    if my_string[0].strip() == '1':
        url_scores_stat = my_string[1].strip()
    else: url_scores_stat = 'none'

    if my_string[2].strip() == '1':
        url_team_stat = my_string[3].strip()
    else:
        url_team_stat = 'none'


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
    #stat_team = soup.find("div", attrs={"id": "chalk_stats"})
    team_city = soup.find('div', attrs={"class": "team-city"}).get_text()
    team_nickname = soup.find('div', attrs={"class": "team-nickname"}).get_text()

    print(team_city)
    print(team_nickname)

    #allgame_stats = stat_team.find_all('td', attrs={"class": re.compile('(team|score|time)')})
    #allgame_team_name =  stat_team.find_all('td', attrs={"class": "team"})
    #allgame_team_score = stat_team.find_all('td', attrs={"class": "score"})
    #allgame_team_time = stat_team.find_all('td', attrs={"class": "time"})
    #---


if __name__ == '__main__':
    Load_Settings()
    GetUrl()
    if len(url_scores_stat) > 5:
        sys.stdout = open('resultstat.out', 'w')
        Read_All_Stats()
    if len(url_team_stat) > 5:
        sys.stdout = open('resultstatteam.out', 'w')
        Read_Stats_Team()