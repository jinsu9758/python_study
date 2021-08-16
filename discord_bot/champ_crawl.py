import requests
from bs4 import BeautifulSoup

'''
url = "https://www.op.gg/champion/statistics"

headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
res = requests.get(url, headers=headers)

res.raise_for_status()

#print(res.text)

soup = BeautifulSoup(res.text, "lxml")

champions = soup.find_all("div", attrs={"class":"champion-index__champion-item"})

for champion in champions:
    print(champion['data-champion-key'])
'''


f = open("C:\jin\discord_bot\champ.txt", 'r')
lines = f.readlines()
for line in lines:
    f2 = open("C:\jin\discord_bot\champ2.txt", 'a')
    print(line)
    line = line.replace('\n','')
    a = input('입력 : ')
    data = "{'%s' : '%s'}\n"%(line, a)
    f2.write(data)
    f2.close()
f.close()

