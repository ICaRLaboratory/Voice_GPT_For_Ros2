import rclpy
from rclpy.node import Node
import pyautogui
import pyperclip
import time

class GPTClipNode(Node):
    def __init__(self):
        super().__init__('gpt_clip')
        self.timer = self.create_timer(10, self.find_and_click_image)  # 10초마다 이미지 찾아 클릭하고 텍스트 추출

    def find_and_click_image(self):
        time.sleep(5)  # 웹 페이지가 로드되고 이미지가 화면에 나타날 시간을 줍니다.
        image_path = '/home/qwert/test_ws/src/gpt_clip/resource/copy_img.png'  # 찾고자 하는 이미지 파일의 경로

        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)  # 화면에서 이미지 위치 찾기

            if location:
                pyautogui.click(location)  # 이미지 중앙 위치를 기준으로 마우스 클릭
                self.get_logger().info(f"Image found and clicked at {location}")
                time.sleep(1)  # 잠시 대기하여 클립보드 내용이 업데이트 되도록 함

                copied_text = pyperclip.paste()  # 클립보드에서 텍스트 가져오기
                file_path = '/home/qwert/Documents/output.txt'  # 저장할 텍스트 파일의 경로 지정

                with open(file_path, 'w') as f:
                    f.write(copied_text)
                self.get_logger().info(f"Copied text saved to {file_path}")

                # 저장된 텍스트 파일에서 '```python'부터 '```'까지의 코드 추출
                with open(file_path, 'r') as f:
                    lines = f.readlines()

                start_tag = '```python'
                end_tag = '```'
                code_lines = []
                capture = False

                for line in lines:
                    if start_tag in line:
                        capture = True  # 코드 블록 추출 시작
                        continue
                    elif end_tag in line and capture:
                        capture = False  # 코드 블록 추출 종료
                        continue
                    elif capture:
                        code_lines.append(line)  # 코드 라인 추가

                if code_lines:
                    # 코드 부분만을 포함하는 새로운 파일 경로
                    code_file_path = '/home/qwert/Documents/extracted_code.txt'

                    with open(code_file_path, 'w') as f:
                        f.writelines(code_lines)
                    self.get_logger().info(f"Code block extracted and saved to {code_file_path}")
                else:
                    self.get_logger().info("No code block found within the specified tags.")

        except pyautogui.ImageNotFoundException:
            self.get_logger().info("Image not found on screen. Will try again.")

def main(args=None):
    rclpy.init(args=args)
    node = GPTClipNode()
    try:
        rclpy.spin(node)  # 노드 실행, 이벤트 처리 시작
    except KeyboardInterrupt:
        # 사용자 인터럽트 처리 (Ctrl+C)
        node.get_logger().info('Node interrupted by user.')
    finally:
        # 노드 종료 전 정리 작업
        rclpy.shutdown()

if __name__ == '__main__':
    main()
