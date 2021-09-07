## discord_bot_v3 ##
#chromedriver, champ2.txt, temp폴더 필요

import asyncio
import discord
import requests
from bs4 import BeautifulSoup
import time
import os
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

client = discord.Client()

# 생성된 토큰을 입력해준다.
token = "보안상의 이유로 가립니다."
Line = {'탑':'top', '정글':'jungle', '미드':'mid', '원딜':'adc', '서폿':'support'}


#url = "https://www.op.gg/"
def Site():
    url = "https://www.op.gg/"
    return url


def Search_user(msg): #띄어쓰기 있으면 %20 넣어야함.
    msg = msg.replace(' ', '%20')
    url = 'https://www.op.gg/summoner/userName=' + msg
    return url


def Search_champ(msg):
    msg = msg.split(' ') # [0] : 라인 [1] : 챔피언
    with open('champ2.txt', 'r') as file_data:
        for line in file_data:
            line = line.replace('\n','')
            if msg[1] in line:
                eng_champ = line.split(':')
                eng_champ = eng_champ[0]
                eng_champ = eng_champ[2:-1]
    #print(eng_champ, type(eng_champ))
    #print(Line[msg[0]])
    url = "https://www.op.gg/champion/{}/statistics/{}/build".format(eng_champ, Line[msg[0]])
    return url

def upload_pic(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome('chromedriver.exe', options=options)
    browser.get(url)
    browser.set_window_size(750,800)
    browser.execute_script("window.scrollTo(0, 1850)")
    secs = time.time()
    browser.save_screenshot('./temp/' + str(secs)+'.png')
    file = './temp/' + str(secs)+'.png'
    browser.quit()
    return file
    
def remove(file):
    os.remove(file)


def champ_tier(msg):
    url = "https://www.op.gg/champion/statistics"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    result2=""
    if msg == "탑":
        topchamp = soup.find_all("tbody", attrs={"class":"tabItem champion-trend-tier-TOP"})
    elif msg == "정글":
        topchamp = soup.find_all("tbody", attrs={"class":"tabItem champion-trend-tier-JUNGLE"})
    elif msg == "미드":
        topchamp = soup.find_all("tbody", attrs={"class":"tabItem champion-trend-tier-MID"})
    elif msg == "원딜":
        topchamp = soup.find_all("tbody", attrs={"class":"tabItem champion-trend-tier-ADC"})
    elif msg == "서폿":
        topchamp = soup.find_all("tbody", attrs={"class":"tabItem champion-trend-tier-SUPPORT"})

    for champs in topchamp:
        champs = champs.find_all("div", attrs={"class" : "champion-index-table__name"})
        champs = champs[0:10]
        cnt = 1
        for champ in champs:
            champ = champ.get_text()
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
                    #print("{}. ".format(cnt)+kor_champ)
                    result = "\'{}. ".format(cnt)+kor_champ+"\'\n"
                    cnt = cnt+1
                    result2 = result2 + result
            f.close()
    return result2
        


def user_info(url):
    res = requests.get(url)
    
    soup = BeautifulSoup(res.text, "lxml")
    #print("랭크 뜀")
    try:   #랭크 경험이 있는 경우
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
            champ_win_rate_game = champ_win_rate_game.replace('Played','게임')
            champ_win_rate_game = champ_win_rate_game.replace(' ','')
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
                    most_champs = most_champs + "{}. ".format(cnt) + kor_champ+ '/' + kdas_list[index] + '/' + "{}({})".format(champ_win_rate_percent_list[index], champ_win_rate_game_list[index]) + "\n"
                    cnt = cnt + 1
                    index = index+1
            f.close()
        #print(most_champs)
                        

        #########
        result = "```cs\n## 솔로랭크 기준##\n\n"
        user_sen = "\'{} 검색결과 입니다\'\n\n".format(user)
        rank_sen = "\'티어 : " + rank +' / ' + point + "\'" +'\n'
        rate_sen = "\'" + rate+' / ' + games_win +' '+ games_loss  + "\'" + '\n\n'
        most_champs = '#[ Most Champs List ]#\n' + "\'" + "\n" + most_champs + "\'" + "```"
        #########

        result = result + user_sen + rank_sen + rate_sen + most_champs


    except:   #랭크 경험이 없는 경우
           solo_rank_existence = soup.find("div", attrs={"class":"TierRank unranked"}).get_text().strip()
           #print(solo_rank_existence)
           if solo_rank_existence == "Unranked":
               #print("애송이")
               result = ""
               result = "랭크나 뛰고 와라...애송아....에욱"
    return result

#칼바람 챔프티어 확인
def wind_champ_tier(wind_champ):
    try:
        result = ""
        with open('champ2.txt', 'r') as file_data:
            for line in file_data:
                line = line.replace('\n','')
                if wind_champ in line:
                    eng_champ = line.split(':')
                    eng_champ = eng_champ[0]
                    eng_champ = eng_champ[2:-1]
        url="https://www.op.gg/aram/{}/statistics/450/build".format(eng_champ)
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        champ_tier = soup.find("div", attrs={"class" : "champion-stats-header-info__tier"}).find("b").get_text().strip()
        champ_tier = champ_tier.split(' ')
        champ_tier = champ_tier[1]
        result = result + champ_tier + ' 티어'
        return result
    
    except:
        result = ""
        result = "챔피언 똑바로 입력 안할래?!\n뭉개버린다잉?"
        return result
        


# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("디스코드 봇을 가동합니다!")
    print("Bot Name : "+client.user.name)
    print("Start!")
    #print(client.user.id)
    

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if message.content.lower() == "help":
        help_msg = message.channel

        msg = "```cs\n# 사용법 \n"\
                +"\"- help / 사용법을 알려줌\"\n"\
                +"\"- op.gg / op.gg 접속\"\n"\
                +"\"- !!소환사_이름 / 유저검색\"\n"\
                +"\"- 라인 챔피언 / ex) 탑 가렌\"\n"\
                +"\"- 라인티어 / ex) 미드티어\"\n"\
                +"\"- 칼바람 챔피언이름\"```"


        await help_msg.send(msg)

    if message.content.startswith('!안녕'):
        channel = message.channel
        await channel.send('안녕은 무슨...롤이나 해라')

    if message.content == "원준이":
        channel = message.channel
        await channel.send("롤한다고 바쁘다...부르지마라")

    if message.content == "최원준":
        channel = message.channel
        await channel.send("응애 나 애기 원준..롤하고싶어")

    if message.content == "권용우":
        channel = message.channel
        await channel.send("용우 머머리야 어디고? 롤하자")

    if message.content == "김형진":
        channel = message.channel
        await channel.send("아니 김형진 담배값 내놔라")

    if message.content == "배민석":
        channel = message.channel
        await channel.send("민석이 카톡좀 봐라")

    if message.content == "백승원":
        channel = message.channel
        await channel.send("여자친구 생긴거 아니제? 오늘 (샛)별이 참 이쁘네")

    if message.content == "정현석":
        channel = message.channel
        await channel.send("스타말고 롤해라 씹덕아")

    if message.content == "채진수":
        channel = message.channel
        await channel.send("진수는 멋쟁이★")

    if message.content.endswith('머리'):
        channel = message.channel
        await channel.send("용우 그 자체")

    if (message.content.lower()) == "op.gg":
        site = message.channel
        await site.send('옛다! 내가 인심써서 올려준다ㅋ'+'\n'+Site())

    if message.content.startswith('!!'):
        message.content = message.content.split('!!')
        msg = message.content[1]
        search_user = message.channel
        url = Search_user(msg)
        result = user_info(url)
        await search_user.send('아니 내가 왜 검색해줘야함ㅋ (츤츤)'+'\n'+Search_user(msg))
        await search_user.send(result+'\n↑↑자세하게 보려면 위 링크 클릭!')

    if message.content.startswith('탑 ') or message.content.startswith('미드 ') or message.content.startswith('정글 ') or message.content.startswith('원딜 ') or message.content.startswith('서폿 '):
        search_champ = message.channel
        url = Search_champ(message.content)
        await search_champ.send('3초만 기다려 달라구...올려줄게....에욱')
        file = upload_pic(url)
        await search_champ.send('{} 이거 많이 해본거 맞냐??... 불안하다..★'.format(message.content)+"\n"+Search_champ(message.content))
        await search_champ.send(file=discord.File(file))
        remove(file)
        
    if message.content == "탑티어" or message.content == "미드티어" or message.content == "정글티어" or message.content == "원딜티어" or message.content == "서폿티어":
        msg = message.content.split("티어")
        msg = msg[0]
        line_tier = message.channel
        await line_tier.send('```cs\n# '+message.content+' hot 10 champs #\n'+champ_tier(msg)+"```")


    if message.content.startswith('칼바람 '):
        msg = message.content.split(" ")
        wind_champ = msg[1]
        result = wind_champ_tier(wind_champ)
        cal_tier = message.channel
        await cal_tier.send(result)
        

if __name__ == "__main__":
    client.run(token)

