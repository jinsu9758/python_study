import requests
from bs4 import BeautifulSoup

url = "https://www.op.gg/champion/statistics"

res = requests.get(url)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

topchamp = soup.find_all("tbody", attrs={"class":"tabItem champion-trend-tier-JUNGLE"}) #JUNGLE, MID, ADC, SUPPORT


for champs in topchamp:
    champs = champs.find_all("div", attrs={"class" : "champion-index-table__name"})
    champs = champs[0:10]
    cnt = 1
    for champ in champs:
        champ = champ.get_text()
        print(champ)
        champ = champ.lower()
        #예외 처리
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
                print("{}. ".format(cnt)+kor_champ)
        cnt = cnt+1

