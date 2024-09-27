本代码由国立顺天乡大学电子系智能控制与机器人实验室自主移动小组编写。

工作环境为 Python 3.11 版本/ROS2 Humble/虚拟化 Ubuntu WSL2 和 Ubuntu 22.04 LTS。

---]

## 工作原理
1. 使用语音识别向谷歌翻译器发出命令
2. 将命令保存为 txt 文件
3. 将 txt 文件中翻译好的命令复制到 Chat-gpt 的命令窗口中
4. Chat-gpt 生成代码，并保存到另一个 txt 文件中
5. 将 txt 文件中的代码打包成 Python 代码
6. 打包后的代码在 ROS2 上自动构建和执行，然后传输到实际系统。

---...

## 安装依赖项
#### 软件包
1. 获取此代码并将 Voice_GPT_For_Ros2 更改为 [desired name_ws]。
然后，将 voice_gpt 文件夹更改为 src 文件夹。
3. 执行以下步骤

##### 安装 pyaudio
    $pip install pyaudio
    $sudo apt-get install portaudio19-dev python3-pyaudio
    $pip install pyaudio

##### 安装 ALSA 音频
    $sudo apt-get update
    $sudo apt-get install --reinstall alsa-base alsa-utils
    $sudo alsactl init

验证 ##### 的安装
    $sudo apt-get install pulseaudio
    启动

## 运行
#### 进程
运行终端并打开 flask 服务器

禁用访问控制
~~~Β
$export DISPLAY=:0
$xhost
~~~$xhost
注意，当 Ubuntu 会话结束时，该进程将被重置，因此每次运行前都必须禁用访问控制。
2. 通过下面的过程运行 flask 服务器 
~~~Β
export FLASK_APP=app.py
export FLASK_ENF=development
$flask run --host=0.0.0.0 --port=5000
~~~Β

3. 启动另一个终端，执行以下操作

~~~Β
$cd [工作区名称_ws］
$colcon build
$source install/setup.bash
$ros2 运行 [选择节点] [选择节点］
~~~]

# 注释。
我写了一些可怕的代码，使其工作起来相当简单
修改也很容易
如果你想更改要使用的语言，只需更改 src/voice_gpt/voice_recognition/voice_recognition/voice_recog.py 第 75 行 language='' 的国家代码即可。

此代码尚未完成
我们目前正在实施原则 3，并将尽快更新。

我使用 Flask 和看门狗实现了将保存在记事本中的命令复制到 GPT 聊天窗口并将其作为输入。

请注意，如果发现其他错误或对代码进行了修改，本文件中的描述可能会有所改变。

如果您对此代码有任何疑问，请联系 Issues 或 icarlaboratory@gmail.com로。

[日本語バージョンはこちら](ReadMe_JPN.md) | [英文版本在這裡](ReadMe_ENG.md) | [中文版本在這裡](ReadMe_CHN.md)