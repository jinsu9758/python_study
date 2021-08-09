#import collections -> 여러 모듈들이 있네요?....
'''
collections 모듈은 다양한 자료구조인 리스트, 튜플, 딕셔너리 등을 확장하여 제작된
파이썬의 내장 모듈이다.
'''
#1. deque 모듈 (스택과 큐를 모두 지원)
from collections import deque

#스택
'''
deque_list = deque()
for i in range(5):
    deque_list.append(i)

print(deque_list) #0 1 2 3 4

print(deque_list.pop()) #4
print(deque_list.pop()) #3

print(deque_list) # 0 1 2
'''

# 큐 -> 새로운 값을 왼쪽으로부터 입력되게 하여 먼저 들어간 값부터 출력하기
'''
deque_list = deque()

for i in range(5):
    deque_list.appendleft(i)

print(deque_list) # 4 3 2 1 0

print(deque_list.pop()) #0
print(deque_list.pop()) #1

print(deque_list) # 4 3 2
'''

#OrderedDict 모듈
# 입력한 순서대로 dict 형태로 저장됨. 원래는 그렇게 저장이 안됨.
'''
from collections import OrderedDict

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 400

for k,v in d.items():
    print(k, v)
'''

#defaultdict 모듈
# 딕셔너리 변수를 생성할 때 키에 기본 값을 지정하는 방법이다.
from collections import defaultdict

'''
d = defaultdict(lambda:0)
print(d['first'])
'''


s = [('yellow',1), ('blue',2), ('yellow',3), ('blue',4), ('red',1)]
#print(type(s))
d = defaultdict(list) # default를 list로 잡음
for k,v in s:
    d[k].append(v)

print(d.items())


#Counter 모듈
'''
from collections import Counter
text = list("gallahad")
print(text)
c = Counter(text)
print(c)
print(c['a'])
'''

#namedtuple 모듈
'''
from collections import namedtuple
Student = namedtuple('Student',['sno','name','major'])
s = Student(1,'홍길동','컴공')
print(s) #Student(sno=1, name='홍길동', major='컴공')
'''











