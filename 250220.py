fruits = ["strawberry", "kiwi", "orange"] #문자열 리스트
numbers = [6,3,1,5] #숫자 리스트
bools = [True, False, True] #불리언 리스트
mixed_list = ["안녕하세요", 12, True] #혼합 리스트
#a = ("first")

print(fruits)
print(fruits[2]) #orange
print(fruits[2][1]) #orange 중 r
print(fruits[-2]) #kiwi

fruits[1] = "cherry" #요소변경
print(fruits)

#numbers.append("hi") #요소추가(가장 끝에)
#print(numbers)
#numbers.insert(1,2) #특정자리에 요소추가 (인서트1 자리에 2를 대입)
#print(numbers)

#numbers.pop() #요소삭제1
#print(numbers.pop()) #리스트의 마지막 요소가 리턴
#numbers.remove("hi") #삭제2
#print(numbers)
#del numbers[5] #삭제3
#print(numbers)

#print(len(mixed_list)) #리스트의 길이
numbers.sort() #순서배열(작은순)
print(numbers)
#numbers.sort(reverse=True) #옵션(큰순)  #Ctrl+Space Bar = 옵션보기
print(numbers)
bools.sort()
print(bools)
fruits.sort()
print(fruits)

numbers.reverse() #순서를 거꾸로
print(numbers)

fruits = "-".join(fruits) #지정한 문자열로 합치기
print(fruits)

# cart = []
# cart.append(input("추가할 상품: "))
# cart.append(input("추가할 상품: "))
# cart.append(input("추가할 상품: "))
#
# print(cart)

colors = ("red", "green", "black", "yellow") #변경불가능
numbers = (1,5,3,9,1,2)
bools   = (True, False, True)
mixed_tuple = ("red", 1, True)
#a = ("first", ) #튜플은 요소가 하나일 경우 뒤에 콤마

print(colors[1])
#colors[1] = "yellow" #튜플은 변경 불가능
print(numbers[0:2]) #튜플은 슬라이싱 가능
print(numbers.count(1)) #튜플은 카운트 가능
print(numbers.index(9)) #해당 인덱스 찾기

a,b,c,d = colors #unpacking a-red, b-green, c-black
print(d)

