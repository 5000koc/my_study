# li_1 = ["Hello", "World", "Python"]
# li_2 = [1, 2, 3]

# print(li_1[0], li_1[1], li_1[2])

# # join(리스트)
# # 리스트의 문자열을 합친다
# print(" ".join(li_1))
# print(li_1[0] + " " + li_1[1] + li_1[2])

# print(li_1[0][:3] + li_1[2][0])

# print(li_1 + li_2)

# li_1.extend(li_2)
# print(li_1)

# li_1.insert(1 ,li_2[0])
# li_1.insert(3, li_2[1])
# li_1.insert(5, li_2[2])
# print(li_1)

# li_1 = ["Hello", "World", "Python"]
# li_1.insert(1, li_2[0])
# li_1.insert(3, li_2[1])
# li_1.append(li_2[2])
# print(li_1)


# ""
# scores = []
# scores = list() # 둘이 같은 명령
# scores.append(int(input("영어 점수:")))
# scores.append(int(input("국어 점수:")))
# scores.append(int(input("수학 점수:")))

# avg = (scores[0] + scores[1] + scores[2])/ 3
# avg = sum(scores) / 3 # 리스트의 모든 요소를 더한다
# if avg >= 91:
#    print("A")
# elif avg >= 81:
#    print("B")
# elif avg >= 71:
#    print("C") 
# elif avg >= 61:
#    print("D")
# elif avg < 60:
#    print("F") 
# ""

# 나이와 가지고 있는 돈을 입력받는다
# 가지고 있는 돈으로 물건을 몇개 살 수 있는지와 잔돈을 출력한다
# 물건의 값은 500원이다

age = input("나이:")
money = int(input("돈:"))
price = 500
print(money // price)
print(money % price)
 
# 나이와 가지고 있는 돈을 입력받는다
# 가지고 있는 돈으로 물건 별로 각각 살수 있는 갯수와 잔돈을 출력한다
# 물건의 가격은 1번 물건은 1000원 2번 물건은 50원 3번 물건은 120원이다

age = input("나이:")
money = int(input("돈:"))
price = [1000, 50, 120]
print(money // price[0], money % price[0])
print(money // price[1], money % price[1])
print(money // price[2], money % price[2])
