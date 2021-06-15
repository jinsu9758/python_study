#project) 웹 스크래핑을 이용하여 나만의 비서를 만드시오
# [조건]
# 1.네이버에서 오늘 대구의 날씨정보를 가져온다 o
# 2. 헤드라인 뉴스 3건을 가져온다
# 3. IT 뉴스 3건을 가져온다
# 4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다
# ===================================================================

# [출력 예시]

# [오늘의 날씨]
# 비, 어제보다 3˚ 낮아요
# 현재 00C ( 최저 00도 / 최고 00도)

# 미세먼지 00 좋음
# 초미세먼지 00 좋음
# 오존지수 00좋음

import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hKlhIdprvh8ssCzIB94ssssstTl-119752"
res = requests.get(url)
res.raise_for_status()
#print(res.text)

soup = BeautifulSoup(res.text,"lxml")
print("[오늘의 날씨]")
cast_txt = soup.find("p", attrs={"class":"cast_txt"}).get_text() #날씨 설명
print(cast_txt)

today_temp = soup.find("span", attrs={"class":"todaytemp"}).get_text() #오늘 날씨
temp_mark = soup.find("span", attrs={"class":"tempmark"}).get_text()[-1:] #℃
min_to_max = soup.find_all("span", attrs={"class":"num"})
low_temp = min_to_max[0].get_text() # 오늘 최저기온
high_temp = min_to_max[1].get_text() # 오늘 최고기온


nano_dust = soup.find_all("dd", attrs={"class":"lv1"}) #dd를 들고오면 안됨. class가 바뀔수 있음. 그 위에 태그를 들고오도록 하자! 수정 필요!
ozone = soup.find("dd", attrs={"class":"lv2"})
print("현재 "+today_temp+temp_mark+"( 최저 "+low_temp+" / 최고 "+high_temp+" )")
#print(low_temp, high_temp)
print()
#print(nano_dust)
print("미세먼지"+nano_dust[0].get_text())
print("초미세먼지"+nano_dust[1].get_text())
print("오존지수"+ozone.get_text())

print("\n"+"="*100)
# ===================================================================
# [헤드라인 뉴스]
# 1. ~~~~~~
# (링크  : ~~~)
# 2. ~~~~~~
# (링크  : ~~~)
# 3. ~~~~~~
# (링크  : ~~~)

url = "https://news.naver.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
res = requests.get(url, headers=headers) #네이버 뉴스 헤더 없으면 안들어가지네용
res.raise_for_status()
#print(res.text)
print()
print("[헤드라인 뉴스]")

soup = BeautifulSoup(res.text,"lxml")

titles = soup.find_all("div", attrs={"class":"hdline_article_tit"})
#print(titles[0].a)

#print(links)

#print(titles[0].get_text().strip())

for i in range(3):
    link = titles[i].a["href"]
    print("{}. ".format(i+1)+titles[i].get_text().strip())
    print("( 링크 : "+url+link+" )")
    print()

print("\n"+"="*100)
# ===================================================================
# [IT뉴스]
# 1. ~~~~~~
# (링크  : ~~~)
# 2. ~~~~~~
# (링크  : ~~~)
# 3. ~~~~~~
# (링크  : ~~~)

print()
print("[IT 일반 뉴스]")

url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"

res = requests.get(url, headers=headers)
res.raise_for_status()

#print(res.text)

soup = BeautifulSoup(res.text, "lxml")

class_title = soup.find_all("dt", attrs={"class":"photo"})
titles = soup.find_all("dt")
#print(titles)

results = [x for x in titles if x not in class_title]  # 전체리스트 - 클래스있는 리스트

#print(not_class_title)

for i in range(3):
    link = results[i].a["href"]
    print("{}. ".format(i+1)+results[i].a.get_text().strip())
    print("( 링크 : "+link+" )")
    print()

print("\n"+"="*100)

print()

# ===================================================================
# [오늘의 영어 회화]
# (한글 지문)
# ~~~~~~~~~~~~
# ~~~~~~~~~~~~

# (영어 지문)
#  ~~~~~~~~
#  ~~~~~~~~~


print("[오늘의 영어 회화]")

url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"

res = requests.get(url, headers=headers)
res.raise_for_status()

#print(res.text)

soup = BeautifulSoup(res.text,"lxml")

today_expression = soup.find_all("b", attrs={"class":"conv_txtTitle"})

kor = today_expression[0]

eng = today_expression[1]

contents = soup.find_all("span", attrs={"class":"conv_sub"})  # 0~3 : 한국어, 4~7 : 영어


print("## 한글 지문 ##")
print("오늘의 표현 : " + kor.get_text()+"\n")

for i in range(4):
    content = contents[i].get_text()
    print(content)
    print()

print("## 영어 지문 ##")
print("오늘의 표현 : " + eng.get_text()+"\n")

for i in range(4,8):
    content = contents[i].get_text()
    print(content)
    print()

print("\n"+"="*100)