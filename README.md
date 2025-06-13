# ExusiAI - AI Digital Character Project

## 项目简介 / Project Introduction

ExusiAI 是一个基于 [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) 音色提取合成项目和 DeepSeek API 的 AI 数字人项目。本项目以游戏《明日方舟》中的角色"能天使"（Exusiai）为原型，通过提取游戏中的角色语音和剧情文本，构建了一个具有独特个性的 AI 数字角色。项目集成了大语言模型（LLM）对话、语音合成、音色迁移等功能，支持多语言（中英、日英等）文本到语音的自然流畅转换，并提供美观易用的桌面图形界面。

未来计划推出用户自定义 AI 虚拟角色的功能，让用户能够创建属于自己的数字角色。

ExusiAI is an AI Digital Character Project based on [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) timbre extraction & synthesis and DeepSeek API. This project takes "Exusiai" from the game "Arknights" as its prototype, creating an AI digital character with unique personality by extracting character voice lines and story texts from the game. It integrates LLM dialogue, voice synthesis, timbre transfer, and supports multi-language (Chinese-English, Japanese-English, etc.) text-to-speech with a beautiful desktop GUI.

Future plans include launching user-customizable AI virtual character features, allowing users to create their own digital characters.

## 主要特点 / Key Features

- 当前版本为基于游戏"明日方舟"中"能天使"角色设定的 AI 数字人 / AI Digital Character based on Exusiai from Arknights
- 角色语音和性格特征提取自游戏内容 / Character voice and personality extracted from game content
- 自然流畅的语音合成 / Natural and fluent voice synthesis
- 基于 DeepSeek API 的智能对话 / Intelligent dialogue based on DeepSeek API
- 美观的桌面图形界面 / Beautiful desktop GUI
- 支持语音输入和文本输入 / Support for both voice and text input
- 实时语音合成和播放 / Real-time voice synthesis and playback
- 支持自定义对话参数 / Customizable dialogue parameters
- 支持对话历史记录保存 / Support for dialogue history saving

## 系统要求 / System Requirements

### 硬件要求 / Hardware Requirements
- CPU：Intel i5/AMD Ryzen 5 或更高 / Intel i5/AMD Ryzen 5 or higher
- 内存：8GB RAM 或更高 / 8GB RAM or higher
- 显卡：NVIDIA GPU（推荐 RTX 2060 或更高） / NVIDIA GPU (RTX 2060 or higher recommended)
- 存储空间：至少 10GB 可用空间 / At least 10GB free storage space

### 软件要求 / Software Requirements
- 操作系统：Windows 10/11 64位 / Windows 10/11 64-bit
- Python 3.9 或更高版本 / Python 3.9 or higher
- 网络：稳定的互联网连接 / Stable internet connection
- 音频设备：支持音频输入输出的声卡 / Sound card with audio input/output support

## 技术架构 / Technical Architecture

- 前端界面：PyQt6 / Frontend: PyQt6
- 语音合成：GPT-SoVITS / Voice Synthesis: GPT-SoVITS
- 大语言模型：DeepSeek API / LLM: DeepSeek API
- 音频处理：PyDub / Audio Processing: PyDub
- 语音识别：Whisper / Speech Recognition: Whisper

## 安装说明 / Installation

1. 克隆仓库 / Clone the repository:
```bash
git clone https://github.com/yourusername/ExusiAI.git
cd ExusiAI
```

2. 安装依赖 / Install dependencies:
```bash
pip install -r requirements.txt
```

3. 配置 API 密钥 / Configure API keys:
- 在 `config.py` 中设置 DeepSeek API 密钥 / Set DeepSeek API key in `config.py`
- 确保已安装 GPT-SoVITS 并配置相关路径 / Ensure GPT-SoVITS is installed and paths are configured

## 使用说明 / Usage

1. 启动应用 / Launch the application:
```bash
python main.py
```

2. 主要功能 / Main features:
- 点击麦克风图标开始语音输入 / Click microphone icon for voice input
- 在文本框中输入文字进行对话 / Type in text box for dialogue
- 使用设置按钮调整对话参数 / Use settings button to adjust dialogue parameters
- 查看对话历史记录 / View dialogue history

## 项目结构 / Project Structure

```
ExusiAI/
├── main.py              # 主程序入口 / Main program entry
├── config.py            # 配置文件 / Configuration file
├── requirements.txt     # 依赖列表 / Dependencies list
├── README.md           # 项目说明文档 / Project documentation
├── src/                # 源代码目录 / Source code directory
│   ├── ui/            # 界面相关代码 / UI related code
│   ├── core/          # 核心功能模块 / Core functionality modules
│   ├── utils/         # 工具函数 / Utility functions
│   └── resources/     # 资源文件 / Resource files
└── tests/             # 测试文件 / Test files
```

## 注意事项 / Notes

- 需要稳定的网络连接以使用 DeepSeek API / Stable internet connection required for DeepSeek API
- 建议使用耳机以获得最佳语音体验 / Headphones recommended for best voice experience
- 首次运行可能需要下载模型文件 / Model files may need to be downloaded on first run
- 请确保系统已安装必要的音频驱动 / Ensure system has necessary audio drivers installed

## 未来计划 / Future Plans

- 支持更多语言 / Support for more languages
- 添加更多角色模板 / Add more character templates
- 优化语音合成质量 / Optimize voice synthesis quality
- 增加更多交互功能 / Add more interactive features
- 推出用户自定义 AI 虚拟角色功能 / Launch user-customizable AI virtual character features

## 贡献指南 / Contributing

欢迎提交 Issue 和 Pull Request 来帮助改进项目。在提交代码前，请确保：

- 代码符合项目的编码规范 / Code follows project coding standards
- 添加了必要的测试用例 / Added necessary test cases
- 更新了相关文档 / Updated relevant documentation

## 许可证 / License

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 致谢 / Acknowledgments

- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - 语音合成基础 / Voice synthesis foundation
- [DeepSeek](https://deepseek.com) - 大语言模型支持 / LLM support
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) - 图形界面框架 / GUI framework
- [Whisper](https://github.com/openai/whisper) - 语音识别支持 / Speech recognition support
- [明日方舟](https://www.arknights.global/) - 角色原型来源 / Character prototype source
