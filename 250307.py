#사용자 정의 함수
# def 함수이름(매개변수1, 매개변수2..)

# def func1():
#     print("Hello World")
#
# func1() #매개변수 x

# def plus():
#     a=2
#     b=3
#     print(a+b)
# plus() #매개변수 x

# def hello(name):
#     print(f"안녕하세요 {name}입니다.")
#
# hello("홍길동") #매개변수 삽입
#
# def plus(x,y):
#     print(x+y)
#
# plus(5,6) #매개변수 삽입

# def introduce(name, age):
#     print(f"제 이름은 {name}이고 나이는 {age}세 입니다.")
#
# introduce("최가인", 22)
# introduce(age=22, name="최가인") #매개변수 순서 상관x

# def calculator(x,y,operation):
#     return operation(x,y)
#
# def plus(x,y):
#     return x+y
#
# def minus(x,y):
#     return x-y
#
# print(calculator(8,4,plus))
# print(calculator(8,4,minus))

#lamba 함수(익명함수, 미시함수)
# def plus(x,y):
#     return x+y
# print(plus(4,5))
#
# add_lambda = lambda x,y : x+y
# print(add_lambda(4,5))

# parity = lambda x: "짝수" if x % 2 == 0 else "홀수"  #삼항연산자
# print(parity(2))

