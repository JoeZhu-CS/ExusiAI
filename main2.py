import os, sys
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from queue import Queue
import threading
import time
import re
import pygame

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont, QFontDatabase

import dp_local2
import audio_generator
import qtUI

# 模块间传参队列
text_queue = Queue()
audio_file_path_queue = Queue()
is_audio_play_complete = Queue()
is_text_generating_queue = Queue()
dp2qt_queue = Queue()
qt2dp_queue = Queue()
QT_message_queue = Queue()

dp_chat = dp_local2.DSLocalAndVoiceGen()
audio_gen = audio_generator.AudioGenerate()
audio_gen.initialize()

os.system('cls')
print("语音助手程序已启动...")

def main_thread():
    while True:
        time.sleep(1)
        if not text_queue.empty():
            this_turn_response = text_queue.get()
            if this_turn_response == 'bye':
                dp2qt_queue.put("（再见）")
                QT_message_queue.put('bye')
                break

            this_turn_response = this_turn_response + '。'  # 确保每句话都有句号
            this_turn_response = re.findall(r'.+?。', this_turn_response)
            QT_message_queue.put("正在生成语音...")

            for i in range(0, len(this_turn_response), 2):
                group = this_turn_response[i:i+2]  # 一次合成两句话
                output_for_audio = "".join(group)
                cleaned_text = re.sub(r"（.*?）", "", output_for_audio)
                cleaned_text = re.sub(r"\(.*?\)", "", cleaned_text)  # 删除括号内的内容
                
                if bool(re.fullmatch(r'[\W_]+', cleaned_text.strip())):  # 若只包括符号
                    cleaned_text = '。'
                if cleaned_text == '。':
                    cleaned_text = '不能送去合成'

                audio_generate_count = 1
                while audio_generate_count <= 3:  # 语音合成异常处理
                    try:
                        audio_gen.audio_generator(cleaned_text)
                        break
                    except Exception as e:
                        QT_message_queue.put("语音合成出错，重试中")
                        audio_generate_count += 1
                        time.sleep(1)
                        QT_message_queue.put(f"语音合成错误信息： {str(e)}")
                else:
                    QT_message_queue.put("语音合成失败")
                    dp2qt_queue.put(output_for_audio)
                    is_text_generating_queue.get()
                    break

                audio_file_path_queue.put(audio_gen.audio_file_path)
                # 自动播放音频
                audio_path = audio_gen.audio_file_path
                if os.path.exists(audio_path):
                    try:
                        pygame.mixer.init()
                        pygame.mixer.music.load(audio_path)
                        pygame.mixer.music.play()
                        print(f"[提示] 正在播放音频：{audio_path}")
                        while pygame.mixer.music.get_busy():
                            time.sleep(0.1)
                    except Exception as e:
                        print(f"[错误] 音频播放失败: {e}")
                else:
                    print(f"[警告] 未找到音频文件：{audio_path}")
                if i == 0:
                    is_text_generating_queue.get()  # 让模型停止思考
                dp2qt_queue.put(output_for_audio)

            is_audio_play_complete.put('yes')  # 不让LLM模块提前进入下一个循环

qt_app = QApplication(sys.argv)
qt_win = qtUI.ChatGUI(
    dp2qt_queue=dp2qt_queue,
    qt2dp_queue=qt2dp_queue,
    QT_message_queue=QT_message_queue
)

# 设置字体
font_id = QFontDatabase.addApplicationFont("../font/ft.ttf")
font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
font = QFont(font_family, 12)
qt_app.setFont(font)

# 设置qt窗口位置
from PyQt5.QtWidgets import QDesktopWidget
screen_w_mid = int(0.5 * QDesktopWidget().screenGeometry().width())
screen_h_mid = int(0.5 * QDesktopWidget().screenGeometry().height())
qt_win.move(screen_w_mid, int(screen_h_mid - 0.35 * QDesktopWidget().screenGeometry().height()))

# 启动线程
tr2 = threading.Thread(target=dp_chat.text_generator, args=(text_queue, is_audio_play_complete, is_text_generating_queue, dp2qt_queue, qt2dp_queue, QT_message_queue))
tr3 = threading.Thread(target=main_thread)
tr2.start()
tr3.start()

qt_win.show()
qt_app.exec_()

# 清理音频缓存
folder_path = '../reference_audio/generated_audios_temp'
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
