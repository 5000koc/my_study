# tuple(튜플)형
# element값을 정해지면 수정할 수 없다
# mutable / immutable
# mutable 수정 가능 함수 list, dict
# immutable 수정 불가 함수 int, float, str, tuple

# mutable 예시
# my_list = [1, 2, 3]
# my_list[0] = 5
# print(my_list)

# immutable 예시 수정불가 에러메세지 출력
# my_tuple = (1, 2, 3)
# my_tuple[0] = 5
# print(my_tuple)

#사용 예시
tuple_1 = ("Hello", "World", "Python")
t2 = (1, 2, 3, 4, 5)
t3 = (1, 2, "Hello")
t4 = 1, 2, 3
t5 = (1, 2, (3, 4, 5))

t6 = tuple_1 + t2 # 이어붙이기 
t7 = t3 * 3 # 반복하기
t7 = t3 * 4

t3 = (1, 2, "Hello")
print(t3[2])
print(t3[0:2]) #tuple로 가져온 데이터는 수정이 안됨
print(len(t3))

t5 = (1, 2, (3, 4, 5))
print(t5[2][1])

t8 = (5, 3, 1, 4, 2) # 순서, 위치를 바꾸는 것도 값의 변경이라서 이 식은 되지 않음


for i in t8:
    print(i)
