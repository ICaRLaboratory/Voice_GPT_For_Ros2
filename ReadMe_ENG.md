This code was written by the Autonomous Driving Mobility Team of the Intelligence Control and Robotics Laboratory of Soonchunhyang University's Department of Electronic Engineering

The operating environment is Python 3.11 version / ROS2 Humble / Virtualization Ubuntu WSL2 and Ubuntu 22.04 LTS

---

# Embedded Package Information
## gpt_clip
A package that copies the entire gpt answer and then selects the code part and stores it as a text file in Documents
## gpt_node
The gpt_node package does two things

i. Package the text file stored by the gpt_clip package, build it, and run it

ii. Enter the text file saved by the voice_recognition package into the gpt
## voice_recognition
A package that stores commands recognized through speech recognition as a recognized_text.txt file

## principle of operation
1. Use speech recognition to command Google Translator
2. The command is saved as a txt file
3. The translated commands in the txt file are copied to the command window in Chat-gpt
4. When Chat-gpt generates the code, it is saved back to another txt file
5. The code in the txt file is packaged in Python code
6. Packaged code is automatically built and executed in ROS2 and handed over to the physical system

---

## Dependency installation
#### package
1. Receive this code and change Voice_GPT_For_Ros2 to [Desired Name_ws]
2. Subsequently, change the voice_gpt folder to src
3. Follow these steps

##### install pyaudio
    $pip install pyaudio
    $sudo apt-get install portaudio19-dev python3-pyaudio
    $pip install pyaudio

##### Install ALSA audio
    $sudo apt-get update
    $sudo apt-get install --reinstall alsa-base alsa-utils
    $sudo alsactl init

##### Confirmation of installation
    $sudo apt-get install pulseaudio
    $pulseaudio --start

##### install pyautogui
    $sudo apt update
    $sudo apt install python3 python3-pip
    $sudo apt install scrot python3-tk python3-dev
    $pip3 install pyautogui

##### speech recognition 설치
    $sudo apt update
    $pip3 install SpeechRecognition

##### Install watchdog
    $pip install watchdog

##### Install Flask
    $pip install Flask

##### Installing the Screen Shooting Library
    $sudo apt-get install gnome-screenshot

4. Change file internal settings
~~~
gpt_cilp/gpt_cilp/gpt_clip_node.py
~~~
Use lines 14, 25 and 52 by changing them to their names
~~~
gpt_node/gpt_node/gpt_node.py
~~~
Change the part corresponding to lines 12, 13, 32, 41, and 97 to the name you use and enter the following command
~~~
voice_recognition/voice_recognition/voice_recog
~~~
Change the part corresponding to line 29 to the name you use
## Execute
#### Process
1. Run the terminal and open the flask server

Disabling Access Control
~~~
$export DISPLAY=:0
$xhost +
~~~
This process is initialized at the end of the Ubuntu session, so you must disable access control before each run

2. And run the flask server through the following process 
~~~
$export FLASK_APP=app.py
$export FLASK_ENV=development
$flask run --host=0.0.0.0 --port=5000
~~~

3. Run gpt_node

Developer Comment: An error occurred in the process of creating the package directly, and the gpt_node package is modified by correcting the empty text
It's been implemented. 

Therefore, an empty package called gpt_script is required. 

If an error occurs that the file was not found, please try to delete the gpt_script package and create it first.
~~~
$ros2 pkg create --build-type agent_python --license Apache-2.0 --node-name {package_name} {node_name}
~~~
The execution command is
~~~
$ros2 run gpt_node gpt_node
~~~
This will now allow gpt_node to monitor files and gpt sites on your computer

4. Run a different terminal and proceed with the following process

Then, select LIMO assistant on the gpt site to open the chat window and execute the following command from the terminal
~~~
$cd [Workspace Name_ws]
$colcon build
$source install/setup.bash
$ros2 run [Select Node] [Select Node]
~~~
If you then speak to the microphone, it will be published and saved in the recognized_text.txt
The gpt_node being monitored detects the change, copies it to the gpt message window, and asks the gpt
After receiving the message, the gpt starts to output the code

*Developer Comment: You should click on the gpt window immediately after speaking to the microphone

5. Run gpt_clip
~~~
$ros2 run gpt_clip gpt_clip
~~~
When the screen monitoring program is running and all gpts are output, copy the code and save it as a text file

6. After that, the gpt_node that was being monitored builds and runs automatically


# Comments
I've written a code to make it work fairly simply
It's also very simple to fix
If you want to change the language you want to use, you can change the country code for language=" on line 75 of src/voice_recognition/voice_recognition/voice_recognition.py

As of September 24, 2024, the current code has been confirmed to operate normally
It's a complete code, so there's no problem adding or modifying the function here

Using Flask and Watchdog, commands stored in the memo are copied to the GPT chat window and given as input

Please be aware that the description of this file may change if other bugs occur or if there is a change in the code

If you have any questions about this code, please contact Issues or icarlaboratory@gmail.com

[日本語バージョンはこちら](ReadMe_JPN.md) | [한국어는 이쪽](ReadMe.md) | [中文版本在这里](ReadMe_CHN.md)
