import os
import glob
from inference_cli import synthesize
import re

ref_audio_language_list = [
    "中文",
    "英文",
    "日文",
    "粤语",
    "韩文",
    "中英混合",
    "日英混合",
    "粤英混合",
    "韩英混合",
    "多语种混合",
    "多语种混合(粤语)"
]

class AudioGenerate:
    def __init__(self):
        self.GPT_model_file = ''
        self.SoVITS_model_file = ''
        self.ref_audio_file = '../reference_audio/source_speaker.wav_0000021120_0000197120.wav'
        self.ref_audio_language = ''
        self.program_output_path = "../reference_audio/generated_audios_temp"
        self.speed = 1.0
        self.audio_file_path = ''
        self.is_completed = False
        self.audio_language_choice = "中文"

    def initialize(self):
        self.GPT_model_file = glob.glob(os.path.join("../GPT_weights_v2", f"*.ckpt"))
        if not self.GPT_model_file:
            raise FileNotFoundError(f"没有找到GPT模型文件(.ckpt)")
        self.GPT_model_file = max(self.GPT_model_file, key=os.path.getmtime)
        print(f"GPT模型文件: {self.GPT_model_file}")

        self.SoVITS_model_file = glob.glob(os.path.join("../SoVITS_weights_v2", f"*.pth"))
        if not self.SoVITS_model_file:
            raise FileNotFoundError(f"没有找到SoVITS模型文件(.pth)")
        self.SoVITS_model_file = max(self.SoVITS_model_file, key=os.path.getmtime)
        print(f"SoVITS模型文件: {self.SoVITS_model_file}")

        ref_audio_language_file = '../reference_audio/reference_audio_language.txt'
        with open(ref_audio_language_file, "r", encoding="utf-8") as f:
            try:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        self.ref_audio_language = ref_audio_language_list[int(line) - 1]
                        break
            except Exception:
                raise ValueError("参考音频的语言参数文件读取错误")
        print(f"推理参考音频的语言为：{self.ref_audio_language}")

    def audio_generator(self, text):
        self.is_completed = False

        if text == "不能送去合成":
            self.audio_file_path = '../reference_audio/silent_audio/silence.wav'
            self.is_completed = True
            return

        # 清理文本
        pattern = r'^[^A-Za-z0-9\u3040-\u30FF\u4E00-\u9FFF]+'    # 去除句首的所有标点
        text = re.sub(pattern, '', text)
        text = text.replace(' ', '')  # 空格替换为空
        text = text.replace('...', '，')

        # 生成音频
        self.audio_file_path = synthesize(
            GPT_model_path=self.GPT_model_file,
            SoVITS_model_path=self.SoVITS_model_file,
            ref_audio_path=self.ref_audio_file,
            ref_text_path='../reference_audio/reference_text.txt',  # 使用默认参考文本
            ref_language=self.ref_audio_language,
            target_text=text,
            target_language=self.audio_language_choice,
            output_path=self.program_output_path,
            speed=self.speed,
            how_to_cut='按中文句号。切'
        )
        # 检查音频文件是否生成成功
        if not self.audio_file_path or not os.path.exists(self.audio_file_path) or os.path.getsize(self.audio_file_path) == 0:
            print(f"[错误] 音频文件未生成或为空: {self.audio_file_path}")
            self.is_completed = False
        else:
            print(f"[成功] 音频文件已生成: {self.audio_file_path} 大小: {os.path.getsize(self.audio_file_path)} 字节")
            self.is_completed = True

if __name__ == "__main__":
    a = AudioGenerate()
    a.initialize()
    while True:
        text = input(">>>")
        if text == 'bye':
            break
        a.audio_generator(text)
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load(a.audio_file_path)
        pygame.mixer.music.play()
