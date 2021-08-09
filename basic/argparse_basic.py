import argparse


#인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='사용법 테스트입니다.')

#입력받을 인자값 등록 (required=True면 생략불가능, False이면 생략가능한데...default는 생략시 출력)
parser.add_argument('--target', required=True, help='어느 것을 요구하냐')
parser.add_argument('--env', required=False, default='dev', help='실행환경은 뭐냐')

#입력받은 인자값을 args에 저장
args = parser.parse_args()

#입력받은 인자값 출력
print(args.target)
print(args.env)



'''
터미널에서 실행을 시켜서 인자값을 받을 수 있도록 하는거임.
터미널 (Window 기준 -> cmd)

1.
[실행]
>argparse_basic.py -h

[결과]
사용법 테스트입니다.

optional arguments:
  -h, --help       show this help message and exit
  --target TARGET  어느 것을 요구하냐
  --env ENV        실행환경은 뭐냐


2. 꼭 "=" 안붙여도 됨.
[실행]
>argparse_basic.py --target=테스트 --env=local

[결과]
테스트
local

'''
'''
# 간단하게 더하기 프로그램이나 만들겠습니다.
parser = argparse.ArgumentParser(description='더하기 프로그램입니다.')

parser.add_argument('-num1', required=False, default=0, type=int)
parser.add_argument('-num2', required=False, default=0, type=int)

args = parser.parse_args()

num1 = args.num1
num2 = args.num2

print("답 : ",num1 + num2)
'''







