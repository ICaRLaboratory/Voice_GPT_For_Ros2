本コードは順天郷大学電子工学科所属の知能制御およびロボティクス研究室自動運転モビリティチームで作成されたコードです

作動環境はPython 3.11バージョン / ROS2 Humble / 仮想化ウブンツWSL2とUbuntu 22.04LTSです

---

# 内蔵されたパッケージ情報です
## gpt_clip
gptの返事全体をコピーした後、コード部分を選んでDocumentsにテキストファイルとして保存するパッケージ
## gpt_node
gpt_nodeパッケージは二つのことを遂行します

i. gpt_clipパッケージが保存したテキストファイルをパッケージ化してビルド後に実行

ii. voice_recognitionパッケージが保存したテキストファイルをgptに入力します
## voice_recognition
音声認識によって認識された命令をrecognized_text.txtファイルとして保存するパッケージ

## 作動原理
1. 音声認識を使用してGoogle翻訳機で命令を下します
2. 下された命令がtxtファイルとして保存されます
3. txt ファイル内の翻訳されたコマンドが Chat-gpt のコマンドウィンドウにコピーされます
4. Chat-gptがコードを生成すると、これをまた別のtxtファイルとして保存されます
5. txtファイル内のコードがPythonコードにパッケージングされます
6. パッケージングされたコードが自動的にROS2でビルド、実行され、実際のシステムに引き渡されます

---

## 依存性のインストールです
#### パッケージです
1. 本コードを受信し、Voice_GPT_For_Ros2 を [希望する名前_ws] に変更します
2. その後、voice_gptフォルダをsrcに変更します
3. 以下の手順を実行します

##### pyaudioのインストールです
    $pip install pyaudio
    $sudo apt-get install portaudio19-dev python3-pyaudio
    $pip install pyaudio

##### ALSA audioのインストールです
    $sudo apt-get update
    $sudo apt-get install --reinstall alsa-base alsa-utils
    $sudo alsactl init

##### インストールの確認です
    $sudo apt-get install pulseaudio
    $pulseaudio --start

##### pyautoguiをインストールします
    $sudo apt update
    $sudo apt install python3 python3-pip
    $sudo apt install scrot python3-tk python3-dev
    $pip3 install pyautogui

##### speech recognition 설치
    $sudo apt update
    $pip3 install SpeechRecognition

##### watchdogのインストールです
    $pip install watchdog

##### Flaskをインストールします
    $pip install Flask

##### 画面撮影ライブラリのインストールです
    $sudo apt-get install gnome-screenshot

4. ファイルの内部設定を変更します
~~~
gpt_cilp/gpt_cilp/gpt_clip_node.py
~~~
14、25、52番の行に該当する部分を使用する名前に変更して使用します
~~~
gpt_node/gpt_node/gpt_node.py
~~~
12、13、32、41、97 行に該当する部分を使用する名前に変更し、以下のコマンドを入力します
~~~
voice_recognition/voice_recognition/voice_recog
~~~
29番線に該当する部分を使用する名前に変更して使用します
## 実行します
#### 過程
1. ターミナルを実行し、フラスコ サーバーを解放します

アクセス制御を無効にします
~~~
$export DISPLAY=:0
$xhost +
~~~
このプロセスは、Ubuntuセッションが終了すると初期化されるため、毎回実行前のアクセス制御を無効にする必要があります

2. そして、以下のプロセスを通じてフラスコサーバーを実行します 
~~~
$export FLASK_APP=app.py
$export FLASK_ENV=development
$flask run --host=0.0.0.0 --port=5000
~~~

3. gpt_nodeを実行します

開発者コメント:パッケージを直接生成する過程でエラーが発生し、空いているテキストを修正する方式でgpt_nodeパッケージを
実装しました。 

して、gpt_scriptという空のパッケージが必要です。 

ファイルが見つからないというエラーが発生した場合は、gpt_scriptパッケージを削除してから生成する方法をまず試してみてください。
~~~
$ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name {패키지_이름} {ノード_名前}
~~~
実行命令は
~~~
$ros2 run gpt_node gpt_node
~~~
こうなるとgpt_nodeがパソコンのファイルとgptサイトを監視するようになります

4. 別のターミナルを実行し、次の手順に進みます

次に、gptサイトのLIMO assistantを選択してチャットウィンドウを開き、ターミナルで以下の命令を実行します
~~~
$cd [ワークスペース名_ws]
$colcon build
$source install/setup.bash
$ros2 run [選択ノード] [選択ノード]
~~~
その後、音声命令をマイクに当てて話すと、パブリッシングされてrecognized_text.txtに保存されます
監視中のgpt_nodeが変化を感知し、gptメッセージウィンドウにこれをコピーしてgptに尋ねるようになります
メッセージを入力されたgptがコードを出力し始めます

*開発者コメント:マイクに話した後、すぐにgptウィンドウをクリックする必要があります

5. gpt_clipを実行します
~~~
$ros2 run gpt_clip gpt_clip
~~~
画面監視プログラムが実行され、gptがすべて出力されると、コードをコピーしてテキストファイルとして保存します

6. その後、監視中だったgpt_nodeがビルドして自動的に実行されます


# コメントです
かなり簡単に動作するようにコードを作成しておきました
また修正もとても簡単になっています
使用したい言語を変更したい場合はsrc/voice_recognition/voice_recognition/voice_recog.pyの75番目の行のlanguage='の国家コードを変更すればいいです

2024年9月24日現在のコードは正常に動作することを確認しました
完成本コードなので、ここで機能の追加·修正に何の問題もありません

FlaskとWatchdogを使ってメモ帳に保存された命令をGPTチャットウィンドウにコピー後、入力として与えることまで具現しました

他のバグが発生したり、コードの変更点がある場合はこのファイルの説明が変更になることがありますのでご了承願います

本コードについてのお問い合わせは、Issuesか icarlaboratory@gmail.com までお願いします

[한국어는 이쪽](ReadMe.md) | [For English ReadMe Here](ReadMe_ENG.md) | [中文版本在这里](ReadMe_CHN.md)
