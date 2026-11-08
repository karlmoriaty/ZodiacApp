import os
import sys


os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random
import pygame


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class ZodiacApp:
    def __init__(self, root):
        self.root = root
        self.root.title("星座查询")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        
        self.zodiac_info = self._init_zodiac_info()
        self._init_ui()
        self._init_music()
    
    def _init_zodiac_info(self):
        return {
            "摩羯座": {
                "dates": "12月22日 - 1月19日",
                "element": "土象星座",
                "description": "摩羯座是象征着冬天开始的星座，冬天把绝对意识毫无保留地奉献给了摩羯座出生的人。你是一个具有现实主义思想和有抱负的人；同时你又容易被热烈的感情征服，是一个有强烈忘我精神的人。"
            },
            "水瓶座": {
                "dates": "1月20日 - 2月18日",
                "element": "风象星座",
                "description": "水瓶座的人，不愿意接受情感上的丝毫束缚。你时而异想天开，幽默过人，时而又冷若冰霜，令人费解，这常常是一个不易相处的人。有优秀的推理力和求知精神，客观、冷静，善于思考，讲求科学、逻辑和概念，价值观很强。"
            },
            "双鱼座": {
                "dates": "2月19日 - 3月20日",
                "element": "水象星座",
                "description": "双鱼座是黄道十二宫最后一宫，所以他可以说集中了十二星座所有的优点和缺点于一体，而且也可以由代表双鱼座的两条游向相反的鱼所象征中，知道这是多重矛盾的一个星座。"
            },
            "白羊座": {
                "dates": "3月21日 - 4月19日",
                "element": "火象星座",
                "description": "白羊座的人冲动、爱冒险、慷慨、天不怕地不怕，而且一旦下定决心，不到黄河心不死，排除万难的要达到目的。大部分属于白羊座的人的脾气都很差，不过只是炮仗颈，绝对不会放在心上。"
            },
            "金牛座": {
                "dates": "4月20日 - 5月20日",
                "element": "土象星座",
                "description": "金牛座是保守型的星座，他不喜欢变动，安稳是他的生活态度。金牛座的人不会急躁冲动，只有忍耐，而且还非常顽固，一旦决定了的事他不喜欢去改变。"
            },
            "双子座": {
                "dates": "5月21日 - 6月21日",
                "element": "风象星座",
                "description": "双子座的人喜爱变化，不可能同一时间只做一件事情，五时花六时变，心不在焉；虽然拥有些小聪明，但不专一，往往流于肤浅，持久力又低，成功很难，可以说是理性但不安的星座。"
            },
            "巨蟹座": {
                "dates": "6月22日 - 7月22日",
                "element": "水象星座",
                "description": "巨蟹座的人往往充满了爱心，他们将母性的本质发挥到了极限。对他们来说，最重要的东西是家庭。他们往往就像蟹一样，在充满坚硬的外壳下面是柔软的内心。"
            },
            "狮子座": {
                "dates": "7月23日 - 8月22日",
                "element": "火象星座",
                "description": "狮子座的人，自信自强，气度非凡，极具领导统御能力，永不服输，是天生的贵族、王者。只是有时过度追求利，甚至有些自负，莽撞、以自我为中心。"
            },
            "处女座": {
                "dates": "8月23日 - 9月22日",
                "element": "土象星座",
                "description": "处女座追求完美，吹毛求疵是他们的特性。多数的处女座都很谦虚，但也因此给自己造成很大的压力。处女座的人不喜欢闲着，对别人常常乐于服务。"
            },
            "天秤座": {
                "dates": "9月23日 - 10月23日",
                "element": "风象星座",
                "description": "天秤座由金星守护，守护星是维纳斯，影响他们爱好追求和平和谐的感觉；天秤座的人外型优雅、亲切善良、朋友缘极好、喜欢听别人倾诉，沟通力又强，只不过有犹豫不决的最大毛病。"
            },
            "天蝎座": {
                "dates": "10月24日 - 11月22日",
                "element": "水象星座",
                "description": "天蝎座的人精力旺盛、热情、善妒，占有欲极强。他们想要每天过得非常充实，如果失去了目标，他们很难认真地投入精力。天蝎座的人记仇，所以切忌得罪他，有朝一日必定报仇的。"
            },
            "射手座": {
                "dates": "11月23日 - 12月21日",
                "element": "火象星座",
                "description": "射手座的人就像那只在弦上的箭一样，他们主动出击。为人乐观、诚实、热情、喜欢挑战。射手是十二星座中的冒险家，热爱旅行、喜欢赌博。意志力薄弱是射手座天生的弱点，如果沉迷赌博与游戏，后果不堪设想。"
            }
        }
    
    def _get_zodiac(self, month, day):
        zodiac_dates = [
            ("摩羯座", 12, 22, 1, 19),
            ("水瓶座", 1, 20, 2, 18),
            ("双鱼座", 2, 19, 3, 20),
            ("白羊座", 3, 21, 4, 19),
            ("金牛座", 4, 20, 5, 20),
            ("双子座", 5, 21, 6, 21),
            ("巨蟹座", 6, 22, 7, 22),
            ("狮子座", 7, 23, 8, 22),
            ("处女座", 8, 23, 9, 22),
            ("天秤座", 9, 23, 10, 23),
            ("天蝎座", 10, 24, 11, 22),
            ("射手座", 11, 23, 12, 21),
        ]
        
        for zodiac, start_month, start_day, end_month, end_day in zodiac_dates:
            if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
                return zodiac
        return "摩羯座"
    
    def _init_ui(self):
        style = ttk.Style()
        style.configure("Title.TLabel", font=("KaiTi", 20, "bold"))
        style.configure("Info.TLabel", font=("KaiTi", 10))
        style.configure("Result.TLabel", font=("KaiTi", 16, "bold"))
        
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(main_frame, text="🌟 星座查询 🌟", style="Title.TLabel")
        title_label.pack(pady=(0, 20))
        
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(input_frame, text="请选择您的出生日期：", style="Info.TLabel").pack(anchor=tk.W)
        
        date_frame = ttk.Frame(input_frame)
        date_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.year_var = tk.StringVar(value=str(datetime.now().year))
        self.month_var = tk.StringVar(value="1")
        self.day_var = tk.StringVar(value="1")
        
        ttk.Label(date_frame, text="年：").pack(side=tk.LEFT)
        year_spin = ttk.Spinbox(date_frame, from_=1900, to=2100, textvariable=self.year_var, width=8)
        year_spin.pack(side=tk.LEFT, padx=(5, 10))
        
        ttk.Label(date_frame, text="月：").pack(side=tk.LEFT)
        month_spin = ttk.Spinbox(date_frame, from_=1, to=12, textvariable=self.month_var, width=5)
        month_spin.pack(side=tk.LEFT, padx=(5, 10))
        
        ttk.Label(date_frame, text="日：").pack(side=tk.LEFT)
        day_spin = ttk.Spinbox(date_frame, from_=1, to=31, textvariable=self.day_var, width=5)
        day_spin.pack(side=tk.LEFT, padx=(5, 0))
        
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 20))
        
        query_button = ttk.Button(button_frame, text="查询", command=self.query_zodiac)
        query_button.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_button = ttk.Button(button_frame, text="清除", command=self.clear_result)
        clear_button.pack(side=tk.LEFT)
        
        self.result_frame = ttk.Frame(main_frame)
        self.result_frame.pack(fill=tk.BOTH, expand=True)
        
        self.result_label = ttk.Label(self.result_frame, text="", style="Result.TLabel")
        self.result_label.pack(pady=(0, 10))
        
        self.dates_label = ttk.Label(self.result_frame, text="", style="Info.TLabel")
        self.dates_label.pack(pady=(0, 5))
        
        self.element_label = ttk.Label(self.result_frame, text="", style="Info.TLabel")
        self.element_label.pack(pady=(0, 10))
        
        self.desc_text = tk.Text(self.result_frame, wrap=tk.WORD, height=8, font=("KaiTi", 10))
        self.desc_text.pack(fill=tk.BOTH, expand=True)
        self.desc_text.config(state=tk.DISABLED)
    
    def _init_music(self):
        try:
            pygame.mixer.init()
            music_path = resource_path(os.path.join("Music", "消散对白（女声）.MP3"))
            
            if os.path.exists(music_path):
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"音乐加载失败: {e}")
    
    def query_zodiac(self):
        try:
            year = int(self.year_var.get())
            month = int(self.month_var.get())
            day = int(self.day_var.get())
            
            try:
                datetime(year, month, day)
            except ValueError:
                messagebox.showerror("错误", "请输入有效的日期！")
                return
            
            zodiac_name = self._get_zodiac(month, day)
            info = self.zodiac_info[zodiac_name]
            
            self.result_label.config(text=f"您的星座是：{zodiac_name}")
            self.dates_label.config(text=f"日期范围：{info['dates']}")
            self.element_label.config(text=f"属性：{info['element']}")
            
            self.desc_text.config(state=tk.NORMAL)
            self.desc_text.delete(1.0, tk.END)
            self.desc_text.insert(tk.END, info['description'])
            self.desc_text.config(state=tk.DISABLED)
            
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字！")
        except Exception as e:
            messagebox.showerror("错误", f"发生错误：{str(e)}")
    
    def clear_result(self):
        self.result_label.config(text="")
        self.dates_label.config(text="")
        self.element_label.config(text="")
        self.desc_text.config(state=tk.NORMAL)
        self.desc_text.delete(1.0, tk.END)
        self.desc_text.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = ZodiacApp(root)
    root.mainloop()
    try:
        pygame.mixer.quit()
    except:
        pass


if __name__ == "__main__":
    main()
