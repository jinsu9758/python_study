#ARP 패킷은 못들고옴ㄹㅇ ㅋㅋ(미완성)
#ARP 패킷이 없는 네트워크 패킷 파일만 넣어주세요
'''
[!] 다음과 같이 입력해주세요!

[!] [사용 법]
[!] ARP 패킷이 없는 네트워크 패킷 파일만 넣어주세요!

ex)cmd> pckt_filter.py -f 파일경로  -src x.x.x.x:80 -dst x.x.x.x:443

ex)cmd> pckt_filter.py -f 파일경로  -src :80 -dst x.x.x.x:443

ex)cmd> pckt_filter.py -f 파일경로  -src x.x.x.x -dst x.x.x.x:443

- 출발지 또는 목적지 생략 가능
- 포트번호 생략 가능
'''

import argparse
import copy
from scapy.all import *
from Color import Color as c

start = c()

#시작
def Init():
    start.print_title("다음과 같이 입력해주세요!")
    print()
    start.print_title("[사용 법]")
    start.print_title("ARP 패킷이 없는 네트워크 패킷 파일만 넣어주세요!\n")
    start.print_info("ex)cmd> pckt_filter.py -f 파일경로  -src x.x.x.x:80 -dst x.x.x.x:443\n")
    start.print_info("ex)cmd> pckt_filter.py -f 파일경로  -src :80 -dst x.x.x.x:443\n")
    start.print_info("ex)cmd> pckt_filter.py -f 파일경로  -src x.x.x.x -dst x.x.x.x:443\n")
    start.print_info("- 출발지 또는 목적지 생략 가능")
    start.print_info("- 포트번호 생략 가능")
    return start



#인수 생성
def Make_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=False) #None
    parser.add_argument('-src', required=False, default=0)
    parser.add_argument('-dst', required=False, default=0)
    args = parser.parse_args()
    return args



#출발지, 목적지, ip, port 가공하기
def Filter_Packet(path, ip_src, ip_dst):
    if path == None:
        start.print_title("패킷 파일경로를 입력해주세요")
    if ":" in str(ip_src): #포트번호가 있는 경우
        ip_src = ip_src.split(':')
        if len(ip_src[0]) == 0:
            ip_src[0] = 0
        ip_src_dict=dict()
        ip_src_dict['ip_src'] = ip_src[0]
        ip_src_dict['port_src'] = int(ip_src[1])
    else:
        ip_src_dict = dict()
        ip_src_dict['ip_src'] = ip_src
        ip_src_dict['port_src']=0
        
        
    if ":" in str(ip_dst):
        ip_dst = ip_dst.split(':')
        if len(ip_dst[0]) == 0:
            ip_dst[0] = 0
        ip_dst_dict=dict()
        ip_dst_dict['ip_dst'] = ip_dst[0]
        ip_dst_dict['port_dst'] = int(ip_dst[1])
    else:
        ip_dst_dict = dict()
        ip_dst_dict['ip_dst'] = ip_dst
        ip_dst_dict['port_dst']=0

    result = ip_src_dict.copy()
    result.update(ip_dst_dict)
    #print(result)
    return result




#cmd에 출력될 패킷을 필터링 해오는 과정
def Filter_Packet2(path, result):
    packets = rdpcap(path)
    start.print_title("필터링을 시작합니다.\n")
    cnt = 0
    order = 0 #프레임번호
    end=0
    order_list=[]
    for packet in packets:
        order = order + 1
        if result['ip_src'] == 0:
            srcip_cal = True
        else:
            srcip_cal = packet['IP'].src==result['ip_src']
            
            
        if result['ip_dst'] == 0:
            dstip_cal = True
        else:
            dstip_cal = packet['IP'].dst==result['ip_dst']
        
        
        if result['port_src'] == 0: #포트번호를 안받아 오는 경우
            srcport_cal = True
        else:
            srcport_cal = packet['IP'].sport==result['port_src']
        
        
        if result['port_dst'] == 0:
            dstport_cal = True
        else:
            dstport_cal = packet['IP'].dport==result['port_dst']

        if srcip_cal and srcport_cal and dstip_cal and dstport_cal:
            cnt = cnt + 1 #총 패킷 개수 세기
            print("{}. ".format(order)+"출발지 : "+packet['IP'].src+"\t\t"+"출발지포트 : "+str(packet['IP'].sport)+"\t\t"+"목적지 : "+packet['IP'].dst+"\t\t"+"목적지포트 : "+str(packet['IP'].dport)) #출발지/목적지
            order_list.append(order)
            end = order+1
    if end != 0:
        print("{}. 프로그램 종료".format(end))
    print()
    start.print_info("총 패킷 개수 : {}개".format(cnt))
    print()
    if cnt == 0: #패킷 갯수가 없을 때
        quit()
    detail = int(input('선택 : '))
    if detail == end:
        start.print_title("프로그램을 종료합니다.")
        quit()
    final=[]
    final.append(order_list)
    final.append(detail)
    #print(final)
    return final




def ShowPCK(path, final, result):
    packets = rdpcap(path)
    if final[1] in final[0]:
        print(packets[final[1]-1].show())
        print()
        start.print_info("1. 뒤로가기")
        start.print_info("2. 종료하기\n")
        
        choice = int(input('선택 : '))

        if choice == 1:
            final = Filter_Packet2(path, result)
            ShowPCK(path, final, result)
        elif choice == 2:
            start.print_title("프로그램을 종료합니다.")
            quit()
    else:
        start.print_title("알맞은 번호를 선택해주세요\n")
        final = Filter_Packet2(path, result)
        ShowPCK(path, final, result)
        




if __name__ == "__main__":
    args = Make_arg()
    if args.f == None and args.src==0 and args.dst==0:
        start = Init()
    else:
        result = Filter_Packet(args.f, args.src, args.dst)
        final = Filter_Packet2(args.f, result)
        ShowPCK(args.f, final, result)

        
