# weather = "비" # weather 변수에 값 할당
# print("비가 오나요?", weather == "비") # weather == 비  비교연산자
# if weather == "비": # weather의 값이 "비"와 같은면 조건식이 True이므로 안쪽코드 블럭 실행
#     print("우산을 가져간다")
# else: # 조건식이 False이면 실행
#     print("우산을 가져가지 않는다")    

weather = "맑음" # weather 변수에 값 할당
print("비가 오나요?", weather == "비") # weather == 비  비교연산자
if weather == "비": # weather의 값이 "비"와 같은면 조건식이 True이므로 안쪽코드 블럭 실행
    print("우산을 가져간다")
elif weather == "맑음":
    print("날씨가 좋다")
else: # 조건식이 False이면 실행
    print("우산을 가져가지 않는다")    

        