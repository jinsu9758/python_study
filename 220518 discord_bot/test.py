import requests
from bs4 import BeautifulSoup
import re
'''
#op.gg
url = "https://www.op.gg/champions"

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
res = requests.get(url, headers=headers)
res.raise_for_status()


champs_db = dict()

with open("test.html", "w", encoding="utf8") as f:
    f.write(res.text)


soup = BeautifulSoup(res.text, "lxml")
'''
'''
pattern = re.compile("href=\"/champions/\w{1,10}/\w{1,10}")
eng_name = str(soup.find("a", attrs={"class":"e1n0mtzi2"}))
eng_name = pattern.findall(eng_name)[0].replace("href=\"", "").split('/')[2]

kor_name = soup.find("a", attrs={"class":"e1n0mtzi2"}).find("small").get_text()
print(kor_name)
'''

# 스카너 -> RIP (표본이 적어서 안나옴ㅋㅋㅋㅋㅋ)
'''
cnt = len(soup.find_all("a", attrs={"class":"e1n0mtzi2"}))
#print(cnt)
pattern = re.compile("href=\"/champions/\w{1,20}/\w{1,20}")

for c in range(cnt):
    try:
        eng_name = soup.find_all("a", attrs={"class":"e1n0mtzi2"})[c]
        kor_name = eng_name.find("small").get_text()
        #print(kor_name)
        #print(str(eng_name))
        
        eng_name = pattern.findall(str(eng_name))[0].replace("href=\"", "").split('/')[2]
        print(kor_name, eng_name)
        
        champs_db[kor_name] = eng_name
    except:
        continue
print(champs_db)
'''

'''
url = "https://www.leagueofgraphs.com/ko/champions/counters/galio"

headers = {
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

res = requests.get(url, headers=headers)

res.raise_for_status()


with open("test.html", "w", encoding="utf8") as f:
    f.write(res.text)



soup = BeautifulSoup(res.text, "lxml")

victory_champ = soup.find_all('table')[0].find_all("span", attrs={"class" : "name"})[:3] #챔프 3개만 추출
counter_champ = soup.find_all('table')[1].find_all("span", attrs={"class" : "name"})[:3] #챔프 3개만 추출

print(victory_champ)
print(counter_champ)
'''

url = "https://www.op.gg/champions/leblanc/mid/build"

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



res = requests.get(url, headers=headers)

res.raise_for_status()

with open("test.html", "w", encoding="utf8") as f:
    f.write(res.text)

Rune = {'결의':'초록색', '마법':'파란색', '지배':'빨간색', '정밀':'노란색', '영감':'하늘색'}

soup = BeautifulSoup(res.text, "lxml")

champ_runes_name = soup.find("table", attrs={"class":"e10jawsm1"}).find("div", attrs={"class":"rune_header"}).find("div", attrs={"class":"name"}).get_text().split(' + ')
#print(champ_runes_name)

main_rune_list = []
if champ_runes_name[0] == "지배" or champ_runes_name[0] == "정밀":
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

#print(len(ability_rune_rows))

#print(main_rune_rows[0])



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



print(main_rune_list)
print(sub_rune_list)
print(ability_rune_list)


