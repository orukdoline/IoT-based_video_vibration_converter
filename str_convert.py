import re
from openai import OpenAI

class SceneAnalyzer:
    # API 키와 파일명을 받아 객체 초기화
    def __init__(self, api_key, filename):
        self.client = OpenAI(api_key=api_key)  # OpenAI API 클라이언트 생성
        self.filename = filename  # 파일명 저장

    # GPT API를 사용하여 자막 내용의 감정 강도를 1~5로 평가하는 함수
    def scene_analysis(self, content):
        response = self.client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"This is a scene description: '{content}'. Rate the intensity of the scene on a scale of 1 (calm) to 5 (intense). Please respond with a number between 1 and 5.",
            temperature=0.5,
            max_tokens=10
        )
        try:
            # 숫자 추출 및 변환
            intensity = round(float(response.choices[0].text.strip()))
            if 1 <= intensity <= 5:
                return intensity
            # 에러 문구 출력
            else:
                raise ValueError()
        except ValueError:
            print(f"Unexpected response: {response.choices[0].text.strip()}")
            return None

    # 파일을 읽고 시간 정보와 대괄호 안의 자막 내용을 추출하여 리스트에 저장하는 함수
    def extract_bracket_content_and_time(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {self.filename}")
            return []

        bracket_contents_with_time = []
        current_time = None
        pattern = re.compile(r'\[(.*?)\]')  # 대괄호 안의 내용 추출 정규식

        for line in lines:
            line = line.strip()  # 개행 문자 제거
            if '-->' in line:
                current_time = line  # 시간 정보 저장
            else:
                matches = pattern.findall(line)  # 대괄호 안의 내용 찾기
                for match in matches:
                    bracket_contents_with_time.append((current_time, match))
        return bracket_contents_with_time

    # 자막의 시간과 내용을 추출하고 감정 강도를 분석하여 반환하는 함수
    def process_subtitle(self):
        bracket_contents_with_time = self.extract_bracket_content_and_time()

        for i in range(len(bracket_contents_with_time)):
            time, content = bracket_contents_with_time[i]
            intensity = self.scene_analysis(content)
            if intensity is not None:
                bracket_contents_with_time[i] = (time, intensity)  # 감정 강도 업데이트

        return bracket_contents_with_time

if __name__ == "__main__":
    # 메인 실행 코드: 자막 분석을 수행하고 결과 출력
    analyzer = SceneAnalyzer('api-key', 'srt_dir')
    results = analyzer.process_subtitle()
    print(results)