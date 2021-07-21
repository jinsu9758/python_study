# requests : 데이터를 보낼 때 딕셔너리 형태로 보낸다.
# 없는 페이지를 요청해도 에러를 띄우지 않는다.

# urllib.request : 데이터를 보낼 때 인코딩하여 바이너리 형태로 보낸다.
# 없는 페이지를 요청하면 에러를 띄움.

import json
import urllib.request

url = "https://api.androidhive.info/contacts/"

#id, name, emaiil, address, gender, phone(mobile, home, office)
with urllib.request.urlopen(url) as url:
    datas = json.loads(url.read().decode())


datas = datas['contacts']
#print(datas)
#출력형식 지정하기
'''
1.
id :
name :
email :
address:
gender:
[phone]
mobile :
home:
office:
'''
for idx, data in enumerate(datas):
    print(str(idx+1)+".")
    print("{} : {}".format('id', data['id']))
    print("{} : {}".format('name', data['name']))
    print("{} : {}".format('email', data['email']))
    print("{} : {}".format('address', data['address']))
    print("{} : {}".format('gender', data['gender']))
    print("[phone]")
    print("{} : {}".format('mobile', data['phone']['mobile']))
    print("{} : {}".format('home', data['phone']['home']))
    print("{} : {}".format('office', data['phone']['office']))
    print()

    














