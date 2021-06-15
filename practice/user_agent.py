# User-Agent를 넣어줘야 실제 크롬에서 접속했을 때와 동일한 파일(코드) 들을 받아올 수 있다.
import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

res = requests.get(url, headers=headers)

res.raise_for_status()

with open("nadocoding.html","w",encoding="utf-8") as f:
    f.write(res.text)
   
