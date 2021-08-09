#IP, ARP 통신을 가져와서 필터링 해줍니다!

import argparse
import copy
from scapy.all import *
from Color import Color as c

start = c()

#사용법
def Help():
    start.print_title("다음과 같이 입력해주세요!")
    print()
    start.print_title("[사용 법]")
    start.print_title("네트워크 패킷 파일을 넣어주세요!\n")
    start.print_info("ex)cmd> pckt_filter.py -f 파일경로")
    start.print_info("- 출발지 또는 목적지 생략 가능")
    start.print_info("- 포트번호 생략 가능")
    return start


#시작
def Init():
    start.print_title("프로그램을 시작합니다.\n")
    print("1. IP 통신의 패킷 추출하기")
    print("2. ARP 통신의 패킷 추출하기\n")
    choice = int(input("선택 : "))
    return choice
    
    
    

#인수 생성
def Make_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=False) #None
    args = parser.parse_args()
    return args


def Filter_input(choice):
    result = dict()
    address = []
    if choice == 1: #IP 선택
        print()
        start.print_title("IP통신 패킷 필터링 사용법\n")
        start.print_info("[IP, PORT 모두 입력시...]")
        start.print_info("출발지 : x.x.x.x:80")
        start.print_info("목적지 : x.x.x.x:123\n")
        start.print_info("[PORT 입력시...]")
        start.print_info("출발지 : *:80")
        start.print_info("목적지 : x.x.x.x:123\n")
        start.print_info("[출발지 주소만 입력시...]")
        start.print_info("출발지 : x.x.x.x")
        start.print_info("목적지 : *\n\n")
        src_ip = input("출발지 주소 : ")
        dst_ip = input("목적지 주소 : ")
        address.append(src_ip)
        address.append(dst_ip)
        result[choice] = address
        return result
        
        
    elif choice == 2: #arp 선택
        print()
        start.print_title("ARP통신 패킷 필터링 사용법\n")
        start.print_info("[출발지, 목적지 모두 입력시...]")
        start.print_info("출발지 : xx:xx:xx:xx:xx:xx")
        start.print_info("목적지 : ff:ff:ff:ff:ff:ff\n")
        start.print_info("[출발지 주소만 입력시...]")
        start.print_info("출발지 : xx:xx:xx:xx:xx:xx\n\n")
        src_arp = input("출발지 주소 : ")
        address.append(src_arp)
        result[choice] = address
        return result
        
        
def Filter_address(result):
    choice = list(result.keys())[0]  #1 : IP,  2:ARP
    
    if choice == 1:   #IP 선택한 경우
        address_src = result[choice][0] #[0] : 출발지 , [1] : 목적지
        address_dst = result[choice][1]
        result = []
        if ":" in address_src:
            address_src = address_src.split(":")
            if address_src[0] == '*':  #포트번호만 있는 경우
                address_src[0] = '*'
            result.append(address_src[0])
            result.append(address_src[1])
        else:
            result.append(address_src)
            result.append('*')

            
        if ":" in address_dst:
            address_dst = address_dst.split(":")
            if len(address_dst[0]) =='*':
                address_dst[0] = '*'
            result.append(address_dst[0])
            result.append(address_dst[1])
        else:
            result.append(address_dst)
            result.append('*')
        return result
        
    elif choice == 2:
        address_src = result[choice][0]
        result = []
        result.append(address_src)
        result.append('*')
        result.append('*')
        result.append('*')
        return result

def Packet_Filter(result, choice, path):
    packets = rdpcap(path)
    
    if choice == 1:  #IP 필터링 선택시 
        order = 0
        cnt = 0
        end = 0
        order_list=[]
        start.print_title("IP 필터링을 시작합니다!\n")
        for packet in packets:
            order = order + 1
            if result[0] == "*":
                srcip_cal = True
            else:
                srcip_cal = packet['IP'].src==result[0]


            if result[1] == "*":
                srcport_cal = True
            else:
                srcport_cal = packet['IP'].sport == int(result[1])


            if result[2] == "*":
                dstip_cal = True
            else:
                dstip_cal = packet['IP'].dst == result[2]


            if result[3] == "*":
                dstport_cal = True
            else:
                dstport_cal = packet['IP'].dport == int(result[3])

            if srcip_cal and srcport_cal and dstip_cal and dstport_cal:
                cnt = cnt + 1
                print("{}. ".format(order)+"출발지 : "+packet['IP'].src+"\t\t"+"출발지포트 : "+str(packet['IP'].sport)+"\t\t"+"목적지 : "+packet['IP'].dst+"\t\t"+"목적지포트 : "+str(packet['IP'].dport)) #출발지/목적지
                order_list.append(order)
                end = order+1
        if end !=0:
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
        
                        
    elif choice == 2:
        order = 0
        cnt = 0
        end = 0
        order_list=[]
        start.print_title("ARP 필터링을 시작합니다!\n")
        for packet in packets:
            order = order + 1
            ip_layer = packet.getlayer("ARP")
            if ip_layer is not None:
                if packet.src==result[0]:
                    cnt = cnt + 1
                    print("{} .".format(order)+"출발지 : {}\t".format(packet.src)+"목적지 : ff:ff:ff:ff:ff:ff")
                    order_list.append(order)
                end = order + 1
                    
        if end!=0:
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
            final = Packet_Filter(result, choice, path)
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
    if args.f == None:
        start = Help()
    else:
        choice = Init()
        result = Filter_input(choice)  #출발지, 목적지 받아왔음.
        result = Filter_address(result)  # 출발지 목적지 가공하였음. ['출발', '*', '목적', '*']
        final = Packet_Filter(result, choice, args.f)
        ShowPCK(args.f, final, result)
        
        
