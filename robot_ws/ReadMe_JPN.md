本コードは順天郷大学電子工学科所属知能制御及びロボット工学研究室自律走行モビリティチームで作成されたコードです。

動作環境はPython 3.11バージョン / ROS2 Humble / 仮想化Ubuntu WSL2とUbuntu 22.04 LTSです。

---動作原理

## 動作原理
1.音声認識を使用してGoogle翻訳でコマンドを入力します。
2.翻訳されたコマンドがtxtファイルとして保存されます。
3. txtファイル内の翻訳されたコマンドがChat-gptのコマンドウィンドウにコピーされます。
4.Chat-gptがコードを生成すると、これを再び別のtxtファイルに保存されます。
5.txtファイル内のコードがPythonコードにパッケージ化されます。
6.パッケージ化されたコードが自動的にROS2でビルド、実行され、実際のシステムに渡されます。

---パッケージ化されたコードは

## 依存関係のインストール
#### パッケージ
1.本コードを受け取り、Voice_GPT_For_Ros2を[任意の名前_ws]に変更します。
2.その後、voice_gptフォルダをsrcに変更します。
3.以下のプロセスを実行します。

##### pyaudioのインストール
    pip install pyaudio
    sudo apt-get install portaudio19-dev python3-pyaudio
    pip install pyaudio

##### ALSA audioインストール
    sudo apt-get update
    sudo apt-get install --reinstall alsa-base alsa-utils
    sudo alsactl init

##### インストール確認
    $sudo apt-get install pulseaudio
    pulseaudio --start

## 実行
#### プロセス
1.ターミナルを実行してフラスコサーバーを開きます。

アクセス制御無効化
~~~を実行します。
export DISPLAY=:0
$xhost + +~~ ~~~ $xhost
~~~ ~~~~ 了解
このプロセスはUbuntuセッションが終了される場合初期化されるので、毎回実行する前にアクセス制御を無効にする必要があります。
2.そして、下記のプロセスでフラスコサーバーを実行します。
~~~ ~~~~ $xhost
$export FLASK_APP=app.py
export $export FLASK_ENF=development
flask run --host=0.0.0.0.0 --port=5000
~~～～～～っと

3.他のターミナルを実行して次のプロセスを進めます。


cd [ワークスペース名_ws] $cd
colcon build
$source install/setup.bash
ros2 run [選択ノード] [選択ノード] $ros2 run
~~~ ~~~~ 了解

# コメント
かなり簡単に動作するようにコードを書いておきました。
また、修正もすごく簡単になっています。
使いたい言語を変更したい場合はsrc/voice_gpt/voice_recognition/voice_recognition/voice_recog.pyの75行目のlanguage=''の国コードを変更するだけです。

現在は完成したコードではありません
動作原理3を現在実装中で、近日中にアップデートする予定です。

FlaskとWatchdogを使ってメモ帳に保存されたコマンドをGPTチャットウィンドウにコピーして入力することまで実装しました。

他のバグが発生したり、コードの変更点がある場合、このファイルの説明が変更される可能性があることをご了承ください。

本コードに関するお問い合わせはIssuesやicarlaboratory@gmail.com로 までご連絡ください。

[日本語バージョンはこちら](ReadMe_JPN.md) | [For English ReadMe Here](ReadMe_ENG.md) | [中文版本在这里](ReadMe_CHN.md)