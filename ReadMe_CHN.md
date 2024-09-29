本代码是顺天乡大学电子工学系所属的智能控制及机器人学研究室无人驾驶Mobility组制作的代码。

运行环境为 Python 3.11 版本/ROS2 Humble/虚拟化 Ubuntu 22.04 LTS

---

# 内置的软件包信息
## gpt_clip
复制gpt的全部回答后，将代码部分筛选出来保存到Documents文本文件的软件包
## gpt_node
gpt_node 软件包执行两个任务

i. 将gpt_clip软件包保存的文本文件进行软件包化构建后运行

ii. 在 gpt 中输入由 voice_recognition 包保存的文本文件
## voice_recognition
将语音识别命令保存为 recognized_text.txt 文件的软件包

## 工作原理
1. 使用语音识别向 Google 翻译器发出命令
2. 下达的命令将被保存为 txt 文件
3. txt 文件内翻译的指令将被复制到 Chat-gpt 的指令窗口
4. Chat-gpt 生成代码后将其保存为另一个 txt 文件
5. txt文件内的代码将被打包为Python代码
6. 包装好的代码会自动在ROS2上构建、运行，并移交到实际系统。

---

## 依赖性安装
#### 套餐
1. 收到本代码后将Voice_GPT_For_Ros2更改为[所需名称_ws]
2. 然后将 voice_gpt 文件夹更改为 src
3. 运行以下过程

##### 安装 pyaudio
    $pip install pyaudio
    $sudo apt-get install portaudio19-dev python3-pyaudio
    $pip install pyaudio

##### 安装 ALSA audio
    $sudo apt-get update
    $sudo apt-get install --reinstall alsa-base alsa-utils
    $sudo alsactl init

##### 确认安装
    $sudo apt-get install pulseaudio
    $pulseaudio --start

##### 安装 pyautogui
    $sudo apt update
    $sudo apt install python3 python3-pip
    $sudo apt install scrot python3-tk python3-dev
    $pip3 install pyautogui

##### speech recognition 설치
    $sudo apt update
    $pip3 install SpeechRecognition

##### 安装 watchdog
    $pip install watchdog

##### 安装 Flask
    $pip install Flask

##### 安装屏幕拍摄库
    $sudo apt-get install gnome-screenshot

4. 更改文件内部设置
~~~
gpt_cilp/gpt_cilp/gpt_clip_node.py
~~~
将第14、25、52行中的相应部分改为使用名称后使用
~~~
gpt_node/gpt_node/gpt_node.py
~~~
将第12、13、32、41、97行对应的部分改为使用名称，并输入以下命令。
~~~
voice_recognition/voice_recognition/voice_recog
~~~
将第29行对应的部分更改为使用的名称后使用。
## 执行
#### 过程
1. 运行终端并打开烧瓶服务器

禁用访问控制
~~~
$export DISPLAY=:0
$xhost +
~~~
此过程在 Ubuntu 会话结束时初始化， 因此每次运行前必须禁用访问控制
2. 然后通过以下过程运行烧瓶服务器。 
~~~
$export FLASK_APP=app.py
$export FLASK_ENV=development
$flask run --host=0.0.0.0 --port=5000
~~~

3. 运行 gpt_node

开发者评论:在直接生成软件包的过程中发生错误，通过修改空文本的方式将gpt_node软件包
实现了。 

因此，需要名为gpt_script的空包。 

如果发生没有发现文件的错误，请优先尝试删除gpt_script包后生成的方法。
~~~
$ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name {패키지_이름} {节点_名称}
~~~
执行命令是
~~~
$ros2 run gpt_node gpt_node
~~~
这样的话gpt_node会监视电脑的文件和gpt网站
4. 运行其他终端并执行以下过程

然后选择gpt网站的LIMO assistant打开聊天窗口，在终端上执行以下命令
~~~
$cd[工作区名称_ws]
$colcon build
$source install/setup.bash
$ros2 run[选择节点] [选择节点]
~~~
之后将语音命令对着麦克风说话的话，会被发布并保存在recognized_text.txt中。
正在监视的gpt_node感知到变化后，将其复制到gpt消息窗口， 并询问gpt
收到消息的gpt开始输出代码

*开发者评论:对麦克风说完话后，需要立即点击gpt窗口

5. 运行 gpt_ clip
~~~
$ros2 run gpt_clip gpt_clip
~~~
屏幕监视程序运行后，如果gpt全部输出，将复制代码保存为文本文件。

6. 之后由正在监视的gpt_node构建并自动运行。


# 短评
为了操作得相当简单，我写好了代码。
而且修改得也非常简单
如果想更改想要使用的语言，可以更改src/voice_recognition/voice_recognition/voice_recog.py的第75行language=''的国家代码。

以2024年9月24日为基准，已确认当前代码正常运行。
因为是完成版代码，在这里添加或修改功能没有任何问题。

还实现了使用Flask和Watchdog将存储在记事本上的命令复制到GPT聊天窗口后输入。

如果发生其他错误或代码有变更，该文件说明可能会发生变更，敬请熟知。

有关本代码的咨询请通过Issues或icarlaboratory@gmail.com 进行咨询。

[日本語バージョンはこちら](ReadMe_JPN.md) | [For English ReadMe Here](ReadMe_ENG.md) | [한국어는 이쪽](ReadMe.md)
