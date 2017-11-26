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
    global url_player_stat, url_team_roster
    url_player_stat = url_team_roster = 'none'
    settings_1 = open('settingsplayer.txt', 'r')
    my_string = settings_1.readlines()
    if my_string[0].strip() == '1':
        url_player_stat = my_string[1].strip()
    else: url_player_stat = 'none'

    if my_string[2].strip() == '1':
        url_team_roster = my_string[3].strip()
    else:
        url_team_roster = 'none'

def GetUrl():
 headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
 }
 if len(url_team_roster) > 5:
    r = requests.get(url_team_roster, headers=headers)
    with open('teamroster.html', 'w', encoding='utf-8') as output_file:
        output_file.write(r.text)

 if len(url_player_stat) > 5:
     r = requests.get(url_player_stat, headers=headers)
     with open('statsplayer.html', 'w', encoding='utf-8') as output_file:
         output_file.write(r.text)

def Read_Roster():
    team_roster = open('teamroster.html', 'r')
    my_string2 = team_roster.read()
    soup = BeautifulSoup(my_string2, 'html.parser')
    team_rosters1 = soup.find_all('tr', attrs={"class": "odd"})
    team_rosters2 = soup.find_all('tr', attrs={"class": "even"})
    for i in range(0, len(team_rosters2)):
        team_rosters1_td = team_rosters1[i].find_all('td')
        team_rosters2_td = team_rosters2[i].find_all('td')
        str_tr1 = ''
        for j in range(0, len(team_rosters1_td)):
            str_tr1 = str_tr1 + team_rosters1_td[j].text + ' ; '
        print(str_tr1)

        str_tr2 = ''
        for j in range(0, len(team_rosters2_td)):
            str_tr2 = str_tr2 + team_rosters2_td[j].text + ' ; '
        print(str_tr2)

    if len(team_rosters1)>len(team_rosters2):
        team_rosters1_td = team_rosters1[len(team_rosters1)-1].find_all('td')
        str_tr1 = ''
        for j in range(0, len(team_rosters1_td)):
            str_tr1 = str_tr1 + team_rosters1_td[j].text.strip() + ' ; '
        print(str_tr1)

def Read_Stats_Player():
    team_player = open('statsplayer.html', 'r')
    my_string2 = team_player.read()
    soup = BeautifulSoup(my_string2, 'html.parser')
    team_stats_player = soup.find_all('tr')
    for i in range(0,len(team_stats_player)):
        team_stats_player_hr = team_stats_player[i].find_all('td')
        str_tr1 = ''
        for j in range(0, len(team_stats_player_hr)):
            str_tr1 = str_tr1 + team_stats_player_hr[j].text.strip() + ' ; '
        print(str_tr1)
    print('ps-')



if __name__ == '__main__':
    Load_Settings()
    GetUrl()
    if len(url_team_roster) > 5:
        sys.stdout = open('resultroster.out', 'w')
        Read_Roster()
    if len(url_player_stat) > 5:
        sys.stdout = open('resultstatplayer.out', 'w')
        Read_Stats_Player()