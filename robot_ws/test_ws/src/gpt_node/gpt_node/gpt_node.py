import time
import pyautogui
import shutil
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class UnifiedFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # 감시할 파일 경로 설정
        recognized_text_file = "/home/qwert/test_ws/recognized_text.txt"
        extracted_code_file = "/home/qwert/Documents/extracted_code.txt"

        # 'recognized_text.txt' 파일이 변경되었을 때 실행
        if event.src_path == recognized_text_file:
            print(f"{recognized_text_file} 파일 변경 감지.")
            with open(recognized_text_file, 'r') as file:
                lines = file.readlines()
                last_line = lines[-1].strip() if lines else ""
                
                if last_line:
                    # 마지막 줄의 텍스트를 읽고 이미지를 클릭하여 텍스트 입력
                    #last_line_split = last_line.split("-")[3]
                    self.click_image_and_type(last_line)

        # 'extracted_code.txt' 파일이 변경되었을 때 실행
        elif event.src_path == extracted_code_file:
            print(f"{extracted_code_file} 파일 변경 감지.")
            base_dir = os.path.expanduser('~')
            source_file = os.path.join(base_dir, 'Documents', 'extracted_code.txt')
            target_file = os.path.join(base_dir, 'test_ws', 'src', 'gpt_script', 'gpt_script', 'gpt_script.py')
            replace_file_contents(source_file, target_file)
            package_name = 'gpt_script'
            build_package(package_name)
            node_executable = 'gpt_script'
            run_node(package_name, node_executable)

    def click_image_and_type(self, text):
        # 이미지 경로 설정
        image_path = '/home/qwert/test_ws/src/voice_recognition/voice_recognition/images/scaning.png'

        # 이미지가 화면에 있는지 확인하고 클릭
        try:
            button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if button_location:
                print("이미지 위치를 찾았습니다:", button_location)
                pyautogui.click(pyautogui.center(button_location))  # 이미지 중앙 클릭
                time.sleep(1)  # 대기 시간 (필요에 따라 조정 가능)

                # 텍스트를 그대로 입력
                pyautogui.write(text)
                pyautogui.press('enter')
                print(f"텍스트 '{text}'를 입력하고 엔터 완료")
            else:
                print("이미지를 찾을 수 없습니다.")
        except Exception as e:
            print(f"이미지 클릭 실패 또는 오류 발생: {str(e)}")

def replace_file_contents(source_file, target_file):
    try:
        # 소스 파일에서 내용 읽기
        with open(source_file, 'r') as file:
            content = file.read()

        # 타겟 파일에 내용 쓰기 (기존 내용 대체)
        with open(target_file, 'w') as file:
            file.write(content)

        print("파일 내용이 성공적으로 업데이트되었습니다.")
    except Exception as e:
        print(f"파일 내용 업데이트 중 오류 발생: {e}")

def build_package(package_name):
    try:
        # 패키지 빌드 명령어 실행
        print(f"ROS 2 패키지 빌드 중: {package_name}")
        subprocess.run(['colcon', 'build', '--packages-select', package_name], check=True)
        print(f"패키지 {package_name} 빌드 성공.")
    except subprocess.CalledProcessError:
        print(f"패키지 빌드 실패: {package_name}")
        return False
    return True

def run_node(package_name, node_executable):
    try:
        # 노드 실행 명령어
        print(f"패키지 '{package_name}'의 노드 '{node_executable}' 실행 중")
        subprocess.run(['ros2', 'run', package_name, node_executable], check=True)
    except subprocess.CalledProcessError:
        print(f"노드 실행 실패: {node_executable}")
        return False
    return True

def main():
    # 감시할 두 디렉터리 설정
    watch_directories = ["/home/qwert/test_ws/", "/home/qwert/Documents"]
    
    # 이벤트 핸들러와 옵저버 설정
    event_handler = UnifiedFileHandler()
    observer = Observer()

    # 옵저버가 각 디렉터리를 감시하도록 설정
    for directory in watch_directories:
        observer.schedule(event_handler, directory, recursive=False)

    # 옵저버 시작
    observer.start()

    try:
        # 프로그램이 종료되지 않도록 유지
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("감시 중지 중...")
        observer.stop()

    observer.join()
    print("프로그램 종료.")

if __name__ == "__main__":
    main()

