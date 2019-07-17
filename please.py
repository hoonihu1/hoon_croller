from bs4 import BeautifulSoup
import urllib.request

def get(max_count = 200):
    # base_url = "http://10000img.com/"
    url = "https://www.shutterstock.com/ko/search/%EC%97%AC%EB%93%9C%EB%A6%84?kw=%EC%9D%B4%EB%AF%B8%EC%A7%80+%EC%82%AC%EC%9D%B4%ED%8A%B8&gclid=CjwKCAjw67XpBRBqEiwA5RCocTRHWWzEE2fBTZ3LV3WObUJHkDG3YoGexUqRjBXWBwWXfXzZUw1fvBoCkaoQAvD_BwE&gclsrc=aw.ds&mreleased=1&number_of_people=1&image_type=photo&page=2"

    count = 5
    count_num = 104
    while count <= max_count:
        print("+---------[ %d번 째 이미지 ]---------+" % count)

        html = urllib.request.urlopen(url)
        source = html.read()

        soup = BeautifulSoup(source, "html.parser")
        img = soup.find_all("img")  # 이미지 태그
        img_src = img[count].get("src")  # 이미지 경로

        img_url = img_src  # 다운로드를 위해 base_url과 합침

        img_name = str(count_num)+'.jpg'

        urllib.request.urlretrieve(img_url, "./img/" + img_name)

        print("이미지 src:", img_src)
        print("이미지 url:", img_url)
        print("이미지 명:", img_name)
        print("\n")
        count += 1  # 갯수 1 증가
        count_num += 1

    else:
        print("크롤링 종료")

get(200)

