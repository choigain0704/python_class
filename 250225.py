# 대입 연산자
# = 대입
# ==같다
# !=같지않다

#x=10 #대입
# x += 10 #더하고 할당 x=x+10
# x -=5 #빼고 할당
# x *= 3 #곱하고 할당
# x /= 2 #나누고 할당 (실수 몫) 5.0
# x //= 2 #나누고 할당 (정수 몫) 5
# print(x)

#비교 연산자(True 또는 False 반환)
# x = 10
# y = 20
# z = 10
# print(x == z) #같다
# print(x != z) #같지않다
# print(x > y) #왼쪽기준 오른쪽보다 크다
# print(x < y) #왼쪽기준 오른쪽보다 작다
# print(x >= z) #크거나 같다
# print(x <= y) #작거나 같다

#논리 연산자(and, or, not)
# True and False = False
# True or False = True
# not True = False
# a = True
# b = False
# print(a and b)
# print(a or (a and b))
# print(not a)
# print(not a and b)
# print(not b or a)
#
# #조건 연산자 (값1 if 조건식 else 값2)(삼항연산자)
# #자바!=자바스크립트
a = 10
b = 20
# max_value = a if a > b else b
# print(max_value)
if a > b :
    max_value   = a
else :
    max_value = b


score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else("C" if score >= 70 else "D"))
print(grade)
if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
else :
    print("C")

seconds = 11
if seconds >= 15 :
    print("C")
elif seconds >= 13 :
    print("B")
else :
    print("A")




