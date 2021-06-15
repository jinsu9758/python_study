#네이버 코스피 시가 총액 순위 크롤링
#시총 1등~200등

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"

f = open(filename, "w", encoding="utf-8-sig", newline="")  #newline -> 엔터 없애줌 바로 다음줄 가게

writer = csv.writer(f)   # 파일쓰기

title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split('\t') #tab 기준으로 리스트 형식이 만들어지면서 엑셀에 넣기 가능
print(title)
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    
# f12 통해서 본 결과 table 형식으로 되어있고, table 전체를 들고와서 긁는 식으로 해야할 것 같음
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:  #의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns]  #리스트 내포 사용하기
        #strip() -> 공백 제거
        #print(data) # 빈 공백들과, tab 같은 불필요한 것들이 보임.
        writer.writerow(data)   # 엑셀파일에 쓰기 리스트 형식으로 집어넣어주어야 한다!
        