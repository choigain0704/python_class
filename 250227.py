#제어문
#조건문
#반복문(for, while)

num = int(input("숫자를 입력해 주세요"))
if num >= 0 :
    print("양수입니다.")
else:
    print("음수입니다.")

input_str = input("점수를 입력해 주세요")
if input_str.isdigit():
    if int(input_str) >= 90 :
      print("A 입니다.")
    elif int(input_str) >= 80 :          #다중조건 elif
        print("B 입니다.")
    elif int(input_str) >= 70 :          #다중조건 elif
        print("C 입니다.")
    else :
        print("D 입니다.")
else :
    print("숫자가 아닙니다.")

# #숫자를 입력받고 짝수인지 홀수인지 판별
num = int(input(""))
if num % 2 == 0:
    print("짝수")
else :
    print("홀수")

#나이와 학생인지 아닌지 두가지 질문
#성인이면서 학생이면 성인학생입니다 출력
#성인이면서 학생아니면 성인학생아닙니다 출력

age = int(input("나이를 입력 하세요."))
student = input("학생입니까?(Y/N)")

if age >= 18 and student == "Y":
    print("성인학생입니다.")
else :
    print("성인학생아닙니다.")


#반복문 while
num = 1
while num < 10:   #조건이 참(True)인동안 계속 반복 / 특정 조건을 만족할 때까지 계속 실행해야하는 경우
    print(num)
    if num == 7:
        break
    num += 1     #조건변경 코드 필수 (없으면 무한루트)

num = 0
while num < 10:
    num += 1
    if num % 3 == 0:  #if문이 참일 경우 cointinue 실행해서 다시 while문으로 돌아간다
        continue
    print(num)

# 구구단 만들기
dan = 1
while dan <= 9 :
    n = 1
    while n <= 9:
        print(f"{dan}x{n}={dan*n}")
        n += 1
    dan += 1

# 5부터 5의 배수를 50이하까지 조건
# 근데 30일때 멈추기

num = 5
while num <= 50:
    if num % 5 == 0:
        print(num)
        if num == 30:
            break
    num += 1

num = 5
while num <= 50:
    print(num)
    if num == 30:
        break
    num += 5


# 반복문(for)
fruits = ["사과", "바나나", "체리", "딸기"] #리스트
for fruit in fruits:
    print(fruit)

score = {                                #딕셔너리
    "동윤" : 80,
    "종원" : 70,
    "지니" : 100
}
for key in score:
    print(key)

for key in score:
    print(score[key])

for key in score:
    print(f"{key}의 점수는 {score[key]}")

a_tuple = ("안녕", "하세요", "반갑습니다.")   #튜플
for a in a_tuple:
    print(a)

a_set = {3,1,1,2,4,6,2}                     #세트
print(sorted(a_set))
for a in a_set:
    print(a)

word = "python"                            #문자열
for i in word:
    print(i)

for i in range(1,10,2): #(시작, 끝, 간격)
    if i == 5:
        continue
    print(i)

for i in range(2,101,2):
    print(i)

#리스트 합 구하기
num_list = [10,20,40,60,80]
total = 0
for num in num_list:
    total += num
print(total)

#for문으로 구구단 만들기
dan = 1
for dan in range(1,10):
    for n in range(1,10):
        print(f"{dan}x{n}={dan*n}")
        n += 1
    dan += 1



