# 더 많은 페이지 긁어서 크롤링 하기

import re
import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

for i in range(1,6):
    print("페이지  : ", i)
    url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

    #url = "https://www.coupang.com/"

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    # soup = BeautifulSoup(res.text, "lxml")
    # print(res.text)

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # "search-product"로 시작하는 모든 것들을 다 긁어옴

    #print(items[0].find("div",attrs={"class":"name"}).get_text())

    for item in items:

        # 광고 제품은 제외
        ad_badge = items.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            print("광고 상품 제외합니다.")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text() #제품명

        #애플 제품 제외
        if "Apple" in name:
            print("Apple 상품은 제외")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격

        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find("em", attrs={"class":"rating"}) #평점
        if rate:
            rate = rate.get_text()
        else:
            print("평점없는 상품 제외")
            continue

        rate_cnt = item.find("span", attrs={"class":"rate-total-count"}) #평점 수
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[1:-1]
        else:
            print("평점 수 없는 상품은 제외")
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]    
            
        if float(rate) >= 4.5 and int(rate_cnt) > 100:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 {rate_cnt}개")
            print("바로가기 : {}".format("https://coupang.com" + link))
            print("-"*30)    #줄 긋기

