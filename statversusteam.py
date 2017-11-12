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
    global url_stat
    url_stat = 'none'
    settings_1 = open('settingsstat.txt', 'r')
    my_string = settings_1.readlines()
    if my_string[0].strip() == '1':
        url_stat = my_string[1].strip()
    else: url_stat = 'none'

def GetUrl():
 headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
 }
 if len(url_stat) > 5:
    r = requests.get(url_stat, headers=headers)
    with open('statsall.html', 'w', encoding='utf-8') as output_file:
        output_file.write(r.text)


def Read_Stat():
    stat_1 = open('statsall.html', 'r')
    my_string = stat_1.read()

    soup = BeautifulSoup(my_string, 'html.parser')
    stat_all_read = soup.find("div", attrs={"id": "chalk_stats"})
    allgame_stats = stat_all_read.find_all('td', attrs={"class": re.compile('(team|score|time)')})
    allgame_team_name =  stat_all_read.find_all('td', attrs={"class": "team"})
    allgame_team_score = stat_all_read.find_all('td', attrs={"class": "score"})
    allgame_team_time = stat_all_read.find_all('td', attrs={"class": "time"})

    for i in range(0, len(allgame_team_name)):
        print(allgame_team_name[i].get_text().strip())
        print(allgame_team_score[i].get_text().strip())
        print(allgame_team_time[i].get_text().strip())
        print('s--')


if __name__ == '__main__':
    sys.stdout = open('resultstat.out', 'w')
    Load_Settings()
    GetUrl()
    Read_Stat()
