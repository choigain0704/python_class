name = "최가인"
age = 22
city = "부산"
print("제 이름은" + name + "입니다") #띄어쓰기x
print("제 이름은", name, "입니다") #띄어쓰기ㅇ

"제 나이는 __ 입니다."
print("제 나이는", age ,"입니다.")
print("제 나이는 {} 이고 이름은 {} 입니다.".format(age, name))
print("제 나이는 {a} 이고 이름은 {b} 입니다.".format(a=22, b="최가인"))
print(f"제 나이는 {age} 이고 이름은 {name} 입니다.") #f-string
print("제 나이는 %s 입니다." % age) #문자열로 들어간다
print("제 나이는 %d 입니다." % age) #모든 숫자가 정수로 들어간다
print(f"제 나이는 %d 이고 이름은 %s 입니다." % (age, name))
print("제 지분은 %d%% 입니다." % 2)
floor = 32
print("제가 사는 곳은", city, "입니다")
print("제가 사는 곳은", city + "입니다.")
print("제가 사는 곳은 {} 입니다.".format(city))
print(f"제가 사는 곳은 {city} 입니다.")
print("제가 사는 곳은 %s 입니다." % city)
print("우리팀이 우승할 확률은 %d%% 입니다." % 90)
print("우리집은 {}층 입니다.".format(floor))
print(f"우리집은 {floor}층 입니다.")

print("%0.4f" % 3.1415925635)
print("%10.4f"% 3.1415925635) #%"자릿수"."몇번째소수점"f

#입력
#input()
#email = input("이메일: ")
#print(email)
#hobby = input(" 취미 : ")
#print(hobby)
#address = input("주소 : ")
#print(address)
#age= int(float(input("나이 : ")))
#print(type(age))
#print(f"제 이메일은 {email}, 제 취미는 {hobby},나이는{int(age)} 입니다.") #int 문자변환

#인덱싱은 0으로 시작한다, 음수는 -1 부터

a = "Life is too short, You need Python"
print(a[4:])
print(a[::2])

#연도, 월, 일, 날씨
#연도는 2025, 월은 02, 일은 18, 날씨는 sunny
date = "20250218sunny"
date2 = "20260218cloudy"

print(f"연도는 {date[:4]}, 월은 {date[4:6]}, 일은 {date[6:8]}, 날씨는 {date[8:]}")
print(f"연도는 {date2[:4]}, 월은 {date2[4:6]}, 일은 {date2[6:8]}, 날씨는 {date2[8:]}")


a = "Life is too short, You need Python"
print(len(a)) #len 문자열 길이
#print(a.count("t", 5, 10)#a.count 문자가 몇개 있는지
#print(a.index("x")) #앞에서부터 찾는데 해당 문자의 인덱스 번호
#index는 없으면 오류를 낸다.
print(a.find("x")) #문자열에만 사용가능
#find는 없으면 '-1'을 출력한다.(index와 차이점)
print(a.lower) #upper 소문자/대문자
print(a[0].isupper())
print(a.replace("short","long")) #원문에 영향 없음
print(a)

print(a.strip())#strip 공백제거
print(a.replace(" ",""))

print(a.split()) #tab, 공백, 쉼표 기준으로 리스트형태로 나뉨
b= "a:b:c:d"
print(b.split(":"))

email = input("email: ") #choigain0704@naver.com
#id는 choigain0704
print(f"id는 {email[0:12]}")
email.find("@") # => index 번호 찾기
email.index("@")
print(email.split("@")[1])
print(email[:email.find("@")]) #슬라이싱


