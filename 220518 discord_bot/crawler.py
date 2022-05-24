from urllib import parse
import requests
from bs4 import BeautifulSoup
import util

#op.gg 헤더 
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '_ol=ko_KR; customLocale=ko_KR; _oul=true',
    'referer': 'https://www.op.gg/',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }



headers2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'lolg_euconsent=nitro; languageBanner_ko_count=2',
    'Host': 'www.leagueofgraphs.com',
    'Referer': 'https://www.leagueofgraphs.com/',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }



Line = {'탑' : 'top', '미드' : 'mid', '정글':'jungle', '원딜':'adc', '서폿':'support'} #op.gg용
Line2 = {'탑' : 'top', '미드' : 'middle', '정글':'jungle', '원딜':'adc', '서폿':'support'} #leagueofgraphs용


Rune = {'결의':'(초록색)', '마법':'(파란색)', '지배':'(빨간색)', '정밀':'(노란색)', '영감':'(하늘색)', '능력치 파편':''}

#########
'''
유저검색시, 정보들을 저장하는 info에 관하여
[url, ## 솔로랭크 기준 ##, ooo검색 결과 입니다, 티어, 승률, 모스트 챔피언 리스트]

'''
#########


#유저 검색 함수 -> 티어 + url + 승률 + 모스트 챔피언
def search_user(user_name):
    url = user_name
    url = "https://www.op.gg/summoners/kr/" + parse.quote(url)
    print(url)
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    info = ['', '', '', '', '', '']

    '''
    with open("test.html", "w", encoding="utf8") as f:
        f.write(res.text)
    '''
    
    soup = BeautifulSoup(res.text, "lxml")

    #솔로랭크 기록이 없는 경우
    if is_ranked(soup):
        tier = what_tier(soup)
        win_rate = win_lose_rate(soup)
        most_champs = search_most_champs(soup)

        
        info[0] = url
        info[1] = "## 솔로랭크 기준 ##"
        info[2] = user_name + " 검색결과입니다." 
        info[3] = "티어 : " + tier
        info[4] = "승률 : " + win_rate
        info[5] = most_champs
        return info

    #솔로랭크 기록이 있는 경우
    else:
        info[0] = url
        info[1] = "## 솔로랭크 기준 ##"
        info[2] = user_name + " 검색결과입니다." 
        info[3] = "솔로랭크 기록이 없습니다!"
        info[4] = ""
        info[5] = ""
        return info
        
#유저검색 -> 언랭인지 아닌지
def is_ranked(soup):
    ranked = soup.find_all("div", attrs={"class":"tier-rank"})
    #print(ranked)
    #솔로랭크 기록이 있음.
    if ranked:
        return True
    # 솔로랭크 기록이 없음.
    return False


#유저검색 -> 티어
def what_tier(soup):
    tier = soup.find("div", attrs={"class":"tier-rank"}).get_text().strip()
    #print(tier)
    return tier


#유저검색 ->  승률
def win_lose_rate(soup):
    win_rate = soup.find("span", attrs={"class":"win-lose"}).get_text().strip()
    #print(win_rate)
    return win_rate

#유저검색 -> 모스트 챔피언
def search_most_champs(soup):
    cnt = len(soup.find_all("div", attrs={"class":"champion-box"}))
    most_champs_lists=[[] for _ in range(cnt)]
    for c in range(cnt):
        most_champs = soup.find_all("div", attrs={"class":"champion-box"})[c]
        most_champs_info = most_champs.find_all("div", attrs={"class":"info"})
        most_champs_name = most_champs.find("div", attrs={"class":"name"}).get_text().strip()
        most_champs_kda = most_champs.find("div", attrs={"class":"kda"}).find("div", attrs={"class":"exxtup1"}).get_text().strip()
        most_champs_win_rate = most_champs.find("div", attrs={"class":"played"}).find("div", attrs={"class":"exxtup0"}).get_text().strip()
        most_champs_cnt = most_champs.find("div", attrs={"class":"played"}).find("div", attrs={"class":"count"}).get_text().strip()

        most_champs_lists[c].append(most_champs_name)
        most_champs_lists[c].append(most_champs_kda)
        most_champs_lists[c].append(most_champs_win_rate)
        most_champs_lists[c].append(most_champs_cnt)
    
    return most_champs_lists


    
#########
'''
챔피언 검색 시, 정보들을 저장하는 info에 관하여
[url, 라인 챔프명 검색결과입니다, 협곡 티어, 상대하기 쉬운 챔프, 상대하기 어려운 챔프, 룬]

'''
#########

# 챔피언 검색
def search_champ(cmd):
    line = cmd[1:].split(' ')[0]
    line_len = len(line)
    champ_name = cmd[line_len+2:]
    info = ['', '', '', '', '', '']
    
    url = "https://www.op.gg/champions/"+util.champs_db[champ_name]+"/"+Line[line]+"/build"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    
    print(url)


    url2 = "https://www.leagueofgraphs.com/ko/champions/counters/"+util.champs_db[champ_name] + "/" + Line2[line]
    res2 = requests.get(url2, headers=headers2)
    res2.raise_for_status()

    print(url2)
    
    soup = BeautifulSoup(res.text, "lxml")
    soup2 = BeautifulSoup(res2.text, "lxml")
    #https://www.leagueofgraphs.com/ko/

    '''
    with open("test.html", "w", encoding="utf8") as f:
        f.write(res.text)

    with open("test2.html", "w", encoding="utf8") as f:
        f.write(res2.text)
    '''

    #챔피언에 충분한 데이터가 있을 때
    if is_data(soup):
        champ_tier = soup.find("span", attrs={"class":"tier_color"}).get_text()
        victory_champ = soup2.find_all('table')[0].find_all("span", attrs={"class" : "name"})[:3] #챔프 3개만 추출
        counter_champ = soup2.find_all('table')[1].find_all("span", attrs={"class" : "name"})[:3] #챔프 3개만 추출

        info[0] = url
        info[1] = "## " + line + " " + champ_name + " 결과입니다! ##"
        info[2] = "\'티어 : "+ champ_tier + "\'"
        info[3] = v_champ(victory_champ)
        info[4] = c_champ(counter_champ)
        info[5] = search_rune(soup)
        #print(info)
        return info
        
    else:
        victory_champ = soup2.find_all('table')[0].find_all("span", attrs={"class" : "name"})[:3] #챔프 3개만 추출
        counter_champ = soup2.find_all('table')[1].find_all("span", attrs={"class" : "name"})[:3] #챔프 3개만 추출

        info[0] = url
        info[1] = "## " + line + " " + champ_name + " 결과입니다! ##"
        info[2] = "\'데이터가 부족합니다.\'"
        info[3] = v_champ(victory_champ)
        info[4] = c_champ(counter_champ)
        info[5] = search_rune(soup)
        return info


##챔피언 검색 -> 챔피언에 대한 데이터가 충분한지 확인해줍니다.
def is_data(soup):
    avail = soup.find("span", attrs={"class":"tier_color"})
    if avail==None:
        return False
    return True


# 챔피언 검색 -> 상대하기 쉬운 챔피언 데이터 정리를 해주는 함수.
def v_champ(v):
    v_len = len(v)

    if v_len == 0:
        v_str = "\'상대하기 쉬운 챔피언 : 데이터가 없습니다."
    else:
        v_str = "\'상대하기 쉬운 챔피언 : "
        for i in range(v_len):
            v_str += v[i].get_text() + " / "
    return v_str+"\'"


# 챔피언 검색 -> 카운터 챔피언 데이터 정리를 해주는 함수.
def c_champ(c):
    c_len = len(c)
    
    if c_len == 0:
        c_str = "\'상대하기 어려운 챔피언 : 데이터가 없습니다."
    else:
        c_str = "\'상대하기 어려운 챔피언 : "
        for i in range(c_len):
            c_str += c[i].get_text() + " / "
    return c_str+"\'"

        

def search_rune(soup):
    info = []
    
    champ_runes_name = soup.find("table", attrs={"class":"e10jawsm1"}).find("div", attrs={"class":"rune_header"}).find("div", attrs={"class":"name"}).get_text().split(' + ')
    champ_runes_name.append("능력치 파편")
    
    main_rune_list = []
    if champ_runes_name[0] == "지배":
        main_rune_list.append(['X']*4)
        for i in range(2):
            main_rune_list.append(['X']*3)
        main_rune_list.append(['X']*4)

    elif champ_runes_name[0] == "정밀":
        main_rune_list.append(['X']*4)
        for i in range(3):
            main_rune_list.append(['X']*3)

    else:
        main_rune_list = [['X']*3 for _ in range(4)]

    sub_rune_list = [['X']*3 for _ in range(3)]

    ability_rune_list = [['X']*3 for _ in range(3)]

    #class : e495vw31 #총 4개있는데 앞에 2개만 하면됨.
    main_rune_rows = soup.find_all("div", attrs={"class":"e495vw31"})[0].find_all("div", attrs={"class":"row"})[1:]
    sub_rune_rows = soup.find_all("div", attrs={"class":"e495vw31"})[1].find_all("div", attrs={"class":"row"})[1:]
    ability_rune_rows = soup.find("div", attrs={"class":"e14t5af50"}).find_all("div", attrs={"class":"row"})

    #main rune
    for row in range(len(main_rune_rows)):
        choice = main_rune_rows[row].find_all("div", attrs={"class":"e495vw30"})
        for index in range(len(choice)):
            if 'css-1w13bvn' in str(choice[index]) or 'css-l5ga7x' in str(choice[index]):
                main_rune_list[row][index]="O"

    #sub rune
    for row in range(len(sub_rune_rows)):
        choice = sub_rune_rows[row].find_all("div", attrs={"class":"e495vw30"})
        for index in range(len(choice)):
            if 'css-1w13bvn' in str(choice[index]) or 'css-l5ga7x' in str(choice[index]) or 'css-l5ga7x' in str(choice[index]):
                sub_rune_list[row][index]="O"

    #ability rune
    for row in range(len(ability_rune_rows)):
        choice = ability_rune_rows[row].find_all("img")
        for index in range(len(choice)):
            if 'opacity:1' in str(choice[index]):
                ability_rune_list[row][index]="O"

    info.append(main_rune_list)
    info.append(sub_rune_list)
    info.append(ability_rune_list)
    info.append(champ_runes_name)

    return info
    

    

