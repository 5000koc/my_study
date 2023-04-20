# for문
"""
for 변수 in iterable값:
    반복할 코드
"""
# li_1 = ["one", "two", "three"]
# for i in li_1:
#     print(i)
# 첫번째 요소부터 마지막 요소까지
# 변수에 대입하도록 반복
# s1 = "hello"
# for i in s1:
#     print(i)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(number)

# numbers.reverse()
# for number in numbers:
#     print(number)

# range()
# range(끝 정수)
# 0 ~ 끝 정수 - 1
# for i in range(10): # 0 ~ 9 까지 출력
#     print(i)

# range(시작, 끝)
# 시작 ~ 끝 - 1
# for i in range(1, 11): # 1 ~ 10 까지 출력
#     print(i)

# range(시작, 끝, 스텝)
# 시작 ~ 끝 - 1 까지인데 스탭만큼 차이나게
# for i in range(1, 20, 2):
#     print(i)

# 연습
# For문을 사용해 2부터 30까지 출력
# for i in range(2, 31):
#     print(i)

# for문을 사용해 2부터 30까지 숫자 중 짝수만 출력
# for i in range(2, 31):
#    if i % 2 == 1 : #홀수 출력을 이렇게 넣어도 됨
#       # continue
#       pass # 아무것도 안하고 그냥 넘어갈 때
#    else: # 짝수
#     print(i)

# for i in range(2, 31)
#     if i % 2 == 0: #짝수
#        print(i)

# for i in range(2, 31, 2):
#    print(i)

# for문을 사용해 10부터 1까지 출력
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers.reverse()
# for number in numbers:
#     print(number)

# for i in range(10, 0, -1):
#     print(i)

# for i in reversed(range(1, 11)):
#     print(i)

# for i in range(1, 11)[::-1]: # [시작인덱스:끝인덱스:방향] 슬라이싱
#     print(i)    

# money = 2000
# price = 1000
# coffee = 5
# for i in range(coffee):
#     print("커피를 구매했습니다")
#     money -= price # money = money - price
#     print("남은 커피 :", coffee - 1 - i)
#     if money < price:
#         break

# for i in range(1, coffee + 1): # 1 ~ 5
#     print("남은 커피 :", coffee - i) # 4 ~ 0

# for i in range(coffee):
#     coffee -= 1
#     print("남은 커피 :", coffee) # 4 ~ 0

# while문은 조건시을 체크하면서 동작
# 특정시점까지 동작을 할 때 적절

# prices = [500, 700, 930]
# money = int(input("돈:"))
# for i in range(len(prices)):
#     price = prices[i]
#     print(money // price)
#     print(money % price)
# for price in prices:          # 정말로 중요함
#     print(money // price)     # prices 변수를 가져와서 대입
#     print(money % price)      #

# scores = []
# for i in range(5):
#     score = int(input("시험점수:"))
#     scores.append(score)

# 구구단 2단 출력
# for i in range(1, 10): # 1 ~ 9
#     print("2 * ", i, "=", 2*i)

# 이중 for문 구구단 출력
# for i in range(2, 10): # 2 ~ 9
#     print(i, "단")
#     for j in range(1, 10): # 1 ~ 9
#         print(i, "*", j, "=", i*j)
#     print("--------------")
