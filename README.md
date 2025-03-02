# IoT기반 영상 진동 변환기

<br>

## 프로젝트 개요 🔍
- 청각 장애인 사용자들이 영상 콘텐츠를 더욱 쉽게 이해할 수 있도록 **SRT 자막 데이터를 분석하여 진동 신호로 변환**하는 시스템을 개발하는 것을 목표.  
- 영상 속 자막의 감정 강도를 분석한 후, 이를 진동 모듈을 통해 전달하여 **청각 대신 촉각을 활용한 미디어 경험**을 제공.  

<br>

## 프로젝트 기간 ⏰
2023.06 ~ 2023.07

<br>

## 프로젝트 목표 🎯
| 목표 | 내용 |
|---|---|
| **배리어프리 자막의 변환** | 청각 장애인 사용자들이 영상 콘텐츠를 이해하는데 도움이 되는 배리어프리 자막을 대체 감각인 진동으로 변환하는 기술 개발 |
| **청각 장애인의 정보 격차 해소** | 청각 장애인 사용자들이 디지털 미디어 콘텐츠를 더욱 손쉽게 접근하고 이해할 수 있게 하여 정보 격차의 해소와 디지털 미디어의 보편적 사용 촉진 |
| **청각 장애인에게 동등한 미디어 경험 제공** | 청각 장애인 사용자들에게 OTT 서비스와 같은 영상 콘텐츠 시장에서 더욱 다양하고 풍부한 사용자 경험을 제공하여 일반인과 동등한 경험을 갖게 함 |

<br>

## 프로젝트 내용 📔

| 내용 | 설명 |
|---|---|
| **SRT 파일 정보 추출 및 변환 알고리즘** | SRT 파일에서 자막 정보를 추출하고 이를 진동 신호로 변환하는 알고리즘을 개발하여 사용자에게 오디오 정보를 대체 감각인 진동으로 제공 |
| **PC 및 아두이노간 무선 통신** | 변환된 진동 신호를 아두이노로 전송하여 아두이노가 진동 모터를 제어할 수 있도록 WiFi를 활용한 무선 통신 구현 |
| **변환된 정보 기반 진동 모터 모듈 제어** | 아두이노가 받은 정보를 기반으로 진동 모터를 제어하여 자막의 내용을 물리적인 감각으로 경험하게 하고 오디오 부분을 이해할 수 있도록 피드백 제공 |

<br>

## 하드웨어 구성 🔧
| 부품 | 설명 |
|---|---|
| **아두이노 우노 R4 WiFi** | WiFi 연결을 통해 PC와 아두이노 간의 무선 통신을 지원하는 아두이노 보드. |
| **진동 모듈 (SKU: ELB060416)** | 아두이노의 3번 핀에 연결된 진동 모듈로, 변환된 진동 신호를 사용자에게 전달하는 역할. |

<br>

## 소프트웨어 구성 🏗️  
| 기술         | 파일명           | 설명 |
|-------------|----------------|-------------------------------------------------------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | `index.py` | 웹소켓을 활용하여 생성된 진동 강도 정보를 아두이노로 전송. |
| ![OpenAI API](https://img.shields.io/badge/OpenAI%20API-412991?style=for-the-badge&logo=openai&logoColor=white) | `str_convert.py` | 자막의 감정 분석을 수행하여 진동 강도를 결정. |
| ![Arduino C](https://img.shields.io/badge/Arduino%20C-00979D?style=for-the-badge&logo=arduino&logoColor=white) | `arduino.ino` `arduino_secrets.h`| 아두이노를 프로그래밍하여 진동 모터를 제어. |

<br>

## 실행 방법 📋
1. 🌐 [OpenAI API](https://openai.com/api/) 사이트로 접속하여 **API 키**를 발급받습니다. (유료 서비스)
2. 🔑 `index.py` 파일에서 **API_KEY** 값을 발급받은 키로 변경합니다.
3. 🌍 `index.py` 파일에서 **ARDUINO_IP** 값을 아두이노의 **IP 주소**로 변경합니다.
4. 🎬 `index.py` 파일에서 **sample.srt**는 **자막 파일명**으로, **sample.mp4**는 **영상 파일명**으로 변경합니다.
5. 📶 `arduino_secrets.h` 파일에 아두이노가 연결할 **WiFi 정보**를 입력합니다.
6. 🗂 자막 파일과 영상 파일을 `index.py`와 동일한 경로에 위치시킵니다.
7. ⚡ 아두이노 전원을 켜고 **WiFi 연결**을 확인한 후, `index.py` 파일을 실행합니다.


