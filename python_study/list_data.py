# 리스트(list)자료형
# 여러개의 값을 변수 1개에 저장
# [1, 2, 3, 4, 5, 6, 7] # 이런 식으로 넣거나
# [1, 1, 1, 1, 1] # 똑같은 수를 넣어도 됨
# ["Hello", "World", "Python"] # 문자도 가능
# [1, "Hello", 2, "Wow"] # 이렇게도 가능
# [1, 2, ["Hello", "World"]] # 가능
# [] # 빈칸으로도 사용가능 추후 추가로 사용 가능
# [] 칸에 들어가는 데이터는 엘레멘트, 원소라고 칭함

# 인덱싱 가능
# li_1 = [1, 2, 3] 
# print(li_1[0])
# print(li_1[1])
# print(li_1[2])
# print(li_1[0] + li_1[1]) #인덱싱한 데이터를 더하기도 가능
# print(li_1[2] - li_1[1]) # 빼기나 다른 것도 가능
# li_2 = [1, 2, 3, [4, 5, 6]] #리스트 안에 또 리스트로 묶이면 하나로 봄

# 슬라이싱 가능
# print(li_2[3][0])
# print(li_2[2:3])
# print(li_2[1:])
# print(li_2[:2])
# print(li_2[3][0:2])
# print(li_2[0:1])
# print(li_2[0])

# li_3 = [1, 2, 3, 4, 5]
# # 출력결과가 [2, 3]이 되도록 하시오
# print(li_3[1:3])
# print(len(li_3)) # len함수를 이용 원소의 길이체크 가능
# li_3[0] = 10 # 이렇게 먼저 들어가있던 인덱스의 값을 수정할 수 있음
# print(li_3)
# [10, 2, 3, 4, 5] 이렇게 출력이 됨


# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]] #이런 식으로 행과 열을 묶음

# append(원소)
# # 리스트 마지막에 원소(엘레멘트)를 추가
# li_4 = [1, 2, 3]
# li_4.append(4) #()에는 문자도 가능 ("문자")
# print(li_4)

# # insert(인덱스, 원소)
# # 인덱스 위치에 원소 삽입
# li = [1, 2, 3]
# li.insert(1, 10) #위치 지정 삽입이 가능
# print(li) 
#[1, 10, 2, 3] 이렇게 출력

# remove(값)
# 리스트에서 함수에 입력된 값과 같은 값을 찾아 삭제함
# 리스트에 같은 값이 있을 때 먼저 위치한 값을 삭제함
# 리스트에 없는 값은 넣으면 에러 발생
# li = [1, 2, 3]
# li.remove(2)
# print(li)
#[1, 3] 이렇게 출력

# pop(인덱스)
# 리스트의 인덱스 위치의 요소를 꺼냄
# 인덱스를 함수에 전달하지 않으면 제일 마지막 요소를 꺼냄
# li = [1, 2, 3, 4]
# a = li.pop()
# print(li)
# print(a)
# b = li.pop(1)
# print(li)
# print(b)
#결과값
# [1, 2, 3]
# 4
# [1, 3]
# 2

# index(값)
# 리스트에서 값을 찾아 그 값의 인덱스를 돌려준다
# 값이 리스트에 없으면 에러
# li[2] -> 인덱싱(이덱스로 값에 접근)
# li.index(값) -> 인덱스로 알아내기
# li = [1, 2, 3]
# idx = li.index(2)
# print(idx)
# 1이 출력

# sort()
# 리스트의 요소를 순서대로 정렬한다
# li = [5, 3, 1, 4, 2]
# # li.sort()
# li.sort(reverse = True) #이렇게 넣으면 거꾸로 정렬
# print(li)

# reverse()
# 리스트의 순서를 뒤집는 함수
# 정렬 아님
# li = [5, 1, 3, 4, 2]
# li.reverse()
# print(li)
# [2, 4, 3, 1, 5] 결과값

# count(값)
# 리스트 안에서 해당 값이 몇개 있는지 세는 함수
# li = [1, 2, 3, 2]
# cnt = li.count(2)
# print(cnt)
# 2가 2개 있으므로 2를 출력

# + 연산자
# 리스트를 연결한다
# extend(연결할 리스트) 함수와 같다
# li_1 = [1, 2, 3]
# li_2 = [4, 5, 6]
# li_1.extend(li_2)
# print(li_1) # extend를 쓰지 않으면 + 연산자로 쓰면 됨
# [1, 2, 3, 4, 5, 6] 결과값

# * 연산자
# 리스트를 반복한다
# li = [1, 2, 3]
# print(li * 3)
# [1, 2, 3, 1, 2, 3, 1, 2, 3] 결과값