본 코드는 순천향대학교 전자공학과 소속 지능제어 및 로보틱스 연구실 자율주행 모빌리티 팀에서 작성된 코드입니다

작동 환경은 Python 3.11버전 / ROS2 Humble / 가상화 우분투 WSL2와 Ubuntu 22.04 LTS 입니다

---

# 내장된 패키지 정보
## gpt_clip
gpt의 대답 전체를 복사한 뒤 코드 부분을 추려 Documents에 텍스트 파일로 저장하는 패키지
## gpt_node
gpt_node 패키지는 두가지일을 수행합니다

i. gpt_clip 패키지가 저장한 텍스트 파일을 패키지화 시켜 빌드 후 실행

ii. voice_recognition 패키지가 저장한 텍스트 파일을 gpt에 입력
## voice_recognition
음성 인식을 통해 인식된 명령을 recognized_text.txt 파일로 저장하는 패키지

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

##### pyautogui 설치
    $sudo apt update
    $sudo apt install python3 python3-pip
    $sudo apt install scrot python3-tk python3-dev
    $pip3 install pyautogui

##### speech recognition 설치
    $sudo apt update
    $pip3 install SpeechRecognition

##### watchdog 설치
    $pip install watchdog

##### Flask 설치
    $pip install Flask

##### 화면 촬영 라이브러리 설치
    $sudo apt-get install gnome-screenshot

4. 파일 내부 설정 변경
~~~
gpt_cilp/gpt_cilp/gpt_clip_node.py
~~~
14, 25, 52번 줄에 해당하는 부분을 사용하는 이름으로 변경하여 사용
~~~
gpt_node/gpt_node/gpt_node.py
~~~
12, 13, 32, 41, 97번 줄 에 해당하는 부분을 사용하는 이름으로 변경하고 이하의 명령을 입력합니다
~~~
voice_recognition/voice_recognition/voice_recog
~~~
29번 줄 에 해당하는 부분을 사용하는 이름으로 변경하여 사용합니다
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

3. gpt_node를 실행합니다

개발자 코멘트 : 패키지를 직접 생성하는 과정에서 오류가 발생하여 비어있는 텍스트를 수정하는 방식으로 gpt_node패키지를
구현하였습니다. 

하여, gpt_script라는 비어있는 패키지가 필요합니다. 

파일을 발견하지 못하였다는 오류가 발생하였을 시 gpt_script 패키지를 삭제한 뒤 생성하는 방법을 우선적으로 시도해보시길 바랍니다.
~~~
$ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name {패키지_이름} {노드_이름}
~~~
실행 명령은
~~~
$ros2 run gpt_node gpt_node
~~~
이제 gpt_node가 컴퓨터의 파일과 gpt 사이트를 감시하게 됩니다

4. 다른 터미널을 실행하고 다음의 과정을 진행합니다

그 다음 gpt 사이트의 LIMO assistant를 선택해 채팅창을 열고 터미널에서 이하의 명령을 실행합니다
~~~
$cd [워크스페이스 이름_ws]
$colcon build
$source install/setup.bash
$ros2 run [선택 노드] [선택 노드]
~~~
이후 음성명령을 마이크에 대고 이야기하면 퍼블리싱되어 recognized_text.txt에 저장됩니다
감시 중이던 gpt_node가 변화를 감지하고 gpt 메세지 창에 이를 복사하고 gpt에 물어보게 됩니다
메세지를 입력받은 gpt가 코드를 출력하기 시작합니다

*개발자 코멘트 : 마이크에 말을 한 후 바로 gpt창을 클릭해주어야 합니다

5. gpt_clip을 실행합니다
~~~
$ros2 run gpt_clip gpt_clip
~~~
화면 감시 프로그램이 실행되면서 gpt가 전부 출력 되면 코드를 복사하여 텍스트 파일로 저장합니다

6. 이후 감시 중이던 gpt_node가 빌드하여 자동으로 실행됩니다


# 코멘트
상당히 간단하게 작동하게 끔 코드를 작성해 두었습니다
또한 수정 역시 굉장히 간단하게 되어 있습니다
사용하고 싶은 언어를 변경하고 싶다면 src/voice_recognition/voice_recognition/voice_recog.py의 75번 째 줄의 language=''의 국가코드를 변경하면됩니다

2024년 9월 24일 기준 현재 코드는 정상적으로 동작함을 확인했습니다
완성본 코드이니 여기서 기능을 추가하거나 수정하는 데에 아무런 문제가 없습니다

Flask과 Watchdog을 사용해 메모장에 저장된 명령을 GPT 채팅창에 복사 후 입력으로 주는 것 까지 구현하였습니다

다른 버그가 발생하거나 코드의 변경점이 있을 시 이 파일의 설명이 변경될 수 있는 점 숙지해주시길 바랍니다

본 코드에 대한 문의는 Issues나 icarlaboratory@gmail.com로 문의 바랍니다

[日本語バージョンはこちら](ReadMe_JPN.md) | [For English ReadMe Here](ReadMe_ENG.md) | [中文版本在这里](ReadMe_CHN.md)
