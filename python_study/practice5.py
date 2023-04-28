# 거꾸로 배열해도 같은 단어 또는 문장이 되는 회문(palindrome)인지 판별하는 함수를 정의하시오
# 함수에 문자열을 입력받고 회문이면 True
# 아니면 False를 반환하도록 정의하시오
# 함수 이름 : is_palindrome
# 반환 값 : True 또는 False

def is_palindrome(input_string):
    # 기러기
    # 소주 만병만 주소
    # 다시 합창합시다
    input_string = input_string.replace(" ", "") # 문자열공백제거

    # length = len(input_string)
    # for i in range(length//2): # 회문의 절반만 검사
    #         if input_string[i] != input_string[length - 1 - i]
    #         return False
    # return True
    
    return input_string == input_string[::-1] # 위의 내용보다 간단하게 만든 코드

result = is_palindrome("다시 합창합시다")
print(result)



