# import cv2
# from ultralytics import YOLO
#
# model = YOLO("yolov10n.pt")
#
# cap = cv2.VideoCapture(0)
#
# while cap.is0pened():
#     success, frame = cap.read()
#     if not success:
#         break
#     results = model(frame)
#     for r in results:
#         annotated_frame = r.plot()
#     cv2.imshow("YOLOv10 Real-Time Detection", annotated_frame)
#
#     if cv2.waitKey(1) & 0xff == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#영어단어파일 json으로 바꾸기 검색
#엑셀-파이썬

#---------------------------------------------------------------------------------------------------------

#영어 단어장 만들기 --(일본어 단어장도 만들어보기)
#기능 : 난이도 선택, 랜덤으로 단어 뜻 출력, 해당 영어단어를 입력=> 정답:다음으로 틀리면 오답노트 리스트 만들어서 데이터셋
#메뉴에서 복습하기 => 오답노트에 있는 단어들을 불러 올 것

#메뉴선택-공부하기-난이도선택-정답맞추기-틀리면 오답리스트
#메뉴선택-복습하기-틀렸던 오답리스트 불러오기-공부하기

import json
import random

def study(level):
    review_list = []

    with open("words.json", "r", encoding="utf-8") as file :
        word_list = list(json.load(file))
        filtered_word_list = list(filter(lambda x: x["level"] == level, word_list))
        count = 0

        while count < 5:
            select_index = random.randint(0, len(filtered_word_list))
            print("=====================")
            print(f"{filtered_word_list[select_index]["meaning"]}")

            input_eng = input("단어 : ")
            if input_eng == filtered_word_list[select_index]["word"]:
                print("정답입니다!!!")
            elif input_eng != filtered_word_list[select_index]["word"]:
                print("오답입니다!!!")
                print(f"정답 : {filtered_word_list[select_index]["word"]}")
                review_list.append(filtered_word_list[select_index])


            count += 1

    with open("review_note.json", "w", encoding="utf-8") as review_file:
        json.dump(review_list, review_file, indent=4, ensure_ascii=False)

def review():
    with open("review_note.json", "r", encoding="utf-8") as review_file:
        word_list = list(json.load(review_file))

        incorrect_count = 0
        for word_index in range(0, len(word_list)):
            print("=====================")
            print(f"{word_list[word_index]["meaning"]}")
            input_eng = input("단어 : ")
            if input_eng == word_list[word_index]["word"]:
                print("정답입니다!!!")
            elif input_eng != word_list[word_index]["word"]:
                print("오답입니다!!!")
                print(f"정답 : {word_list[word_index]["word"]}")
                incorrect_count +=1

        if incorrect_count == 0:
            print("오답 노트를 전부 맞췄습니다")

while True:
    print("========메뉴========")
    print("""
        1. 초등
        2. 중고
        3. 전문
        4. 오답노트
    """)

    choice = input("메뉴를 선택하세요: ")
    if choice == "1":
        study("초등")
    elif choice == "2":
        study("중고")
    elif choice == "3":
        study("전문")
    elif choice == "4":
        review()
    else:
        print("다시 선택해 주세요.")

