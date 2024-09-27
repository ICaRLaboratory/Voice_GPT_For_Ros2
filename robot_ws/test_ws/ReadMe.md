본 코드는 순천향대학교 전자공학과 소속 지능제어 및 로보틱스 연구실 자율주행 모빌리티 팀에서 작성된 코드입니다

작동 환경은 Python 3.11버전 / ROS2 Humble / 가상화 우분투 WSL2와 Ubuntu 22.04 LTS 입니다

---

## 작동 원리
1. 음성 인식을 사용해 구글 번역기로 명령을 내립니다
2. 내려진 명령이 txt 파일로 저장됩니다
3. txt 파일 내 번역된 명령어가 Chat-gpt의 명령창으로 복사됩니다
4. Chat-gpt가 코드를 생성하면 이를 다시 다른 txt 파일로 저장됩니다
5. txt 파일내의 코드가 Python코드로 패키징됩니다
6. 패키징 된 코드가 자동적으로 ROS2에서 빌드, 실행되어 실제 시스템으로 넘겨집니다

---

## 의존성 설치
#### 패키지
1. 본 코드를 받고 Voice_GPT_For_Ros2를 [원하는 이름_ws]로 변경합니다
2. 그 후 voice_gpt 폴더를 src로 변경합니다
3. 이하의 과정을 실행합니다

##### pyaudio 설치
    $pip install pyaudio
    $sudo apt-get install portaudio19-dev python3-pyaudio
    $pip install pyaudio

##### ALSA audio 설치
    $sudo apt-get update
    $sudo apt-get install --reinstall alsa-base alsa-utils
    $sudo alsactl init

##### 설치 확인
    $sudo apt-get install pulseaudio
    $pulseaudio --start

## 실행
#### 과정
1. 터미널을 실행하고 플라스크 서버를 개방합니다

접근 제어 비활성화
~~~
$export DISPLAY=:0
$xhost +
~~~
이 과정은 우분투 세션이 종료 될 경우 초기화 되므로 매번 실행 전 접근 제어를 비활성화 해야합니다
2. 그리고 아래의 과정을 통해 플라스크 서버를 실행합니다 
~~~
$export FLASK_APP=app.py
$export FLASK_ENV=development
$flask run --host=0.0.0.0 --port=5000
~~~

3. 다른 터미널을 실행하고 다음의 과정을 진행합니다

~~~
$cd [워크스페이스 이름_ws]
$colcon build
$source install/setup.bash
$ros2 run [선택 노드] [선택 노드]
~~~

# 코멘트
상당히 간단하게 작동하게 끔 코드를 작성해 두었습니다
또한 수정 역시 굉장히 간단하게 되어 있습니다
사용하고 싶은 언어를 변경하고 싶다면 src/voice_gpt/voice_recognition/voice_recognition/voice_recog.py의 75번 째 줄의 language=''의 국가코드를 변경하면됩니다

현재는 완성된 코드가 아닙니다
작동원리 3번을 현재 구현 중에 있으며 빠른 시일 내에 업데이트하도록 하겠습니다

Flask과 Watchdog을 사용해 메모장에 저장된 명령을 GPT 채팅창에 복사 후 입력으로 주는 것 까지 구현하였습니다

다른 버그가 발생하거나 코드의 변경점이 있을 시 이 파일의 설명이 변경될 수 있는 점 숙지해주시길 바랍니다

본 코드에 대한 문의는 Issues나 icarlaboratory@gmail.com로 문의 바랍니다

[日本語バージョンはこちら](ReadMe_JPN.md) | [For English ReadMe Here](ReadMe_ENG.md) | [中文版本在这里](ReadMe_CHN.md)