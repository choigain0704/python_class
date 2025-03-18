#모듈
#표준모듈:파이썬에서 기본적으로 제공하는 내장함수,import문으로 바로 사용 가능
#math,random,json,datetime,re(정규표현식)

import math
from queue import PriorityQueue

#math - 수학 관련 모듈
#ceil - 올림
print(math.ceil(3.14))

#copysign - 두 번째 인자의 부호만 취해 첫 번째 인자에 적용
print(math.copysign(3.14,-1))

#fabs - 절댓값을 반환하는 메소드
print(math.fabs(-3.14))

#factorial - 팩토리얼 구하는 메소드
print(math.factorial(7))

#floor - 내림
print(math.floor(3.14))

#gcd - 두 수의 최대공약수
print(math.gcd(12,6))

#modf - 정수 부분과 소수 부분을 분리해서 리턴
print(math.modf(3.14)) #0.14를 2진법(컴퓨터)으로 바꿀 때 부동소수점의 오류 발생

#trunc - 내림
print(math.floor(-3.14)) #음수쪽으로 내림
print(math.trunc(-3.14)) #양수쪽으로 내림

#log(a,b) - b를 밑으로 하는 log a에 대한 로그 값
print(math.log(8,2))

#원주율
print(math.pi)

import random

#난수
print(random.random())
print(random.randint(1,10)) #끝 값 포함
print(random.randrange(1,10,2)) #끝 값 불포함

#shuffle
abc = ["a", "b", "c", "d", "e"]
random.shuffle(abc)
print(abc)

#choice ----------랜덤게임!
abc = ["a", "b", "c", "d", "e"]
print(random.choice(abc))

menu = "삼겹살", "된장찌개", "맥주", "소주"
print(random.choice(menu))

place = "부산", "서울", "대전", "대구"
print(random.choice(place))

from datetime import datetime, timedelta
now = datetime.now()
print(now)

one_week_later = now +  timedelta(days=7)
print(one_week_later)

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

import os

# print(os.getcwd()) #현재 디렉토리
# print(os.listdir()) #현재 폴더의 파일 목록
#
# if not os.path.exists("new_folder"):
#     os.mkdir("new_folder")

# import re
# pattern =
# email = "choigain0704@naver.com"
#
# if re.match(pattern, email):
#     print("올바른 이메일")
# else:
#     print("틀린 이메일")
