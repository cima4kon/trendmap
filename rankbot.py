import json, os
from datetime import datetime
from urllib.parse import quote

# 1. 단지 리스트 및 기본정보
apartment_list = [
    {"name": "동탄 포레파크 푸르지오", "location": "화성시 산척동", "builder": "대우건설", "units": 1000, "date": "2025-06-25"},
    {"name": "고덕강일 대성베르힐", "location": "서울 강동구", "builder": "대성건설", "units": 890, "date": "2025-06-30"},
    {"name": "청주 동남파크자이", "location": "청주시 상당구", "builder": "GS건설", "units": 1250, "date": "2025-07-10"},
    {"name": "힐스테이트 만촌역", "location": "대구 수성구", "builder": "현대건설", "units": 780, "date": "2025-06-20"},
    {"name": "연산 더샵 센텀포레", "location": "부산 연제구", "builder": "포스코건설", "units": 660, "date": "2025-07-05"},
    {"name": "하남 감일 푸르지오", "location": "하남시 감일동", "builder": "대우건설", "units": 970, "date": "2025-07-01"},
    {"name": "세종 자이 더 시티", "location": "세종시 6-4생활권", "builder": "GS건설", "units": 850, "date": "2025-07-03"},
    {"name": "의정부 푸르지오 센트럴", "location": "의정부시 가능동", "builder": "대우건설", "units": 920, "date": "2025-06-28"},
    {"name": "창원 한화 포레나", "location": "창원시 성산구", "builder": "한화건설", "units": 1050, "date": "2025-07-08"},
    {"name": "파주 운정 더샵 라피아노", "location": "파주시 운정3지구", "builder": "포스코건설", "units": 760, "date": "2025-07-12"},
]

# 2. 블로그 포스팅이 존재하는 단지 (슬러그 기준)
blog_posts = ["동탄-포레파크-푸르지오", "청주-동남파크자이"]

def make_main_link(name):
    slug = name.replace(" ", "-")
    if slug in blog_posts:
        return f"https://sangbalnam.com/{slug}"
    else:
        return f"https://hogangnono.com/search/{quote(name)}"

# 3. 오늘 날짜 파일명 생성
today = datetime.now().strftime("%Y-%m-%d")
os.makedirs("data", exist_ok=True)
filename = f"data/{today}.json"

# 4. 순위 부여 + 링크 포함
output = []
for i, apt in enumerate(apartment_list):
    output.append({
        "rank": i + 1,
        "name": apt["name"],
        "location": apt["location"],
        "builder": apt["builder"],
        "units": apt["units"],
        "date": apt["date"],
        "main_link": make_main_link(apt["name"]),
        "news_link": f"https://search.naver.com/search.naver?query={quote(apt['name'] + ' 분양')}"
    })

# 5. JSON 파일 저장
with open(filename, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✅ JSON 저장 완료: {filename}")
