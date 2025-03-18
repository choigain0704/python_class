#가위바위보 게임
import random
import time

choice_list = ["가위", "바위", "보"]
user_choice = ""  #선택지는 문자이므로 ""
computer_choice = ""
user_score = 0   #점수는 숫자이므로 0
computer_score = 0
same_score = 0

while True:
    if user_score == 5:
        print("사용자 승리 ~!!!")
        break
    elif computer_score == 5:
        print("컴퓨터 승리 ~!!!")
        break

    user_choice = input("가위, 바위, 보 중 선택해 주세요(그만하려면 종료): ")

    if user_choice not in choice_list and user_choice != "종료":
        print("가위, 바위, 보 중 다시 선택해 주세요: ")
        continue

    if user_choice == "종료":
        print(f"종료되었습니다. 컴퓨터 - {computer_score} 사용자 - {user_score} 무승부 - {same_score}")
        break

    computer_choice = random.choice(choice_list)

    print("-------------두구두구-------------")
    time.sleep(2)

    if user_choice == computer_choice:
        print("무승부 입니다.")
        same_score += 1

    elif ((user_choice == "가위" and computer_choice == "보") or        #마음대로 줄바꿈 한 후 or\
          (user_choice == "바위" and computer_choice == "가위") or
          (user_choice == "보" and computer_choice == "바위")):
        print("이겼습니다!!!")
        user_score += 1
    else:
        print("졌습니다ㅠㅠ")
        computer_score += 1


    print(f"컴퓨터 - {computer_score} 사용자 - {user_score} 무승부 - {same_score}")
    continue

