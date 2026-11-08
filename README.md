# ZodiacApp - 星座查询桌面应用

一个基于 Python + Tkinter 的星座查询桌面小工具，支持根据出生日期查询星座信息。

## 功能特性

- 根据日期自动计算对应星座
- 12 星座的日期范围定义与描述
- 内置背景音乐播放
- PyInstaller 打包为 Windows 单文件可执行程序

## 技术栈

- **Python 3.x**
- **tkinter**（GUI）
- **pygame**（音频播放）
- **PyInstaller**（打包）

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 运行
python zodiac_app.py
```

## 打包

```bash
pyinstaller zodiac_app.spec
```

打包后可执行文件位于 `dist/` 目录。
