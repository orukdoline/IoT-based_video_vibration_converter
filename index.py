#%%
import vlc
import time
import socket
from str_convert import SceneAnalyzer

# OpenAI API 키
API_KEY = '********'

# 아두이노 IP와 포트 설정
ARDUINO_IP = '192.168.0.0'
ARDUINO_PORT = 23

# 시간 문자열을 초로 변환하는 함수
def convert_time_to_seconds(time_string):
    hours, minutes, seconds_ms = time_string.split(':')  
    seconds, milliseconds = seconds_ms.split(',')  
    return 3600 * int(hours) + 60 * int(minutes) + int(seconds)

# 이벤트 값(시작 시간, 종료 시간, 강도)을 추출하는 함수
def extract_event_values(event):
    time_range, intensity = event  
    start_time_string, end_time_string = time_range.split(' --> ')  
    start_time = convert_time_to_seconds(start_time_string)  
    end_time = convert_time_to_seconds(end_time_string)  
    return start_time, end_time, intensity

# 아두이노에 진동 강도를 전송하는 함수
def send_intensity(connection, intensity):
    connection.send(str(intensity).encode())

# 자막 분석기 초기화
analyzer = SceneAnalyzer(API_KEY, 'sample.srt')  
events = analyzer.process_subtitle()

# 아두이노에 연결
connection = socket.socket()  
connection.connect((ARDUINO_IP, ARDUINO_PORT))

# 연결확인 및 모듈 초기화
send_intensity(connection, 0)

# 동영상 재생
player = vlc.MediaPlayer("sample.mp4")
player.play()

# 이전 이벤트의 종료 시간 초기화
last_end_time = 0

print(events)
print('시작')

# 이벤트 처리 메인 루프
for event in events:
    # 이벤트 값 추출
    start_time, end_time, intensity = extract_event_values(event)
    
    # 이벤트 시작 시간까지 대기 (이전 이벤트 종료 시간 대비)
    time.sleep(start_time - last_end_time)
    
    # 진동 강도 전송
    send_intensity(connection, intensity)
    
    # 이벤트 종료 시간까지 대기
    time.sleep(end_time - start_time)
    
    # 진동 멈춤 (강도 0 전송)
    send_intensity(connection, 0)
    
    # 이전 이벤트의 종료 시간 업데이트
    last_end_time = end_time

# 아두이노 연결 종료
connection.close()