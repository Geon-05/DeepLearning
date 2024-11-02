import os
import google.generativeai as genai
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
target_file_path = os.path.join(current_dir, '../data/APIkey.json')

# 파일 읽기
with open(target_file_path, 'r') as file:
    data = json.load(file)  # JSON 파일을 파이썬 딕셔너리로 로드

# 환경 변수에서 API 키 가져오기
api_key = data['Gemini']

# API 키 설정
genai.configure(api_key=api_key)

# 모델 초기화
model = genai.GenerativeModel("gemini-1.5-flash")

text = input('질문을 입력하세요. : ')

response = model.generate_content(text)
print(response.text)