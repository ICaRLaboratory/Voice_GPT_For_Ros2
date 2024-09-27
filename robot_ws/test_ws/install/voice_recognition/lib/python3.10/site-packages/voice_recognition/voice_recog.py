import speech_recognition as sr
import datetime
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Bool
import pyautogui
import pyperclip
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time  # time 모듈 추가

class FileHandler(FileSystemEventHandler):
    # 파일이 수정되었을 때 호출되는 함수
    def on_modified(self, event):
        if event.src_path == "recognized_text.txt":
            # 텍스트 파일에서 마지막 줄을 읽어온다
            with open(event.src_path, 'r') as file:
                lines = file.readlines()
                last_line = lines[-1].strip() if lines else ""
                # 마지막 줄이 존재하면 클립보드에 복사하는 함수 호출
                if last_line:
                    self.copy_paste(last_line)

    # 텍스트를 클립보드에 복사하고 붙여넣기하는 함수
    def copy_paste(self, text):
        time.sleep(3)  # time 모듈 사용
        image_path = '/home/qwert/test_ws/src/voice_recognition/voice_recognition/images/scaning.png'
        # 명령 프롬프트 버튼의 위치를 화면에서 찾는다
        try:
            button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if button_location:
                print("버튼이 발견되었습니다:", button_location)
                pyautogui.click(pyautogui.center(button_location))
                try:
                    # 텍스트를 클립보드에 복사
                    pyperclip.copy(text)
                    # 클립보드의 내용을 붙여넣고 엔터를 누른다
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.press('enter')
                except Exception as e:
                    print(f"복사 또는 붙여넣기 실패: {str(e)}")
            else:
                print("명령 프롬프트 버튼을 찾을 수 없습니다.")
        except Exception as e:
            print(f"오류 발생: {str(e)}")

class VoiceRecognition(Node):
    def __init__(self):
        super().__init__('voice_recognition')
        self.publisher_ = self.create_publisher(String, 'voice_commands', 10)
        self.subscription = self.create_subscription(
            Bool,
            'activation',
            self.activation_callback, 10)
        self.listen = True
        self.setup_file_observer()
        self.start_listening()

    # 파일 변경 감시 설정
    def setup_file_observer(self):
        self.observer = Observer()
        event_handler = FileHandler()
        self.observer.schedule(event_handler, os.path.dirname(os.path.abspath(__file__)), recursive=False)
        self.observer.start()

    # 음성 인식 활성화 콜백 함수
    def activation_callback(self, msg):
        self.listen = msg.data
        if self.listen:
            self.get_logger().info('음성 인식을 다시 시작합니다.')
            self.start_listening()
        else:
            self.get_logger().info('음성 인식을 중지합니다.')

    # 음성 명령을 발행하는 함수
    def publish_message(self, message):
        msg = String()
        msg.data = message.lower()
        self.publisher_.publish(msg)
        self.get_logger().info(f'발행 중: "{msg.data}"')

    # 인식된 텍스트를 파일에 저장하는 함수
    def save_to_txt(self, text):
        #timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_text = f"{text}\n"
        with open('recognized_text.txt', 'a', encoding='utf-8') as file:
            file.write(formatted_text)
        self.get_logger().info('인식된 텍스트를 파일에 저장했습니다.')

    # 음성 명령을 인식하는 함수
    def take_command(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            self.get_logger().info('음성을 듣고 있습니다...')
            audio = r.listen(source)
            if self.listen:
                try:
                    value = r.recognize_google(audio, language='en')
                    self.get_logger().info(f"인식된 내용: {value}")
                    self.save_to_txt(value)
                    self.publish_message(value)
                    return value
                except sr.UnknownValueError:
                    self.get_logger().info("알아듣지 못했습니다.")
                except sr.RequestError as e:
                    self.get_logger().info(f"결과를 요청할 수 없습니다: {str(e)}")
                return None

    # 음성 인식을 시작하는 함수
    def start_listening(self):
        while self.listen:
            message = self.take_command()
            if message:
                self.listen = False  # 계속해서 듣는 것을 방지

def main(args=None):
    rclpy.init(args=args)
    voice_recog = VoiceRecognition()
    try:
        rclpy.spin(voice_recog)
    except KeyboardInterrupt:
        voice_recog.observer.stop()
    finally:
        voice_recog.observer.join()
        voice_recog.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

