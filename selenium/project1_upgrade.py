# [출력 예시]

# [오늘의 날씨]
# 비, 어제보다 3˚ 낮아요
# 현재 00C ( 최저 00도 / 최고 00도)

# 미세먼지 00 좋음
# 초미세먼지 00 좋음
# 오존지수 00좋음
import requests
import re
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print("링크 : {}".format(link))
    
    
def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hKlhIdprvh8ssCzIB94ssssstTl-119752"
    soup = create_soup(url)
    cast_txt = soup.find("p", attrs={"class":"cast_txt"}).get_text() #날씨 설명

    today_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    low_temp = soup.find("span", attrs={"class":"min"}).get_text()
    high_temp = soup.find("span", attrs={"class":"max"}).get_text()

    #또 다른 방법
    #today_temp = soup.find("span", attrs={"class":"todaytemp"}).get_text() #오늘 날씨
    #temp_mark = soup.find("span", attrs={"class":"tempmark"}).get_text()[-1:] #℃
    #min_to_max = soup.find_all("span", attrs={"class":"num"})
    #low_temp = min_to_max[0].get_text() # 오늘 최저기온
    #high_temp = min_to_max[1].get_text() # 오늘 최고기온

    #미세먼지 정보
    dust = soup.find("dl", attrs={"class":"indicator"}) 
    pm10 = dust.find_all("dd")[0].get_text() #미세먼지
    pm25 = dust.find_all("dd")[1].get_text() #초미세먼지
    
    
    #출력
    print(cast_txt)
    print("현재 "+today_temp+"( 최저 "+low_temp+" / 최고 "+high_temp+" )")
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()


def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3) # 3개까지 찾는 것
    #print(news_list)
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print()

    #또 다른 방법
    #titles = soup.find_all("div", attrs={"class":"hdline_article_tit"})
    #for i in range(3):
    #    link = titles[i].a["href"]
    #    print("{}. ".format(i+1)+titles[i].get_text().strip())
    #    print("( 링크 : "+url+link+" )")
    #    print()
    

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3) #li태그 3개만 불러오기

    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a 태그의 정보를 사용
        title = news.find_all("a")[a_idx].get_text().strip()
        link = news.find_all("a")[a_idx]["href"]
        print_news(index, title, link)
    print()
        
    #또 다른 방법
    #class_title = soup.find_all("dt", attrs={"class":"photo"})
    #titles = soup.find_all("dt")
    #results = [x for x in titles if x not in class_title]  # 전체리스트 - 클래스있는 리스트
    #for i in range(3):
    #    link = results[i].a["href"]
    #    print("{}. ".format(i+1)+results[i].a.get_text().strip())
    #    print("( 링크 : "+link+" )")
    #    print()



def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    soup = create_soup(url)
    today_expression = soup.find_all("b", attrs={"class":"conv_txtTitle"})

    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print(" (영어 지문) ")
    for sentence in sentences[len(sentences)//2:]: #8문장이 있다고 가정할 때, 5~8까지 짤라서 가져
        print(sentence.get_text().strip())
        
    print()
    print(" (한글 지문) ")
    for sentence in sentences[:len(sentences)//2]: #8문장이 있다고 가정할 때, 5~8까지 짤라서 가져
        print(sentence.get_text().strip())
    print()
    # 또 다른 방법
    #kor = today_expression[0]
    #eng = today_expression[1]
    #contents = soup.find_all("span", attrs={"class":"conv_sub"})  # 0~3 : 한국어, 4~7 : 영어
    #print("## 한글 지문 ##")
    #print("오늘의 표현 : " + kor.get_text()+"\n")
    #for i in range(4):
    #    content = contents[i].get_text()
    #    print(content)
    #    print()
    #print("## 영어 지문 ##")
    #print("오늘의 표현 : " + eng.get_text()+"\n")
    #for i in range(4,8):
        #content = contents[i].get_text()
        #print(content)
        #print()



if __name__ == "__main__": # 직접 실행할때는 아래의 함수들이 실행되지만, 다른 파일에서 실행하게 되면 실행x
    scrape_weather() #오늘의 날씨 정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스 정보 가져오기
    scrape_it_news() # IT 뉴스 정보 가져오기
    scrape_english() # 오늘의 영어회화 가져오기
    