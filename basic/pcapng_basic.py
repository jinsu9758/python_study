# 자료 링크 : https://coding-everyday.tistory.com/54
# 패킷 전체 개수 읽기
from scapy.all import *

packets = rdpcap(r"C:\jin\kdy\test.pcapng")
#print(len(packets))

# 패킷 가져오기
'''
for packet in packets:
    print("출발지 : "+packet['IP'].src+"\t"+"목적지 : "+packet['IP'].dst) #출발지/목적지
'''
'''
for packet in packets:
    if packet['IP'].src == "192.168.1.100" and packet['IP'].sport == packet['IP'].sport: #모든 포트
        #print(packet['IP'].sport == packet['IP'].sport) True
        print("출발지 : "+packet['IP'].src+"\t"+"목적지 : "+packet['IP'].dst) #출발지/목적지
'''

# 프로토콜(80) 가져오기
'''
for packet in packets:
    if packet['IP'].sport == 80 or packet['IP'].dport==80:
        print("출발지 : "+packet['IP'].src+"\t"+"목적지 : "+packet['IP'].dst) #출발지/목적지
'''

# 프로토콜(UDP) 가져오기
#proto=1 -> icmp / proto=6 -> tcp / proto=17 -> udp
'''
for packet in packets:
    if packet['IP'].proto == 17:
        print("출발지 : "+packet['IP'].src+"\t"+"목적지 : "+packet['IP'].dst) #출발지/목적지
'''

# 패킷 내용 가져오기 -> 보안적 요소 때문에 안들고와짐ㅋㅋㅋㅋㅋ
print(packets[0].show())


#프로젝트 (원하는 패킷 찾는 툴 만들기)
'''
출발지 또는 목적지 ip입력 + 포트번호 까지(":") 이걸로 구분
-> 순서대로 정렬 및 내용 확인

>프로젝트.py -f 경로 -src 192.168.0.0:80 -dst 8.8.8.8:443
1.
2.
3.
4.
5.
선택 :


>프로젝트.py -src 192.168.0.0:80 -proto 'UDP'

'''


from scapy.all import *
path = r"C:\jin\kdy\깨달음\network\mac.pcapng"
packets = rdpcap(path)
#print(packets[0].show())


#arp 통신 내역 들고오기
'''
cnt = 0
for packet in packets:
    ip_layer = packet.getlayer("ARP")
    if ip_layer is not None:
        print("{}번".format(cnt+1))
        print(packets[cnt].show())
    cnt = cnt + 1
'''

#arp 통신 출발지 목적지 들고오기  형식-> xx:xx:xx:xx:xx:xx
'''
print(packets[0].src)
print(packets[0].dst) #브로드 캐스트 ff:ff:ff:ff:ff:ff
'''

'''
#mac 조회가 되려면 mac 검색도 해야하는데..
cnt=0
while(1):
    if packets[cnt].src == "04:d9:f5:af:b9:ea":
        print(cnt)
    if cnt == len(packets)-1:
        break
    cnt = cnt + 1
'''


#mac 조회 -> ㄹㅇ arp 통신만 됨.
cnt = 0
for packet in packets:
    #ip_layer = packet.getlayer("ARP")
    #if ip_layer is not None:
    if packet.src == "00:d0:cb:83:07:54":
        print(cnt+1)
        print("출발지 : "+packet.src+"\t"+"목적지 : "+packet.dst) #출발지/목적지
    cnt = cnt + 1



