This code is written by the Autonomous Mobility Team of Intelligent Control and Robotics Laboratory, Department of Electronics, Sunhyang National University.

The working environment is Python 3.11 version / ROS2 Humble / Virtualization Ubuntu WSL2 and Ubuntu 22.04 LTS

---]

## How it works
1. give a command to Google Translator using voice recognition
2. the command is saved as a txt file
3. translated commands in the txt file are copied to Chat-gpt's command window
4. Chat-gpt generates the code, which is saved again in another txt file
5. the code in the txt file is packaged into Python code
6. the packaged code is automatically built, executed on ROS2, and transferred to the real system

---.

## Install dependencies
#### package
1. get this code and change Voice_GPT_For_Ros2 to [name of your choice_ws].
2. after that, change the voice_gpt folder to src
3. execute the following steps

##### install pyaudio
    $pip install pyaudio
    $sudo apt-get install portaudio19-dev python3-pyaudio
    $pip install pyaudio

##### Install ALSA audio
    $sudo apt-get update
    $sudo apt-get install --reinstall alsa-base alsa-utils
    $sudo alsactl init

Verify the installation of #####
    $sudo apt-get install pulseaudio
    $pulseaudio --start

## Run
#### Process
1. run a terminal and open a flask server

Disable access control
~~~Β
$export DISPLAY=:0
$xhost
~~~ $xhost
Note that this process is initialized when the Ubuntu session is terminated, so you need to disable access control before running it each time
2. and run the flask server through the process below 
~~~Β
export FLASK_APP=app.py
export FLASK_ENF=development
$flask run --host=0.0.0.0 --port=5000
~~~Β

3. launch another terminal and do the following

~~~Β
$cd [workspace name_ws]
$colcon build
$source install/setup.bash
$ros2 run [select node] [select node]
~~~]

# Comments.
I've written some terrible code to make it work fairly simply
It's also very easy to modify
If you want to change the language you want to use, just change the country code for language='' on line 75 of src/voice_gpt/voice_recognition/voice_recognition/voice_recog.py

This is not finished code at this time
We're currently working on implementing Principle #3 and will update as soon as possible.

Using Flask and Watchdog, I've implemented copying commands saved in notepad to the GPT chat window and giving them as input.

Please note that the description in this file may change if other bugs are found or changes are made to the code.

If you have any questions about this code, please contact Issues or icarlaboratory@gmail.com로

[日本語バージョンはこちら](ReadMe_JPN.md) | [For English ReadMe Here](ReadMe_ENG.md) | [中文版本在这里](ReadMe_CHN.md)