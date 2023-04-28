# 데이터 수집단계
# 데이터수집 -> 데이터분석/처리 -> 인공지능 모델 학습 -> 인공지능 모델 평가 -> 사용

# 알아야할 것
# http(HyperText Transfer Protocol) 웹페이지의 데이터 전송방식의 구성
# request(요청) - response(응답)
# client(요청) - server(응답)
# client는 정확히 웹브라우저  

# html(HyperText Markup Language)
# 웹사이트를 표현하기 위한 언어
# <html></html>
# html을 읽고 분석하는 것 파싱

# import requests
# url = "https://www.naver.com/"
# response = requests.get(url)
# status = response.status_code
# html = response.text
# print(status)
# print(html)

# http 상태 코드
# 200 : OK (요청성공)
# 302 : 리다이렉트 (다른 페이지로 바로 연결)
# 400 : Bad Request (요청이 잘못됨)
# 401 : unauthorized (비인증됨)
# 403 : Forbidden (접근 권한 없음)
# 404 : Not Found (요청받은 내용이 없음) 주소를 잘못 입력했을 때 제일 많이 나옴
# 405 : Method Not Allowed (접근방법이 잘못됨)
# 500 : Internal Server Error 서버에러 (개발자 문제)
# 501 : Not Implemented
# 502 : Bad Gateway 잘못된 응답 (서버에 문제)

# ip주소는 인터넷에 연결된 특정한 컴퓨터를 찾을 때 사용

# url 구조
# 프로토콜://호스트주소(서버주소):포트번호/경로(호스트에서 보여주는 하위요소들)?쿼리(경로와는 다른 추가적인 데이터를 입력)
# http://naver.com/?~~~~~


# BeautifulSoup
# html 파싱(parsing)을 진행함
# html을 객체 구조화해서 파이썬 문법으로 사용
# html 태그
# <태그이름 속성=속성값>내용</태그이름>
# html = "<html><body>Hello</body></html>"
# soup = BeautifulSoup(html, "html.parser")
# print(soup.body.text)
# print(type(soup.body.text))


# import requests
# from bs4 import BeautifulSoup
# search_url = "https://www.google.com/search?tbm=isch&q="
# # 쿼리이름=값&쿼리이름=값&쿼리이름=값
# keyword = "맥주"
# url = search_url + keyword
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# imgs = soup.find_all('img')
# import os
# folder_name = "imgs"
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
# for idx, img in enumerate(imgs[1:]):
#     print(idx, "번째 이미지 저장")
#     file_name = f"{keyword}_{idx}.jpg"
#     file_path = os.path.join(folder_name, file_name)
#     img_response = requests.get(img['src'])
#     img_data = img_response.content
#     with open(file_path, "wb") as f:
#         f.write(img_data)

# enumerate(이터러블) 이터러블에 번호를 붙임(인덱스형으로)
# li1 = ["김연아", "류현진", "손흥민"]
# for name in enumerate(li1):
#     print(name)

# 네이버 IT/과학 뉴스 크롤링

import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
# 크롤링 방지 회피 코드 headers={"user-agent": "Mozilla/5.0"}
response = requests.get(url, headers={"user-agent": "Mozilla/5.0"})
html = response.text
soup = BeautifulSoup(html, "html.parser")
div = soup.body.find('div', attrs={'class': 'list_body'})
headlines = div.find_all('a', attrs={'class': 'cluster_text_headline'})
import os
folder_name = "crawling_resut"
if not os.path.exists(folder_name):
    os.mkdir("crawling_resut")
for headline in headlines:
    # 과제 crawling_result 폴더의 headlines.txt 파일에 저장
    # with open("crawling_result/headlines.txt", "a", encoding="utf-8") as f:
    #     f.write(headline.text.strip())
    #     f.write("\n")
article_response = requests.get(headline['herf'])
article_soup = BeautifulSoup(article_response.text, "html.parser")
article = article_soup.find('div', attrs={"id":"dic_area"})
print(article.text)