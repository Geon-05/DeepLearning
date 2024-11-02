import openai
import time

openai.api_key = ''

for _ in range(3):  # 최대 3회 재시도
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specializing in financial consulting."},
                {"role": "user", "content": "다음 달에 재무 계획을 세우고 싶은데 어디서부터 시작해야 할까요?"}
            ],
            max_tokens=50,
            temperature=0.5
        )
        print(response['choices'][0]['message']['content'])
        break  # 성공 시 반복문 탈출
    except openai.error.RateLimitError:
        print("Rate limit exceeded. Retrying in 5 seconds...")
        time.sleep(5)  # 5초 대기 후 재시도