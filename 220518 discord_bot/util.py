import crawler


'''
# 챔프들 크롤링한 코드 (참고용)
import requests
from bs4 import BeautifulSoup
import re

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

# 스카너 -> RIP (표본이 적어서 안나옴ㅋㅋㅋㅋㅋ)

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


# 신챔 등장할때마다 추가해주면 됨.
# 스카너 -> RIP (표본이 적어서 안나옴ㅋㅋㅋㅋㅋ)

champs_db = {
    '가렌': 'garen', '갈리오': 'galio', '갱플랭크': 'gangplank', '그라가스': 'gragas',\
    '그레이브즈': 'graves', '그브': 'graves', '그웬': 'gwen', '나르': 'gnar', '나미': 'nami', '나서스': 'nasus',\
    '노틸러스': 'nautilus', '녹턴': 'nocturne', '누누와 윌럼프': 'nunu', '누누': 'nunu', '니달리': 'nidalee',\
    '니코': 'neeko', '다리우스': 'darius', '다이애나': 'diana', '드레이븐': 'draven', '라이즈': 'ryze',\
    '라칸': 'rakan', '람머스': 'rammus', '럭스': 'lux', '럼블': 'rumble', '레나타 글라스크': 'renata','레나타': 'renata',\
    '레넥톤': 'renekton', '레오나': 'leona', '렉사이': 'reksai', '렐': 'rell', '렝가': 'rengar',\
    '루시안': 'lucian', '룰루': 'lulu', '르블랑': 'leblanc', '리 신': 'leesin', '리븐': 'riven',\
    '리산드라': 'lissandra', '릴리아': 'lillia', '마스터 이': 'masteryi', '마이': 'masteryi', '마오카이': 'maokai',\
    '말자하': 'malzahar', '말파이트': 'malphite', '모데카이저': 'mordekaiser', '모데': 'mordekaiser', '모르가나': 'morgana',\
    '문도 박사': 'drmundo', '문도': 'drmundo', '미스 포츈': 'missfortune', '바드': 'bard', '바루스': 'varus', '바이': 'vi',\
    '베이가': 'veigar', '베인': 'vayne', '벡스': 'vex', '벨코즈': 'velkoz', '볼리베어': 'volibear', '브라움': 'braum',\
    '브랜드': 'brand', '블라디미르': 'vladimir', '블리츠크랭크': 'blitzcrank', '블츠': 'blitzcrank', '블리츠': 'blitzcrank', '비에고': 'viego', '빅토르': 'viktor',\
    '뽀삐': 'poppy', '사미라': 'samira', '사이온': 'sion', '사일러스': 'sylas', '샤코': 'shaco', '세나': 'senna',\
    '세라핀': 'seraphine', '세주아니': 'sejuani', '세트': 'sett', '소나': 'sona', '소라카': 'soraka', '쉔': 'shen',\
    '쉬바나': 'shyvana', '스웨인': 'swain', '시비르': 'sivir', '신 짜오': 'xinzhao', '신드라': 'syndra', '신지드': 'singed',\
    '쓰레쉬': 'thresh', '아리': 'ahri', '아무무': 'amumu', '아우렐리온 솔': 'aurelionsol', '솔': 'aurelionsol', '아이번': 'ivern', '아지르': 'azir',\
    '아칼리': 'akali', '아크샨': 'akshan', '아트록스': 'aatrox', '아펠리오스': 'aphelios', '알리스타': 'alistar',\
    '애니': 'annie', '애니비아': 'anivia', '애쉬': 'ashe', '야스오': 'yasuo', '에코': 'ekko', '엘리스': 'elise',\
    '오공': 'monkeyking', '오른': 'ornn', '오리아나': 'orianna', '올라프': 'olaf', '요네': 'yone', '요릭': 'yorick',\
    '우디르': 'udyr', '우르곳': 'urgot', '워윅': 'warwick', '유미': 'yuumi', '이렐리아': 'irelia', '이블린': 'evelynn',\
    '이즈리얼': 'ezreal', '일라오이': 'illaoi', '자르반 4세': 'jarvaniv', '자야': 'xayah', '자이라': 'zyra', '자크': 'zac',\
    '잔나': 'janna', '잭스': 'jax', '제드': 'zed', '제라스': 'xerath', '제리': 'zeri', '제이스': 'jayce', '조이': 'zoe',\
    '직스': 'ziggs', '진': 'jhin', '질리언': 'zilean', '징크스': 'jinx', '초가스': 'chogath', '카르마': 'karma', '카밀': 'camille',\
    '카사딘': 'kassadin', '카서스': 'karthus', '카시오페아': 'cassiopeia', '카시': 'cassiopeia', '카이사': 'kaisa', '카직스': 'khazix', '카타리나': 'katarina',\
    '칼리스타': 'kalista', '케넨': 'kennen', '케이틀린': 'caitlyn', '케인': 'kayn', '케일': 'kayle', '코그모': 'kogmaw', '코르키': 'corki',\
    '퀸': 'quinn', '클레드': 'kled', '키아나': 'qiyana', '킨드레드': 'kindred', '타릭': 'taric', '탈론': 'talon', '탈리야': 'taliyah',\
    '탐켄치': 'tahmkench', '트런들': 'trundle', '트리스타나': 'tristana', '트타': 'tristana', '트린다미어': 'tryndamere',\
    '트위스티드 페이트': 'twistedfate','트페': 'twistedfate', '트위치': 'twitch', '티모': 'teemo', '파이크': 'pyke', '판테온': 'pantheon',\
    '피들스틱': 'fiddlesticks', '피오라': 'fiora', '피즈': 'fizz', '하이머딩거': 'heimerdinger', '헤카림': 'hecarim'
    }

# 봇 사용 설명해줌
def print_help():
    templete = "```cs\n" + "# 롤하는 원준잉 사용법 #\n\n"\
               + "※\'!\'를 붙이면 소환사를 검색해줍니다.\n"\
               + "→\'ex) !소환사명\'\n\n"\
               + "※\'#(해쉬태그)\'를 붙여서 챔피언 정보를 봅시다.\n"\
               + "→\'ex) #라인 챔피언명\'\n\n" + "```"
    return templete


# 유저 검색시, 정보들 출력해줌
def print_user_info(info):
    user_link = info[0]
    title = info[1] # ## 솔로랭크 기준 ##
    title2 = info[2] # ooo 검색결과입니다.
    tier_content = info[3] # 티어 : silver 4
    win_rate_content = info[4].replace(' 패', '패 ')
    most_champ_lists = info[5] #리스트 형식임.

    # 솔랭 결과가 안나오는 유저
    if tier_content == "솔로랭크 기록이 없습니다!":
        templete = user_link + "\n```cs\n" +  "# " + title2 + " #"+"\n\n※" + tier_content +"```"

    # 솔랭 결과나 나오는 유저
    else:
        cnt = len(most_champ_lists) # default 7
        most_champs_msg = ""
        for c in range(cnt):
            _list = most_champ_lists[c]
            name = _list[0]
            kda = _list[1].replace(' 평점', '')
            rate = _list[2]
            games = _list[3].strip().replace(' ', '')
            most_champs_msg += str(c+1) + ". " + name + "/" + kda  + "/" + rate + "/" + games + "\n"

        
        templete = user_link + "\n```cs\n" + title + "\n\n" + "# " + title2 + " #" + "\n\n\'" + tier_content + "\'\n\'" + win_rate_content +"\'\n\n" +"#[ Most Champs List ]#\n" +"\'\n" + most_champs_msg + "\'\n"+"```"
    #print(templete)  
    return templete

# 챔피언 검색시, 정보들 출력해줌.
def print_champ_info(info):
    champ_link = info[0]
    title = info[1] ##라인 챔프명 검색결과입니다!##
    tier = info[2] # 협곡 티어 #
    victory_champs = info[3] #상대하기 쉬운 챔
    counter_champs = info[4] # 상대하기 어려운 챔프
    champ_runes = info[5] # 챔프 룬들

    rune_type = champ_runes[-1]
    #print(rune_type)
    
    rune_templete = ""
    
    for i in range(len(champ_runes)-1):
        runes = champ_runes[i]
        rune_templete += rune_type[i]+crawler.Rune[rune_type[i]]+"\n"
        for j in range(len(runes)):
            rune = runes[j]
            for j in range(len(rune)):
                rune_templete += rune[j] + ' '
            rune_templete += '\n'
        rune_templete += '\n'

    templete = champ_link + "\n```cs\n" + title + "\n\n" + tier + "\n\n" + victory_champs + "\n\n" + counter_champs + "\n\n"\
               + "# 추천 룬 세팅 #" + "\n\n" + rune_templete + "\n```"

    return templete
    
    



