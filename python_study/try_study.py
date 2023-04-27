# 예외 처리 = 오류 처리
# 오류 발생을 잡아내서 처리하는 것

# li = [1, 2, 3, 4, 4]
# li[100]

# f = open("없는파일", "r")

# # 에러발생 시 프로그램을 중단하고 에러 메세지를 보여준다

# # 예외처리 구문
# # try ~ except
# # try 블록에는 오류가 발생할 수 있는 코드
# # except 블록에는 오류가 발생했을 때 수행할 코드
# # 에러가 발생하지 않으면 except 블록의 코드가 실행되지 않음
# try:
#     100 / 0
# except:
#     print("에러 발생")

# print("에러 발생 후")


# try:
#     100 / 0
# except Exception as e: # Exception 오류객체
#     print(e)

# print("에러 발생 후")


# try:
#     100 / 0
# except ZeroDivisionError as e: # 구체적인 에러를 특정해서 예외로 처리 다양한 오류 대응 불가
#     print(e, "0으로 나눌 수 없습니다")
# except IndexError as e:
#     print(e, "인덱싱 할 수 없습니다")

# print("에러 발생 후")

# Finally
# 예외 발생 여부와 상관없이 항상 수행되는 코드
# try:
#     f = open("없는 파일", "r")
# except:
#     print("에러발생")
# finally
#     f.close()

# else
# 오류가 발생하지 않으면 실행되는 코드
# try:
#     age = int(input("나이: "))
# except:
#     print("입력이 잘못 되었습니다") 
# else:
#     if age >= 20:
#         print("성인입니다")
#     else:
#         print("미성년자 입니다")

class Bird:
    def fly(self):
        raise NotImplementedError

my_bird = Bird()
my_bird.fly()


