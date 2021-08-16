import requests
from bs4 import BeautifulSoup

url = "https://www.op.gg/summoner/userName=%EC%9D%B4%EB%B8%94%EB%A6%BC"

res = requests.get(url)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

user = soup.find("span", attrs={"class":"Name"}).get_text()
rank = soup.find("div", attrs={"class":"TierRank"}).get_text()
point = soup.find("span", attrs={"class":"LeaguePoints"}).get_text().strip()
rate = soup.find("span", attrs={"class":"winratio"}).get_text().replace('Win Ratio','승률')
games_win = soup.find("span", attrs={"class":"wins"}).get_text()
games_loss = soup.find("span", attrs={"class":"losses"}).get_text()
solo_rank = soup.find("div", attrs={"class":"MostChampionContent"}).find_all("div", attrs={"class":"Face"})
kdas = soup.find_all("span", attrs={"class":"KDA"})
champ_win_rates = soup.find_all("div", attrs={"class":"Played"})

kdas_list = []
for kda in kdas:
    kdas_list.append(kda.get_text())

champ_win_rate_percent_list = []
for champ_win_rate in champ_win_rates:
    champ_win_rate_percent = champ_win_rate.find("div", attrs={"class":"WinRatio normal tip"})
    if champ_win_rate_percent == None:
        champ_win_rate_percent = champ_win_rate.find("div", attrs={"class":"WinRatio red tip"})
    champ_win_rate_percent = champ_win_rate_percent.get_text().strip()     # 챔피언 승률
    champ_win_rate_percent_list.append(champ_win_rate_percent)


champ_win_rate_game_list=[]
for champ_win_rate in champ_win_rates:
    champ_win_rate_game = champ_win_rate.find("div", attrs={"class":"Title"})
    champ_win_rate_game = champ_win_rate_game.get_text()  # 챔피언 플레이 수
    champ_win_rate_game_list.append(champ_win_rate_game)
    



most_champs=""
cnt = 1
index = 0 #kda 리스트들 저장때 필요한 인덱스
for champ in solo_rank:
    champ = champ['title']
    champ = champ.lower()
    if champ == "dr. mundo" or ' ' in champ or '\'' in champ:
        champ = champ.replace(' ','')
        champ = champ.replace('.','')
        champ = champ.replace('\'','')
    elif champ == "wukong":
        champ = champ.replace('wukong','monkeyking')    
    f = open("champ2.txt","r")
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','')
        if champ in line:
            kor_champ = line.split(':')
            kor_champ = kor_champ[1]
            kor_champ = kor_champ[1:-2]
            most_champs = most_champs + "{}. ".format(cnt) + kor_champ+ ' / ' + kdas_list[index] + ' / ' + "{}({})".format(champ_win_rate_percent_list[index], champ_win_rate_game_list[index]) + "\n\n"
            cnt = cnt + 1
            index = index+1
#print(most_champs)
            

#########
result = "## 솔로랭크 기준##\n\n"
user_sen = "{} 검색결과 입니다\n\n".format(user)
rank_sen = "티어 : " + rank + point + '\n'
rate_sen = rate+' / ' + games_win + games_loss  + '\n\n'
most_champs = 'Most Champs List\n' + most_champs
#########

result = result + user_sen + rank_sen + rate_sen + most_champs


