import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "gemini에서는 사용자의 질문과 그에대한 답변을 자연어처리를 하기위해사용하고싶고 내부적으로는 내가만든 모델을 사용하고 싶은데 가능할까?",
      ],
    },
    {
      "role": "model",
      "parts": [
        " Gemini에서 사용자의 질문과 답변을 처리하는 데 자연어 처리를 사용하고 내부적으로는 사용자 정의 모델을 사용하는 것은 가능하지만 몇 가지 제약 사항과 고려해야 할 사항이 있습니다.\n\n**Gemini는 Google에서 개발한 대규모 언어 모델로, Google에서 제공하는 API를 통해 접근할 수 있습니다.** 따라서 Gemini 자체를 직접 수정하거나 내부 모델을 완전히 통합하는 것은 불가능합니다.\n\n**하지만 다음과 같은 방법을 사용하여 Gemini에 사용자 정의 모델을 부분적으로 통합할 수 있습니다.**\n\n1. **API를 통한 통합:** Gemini API를 사용하여 사용자 정의 모델을 호출하고 그 결과를 Gemini에 입력으로 제공할 수 있습니다. 예를 들어, Gemini를 사용하여 사용자 질문을 분석하고 관련 정보를 추출한 후 사용자 정의 모델에 전달하여 최종 답변을 생성하는 방식입니다.\n2. **파인 튜닝:** Gemini는 파인 튜닝을 통해 특정 작업에 맞게 성능을 향상시킬 수 있습니다. 사용자 정의 데이터셋을 사용하여 Gemini를 파인 튜닝하여 특정 도메인 지식이나 스타일을 학습시킬 수 있습니다.\n3. **외부 모델과의 결합:** Gemini API를 사용하여 다른 자연어 처리 모델이나 서비스를 통합할 수 있습니다. 예를 들어, 사용자 정의 모델을 사용하여 텍스트 요약을 수행한 후 Gemini를 사용하여 요약된 텍스트를 이해하고 답변을 생성하는 방식입니다.\n\n**다음과 같은 점들을 고려해야 합니다.**\n\n* **API 사용 제한:** Gemini API는 무료로 제공되는 버전과 유료로 제공되는 버전이 있으며, 각 버전은 사용량과 기능에 제한이 있을 수 있습니다.\n* **모델 크기 및 성능:** 사용자 정의 모델의 크기와 성능은 API 통합 및 파인 튜닝에 영향을 미칩니다. 큰 모델은 더 많은 컴퓨팅 리소스가 필요하며, 성능은 모델 훈련 데이터와 작업에 따라 달라집니다.\n* **데이터 준비:** 파인 튜닝을 위해서는 사용자 정의 데이터셋을 준비해야 하며, 데이터 품질은 모델 성능에 중요한 영향을 미칩니다.\n\n**결론적으로,** Gemini는 Google에서 제공하는 강력한 자연어 처리 모델로, 사용자 정의 모델을 직접 통합하는 것은 불가능하지만, API를 사용하거나 파인 튜닝을 통해 일부 기능을 확장할 수 있습니다. 사용자의 요구사항과 제약 사항을 고려하여 적절한 방법을 선택해야 합니다.\n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)