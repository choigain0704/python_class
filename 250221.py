#딕셔너리

profile = {
    "name" : "최가인",
    "age" : 24,
    "hobby" : ["산책하기", "사진찍기", "블로그 쓰기"]
}
print(profile["hobby"][2]) #hobby 안 요소에 접근하기

profile["age"] = 25 #키가 존재하는 것을 수정한다
print(profile)

profile["job"] = "예능 PD" #키가 존재하지 않는 것을 추가한다
print(profile)

del profile["job"] #키가 존재하는 것을 삭제
print(profile)

key_list = list (profile.keys()) #키만 뽑아서 나열
key_list.append("job")
print(key_list)

value_list = list(profile.values())
print(value_list)

profile.items() #키-값 형태로 다 뽑아내기
item_list   = list(profile.items())
item_list.append(("job", "예능 PD"))
print(item_list)

python_grade = {
    "가인" : "A",
    "길동" : "C",
    "준식" : "B",
    "상혁" : "D"
}
print(sorted(python_grade.items())) #키 기준 오름차순
print(sorted(python_grade.items(),reverse=True)) #키 기준 내림차순

print(sorted(python_grade.items(),key=lambda x : x[1])) #값 기준 오름차순
print(sorted(python_grade.items(),key=lambda x : x[1],reverse=True)) #값 기준 내림차순


#이름 입력 받고 점수도 입력받고
#방법1
# student = {
#     "name" : input("이름: "),
#     "score" : input("점수 : ")
# }
# print(student)
#
# #방법2
# student["name"] = input("이름: ")
# student["score"] = input("점수: ")  #input은 모두 문자열로 생각한다
# print(student)
#
# student["name"] = input("이름: ")
# student["score"] = int(input("점수: "))
# print(student)
#
#세트
fruits = {"사과", "딸기", "귤", "귤"} #중복불가
print(fruits)

apple_str = set("apple") #set 알파벳분리
print(apple_str)

num = {1,2,5,5,6}
# num.add(8) #추가
# num.remove(19) #삭제 - 존재하지 않는 값일 경우 오류를 띄운다
# num.discard(19) #삭제 - 존재하지 않는 값일 경우 오류를 띄우지는 않는다
num.update([10,11,12]) #여러개 한번에 추가
print(num)

empty_set = {} #세트의 빈값이 아니라 딕셔너리의 빈값
print(empty_set)

empty_set = set() #세트의 빈값
print(empty_set)

num.clear() #요소 전체 제거
print(num)


# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# #합집합
# print(a.union(b))
# print(a|b)
# #교집합
# print(a.intersection(b))
# print(a&b)
# #차집합
# print(a.difference(b))
# print(a-b)
# print(a.symmetric_difference(b))
#
# color = {"b","l","u","e"}
# print(color.pop()) #랜덤으로 사라짐
# print(color)

a = [21,22,23,25,26]
b = [22,24,27]
common = set(a) & set(b) #리스트 형태를 세트로 형변환
print(common)

python_class = ["수현", "현호", "지니", "가인"]
java_class = ["현호", "지니", "홍수", "찬호"]
#공통으로 출석한 학생 :
common_class = set(python_class) & set(java_class)
print(common_class)
#파이썬만 출석한 학생 :
python = set(python_class) - set(java_class)
print(python)
#자바만 출석한 학생 :
java = set(java_class) - set(python_class)
print(java)

# common = set(python_class) & set(java_class)
# print(common)
#
# difference = set(python_class) - set(java_class)
# print(difference)
#
# difference2 = set(java_class) - set(python_class)
# print(difference2)