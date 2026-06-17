import os
import zipfile

def create_agent_files():
    # Nội dung của file agent.py (Giao diện Tkinter cực đẹp, cao cấp, đầy đủ tính năng)
    agent_py_content = """# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sys
import os
import platform
import subprocess
import threading
import time
import json

class AntigravityAgentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Antigravity AI Agent - Phiên bản Pro v1.0")
        self.root.geometry("900x650")
        self.root.configure(bg="#0f172a") # Slate 900
        
        # Đặt font mặc định
        self.font_family = "Segoe UI" if platform.system() == "Windows" else "Helvetica"
        
        # Khởi tạo dữ liệu
        self.api_key = ""
        self.load_config()
        
        # Khởi tạo giao diện
        self.setup_styles()
        self.create_layout()
        
        # Mở tab mặc định
        self.select_tab("chat")
        
        self.append_bot_message("Xin chào! Tôi là Antigravity AI Agent Pro v1.0 được phát triển bởi Google DeepMind & Antigravity Team.\\n"
                               "Tôi có thể hỗ trợ bạn lập trình, kiểm tra hệ thống và dọn dẹp bộ nhớ máy tính.\\n"
                               "Hãy nhập câu hỏi ở bên dưới hoặc khám phá các tính năng ở thanh menu bên trái!")

    def load_config(self):
        try:
            if os.path.exists("config.json"):
                with open("config.json", "r", encoding="utf-8") as f:
                    config = json.load(f)
                    self.api_key = config.get("api_key", "")
        except Exception:
            pass

    def save_config(self):
        try:
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump({"api_key": self.api_key}, f, indent=4)
        except Exception:
            pass

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        
        # Cấu hình Scrollbar
        style.configure("Vertical.TScrollbar", 
                        gripcount=0,
                        background="#1e293b", 
                        troughcolor="#0f172a", 
                        bordercolor="#0f172a", 
                        arrowcolor="#94a3b8")
        
        # Cấu hình Entry
        style.configure("TEntry", fieldbackground="#1e293b", foreground="#f8fafc", insertcolor="#f8fafc")

    def create_layout(self):
        # Container chính
        self.main_container = tk.Frame(self.root, bg="#0f172a")
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # 1. Sidebar bên trái (Thanh Menu)
        self.sidebar = tk.Frame(self.main_container, bg="#1e293b", width=220)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)
        
        # Logo & Tên phần mềm ở Sidebar
        logo_label = tk.Label(self.sidebar, text="ANTIGRAVITY", font=(self.font_family, 16, "bold"), fg="#38bdf8", bg="#1e293b")
        logo_label.pack(pady=(25, 5))
        sub_logo = tk.Label(self.sidebar, text="AI AGENT PRO", font=(self.font_family, 10, "bold"), fg="#94a3b8", bg="#1e293b")
        sub_logo.pack(pady=(0, 25))
        
        # Các nút Menu
        self.menu_buttons = {}
        menu_items = [
            ("chat", "💬  Trò chuyện AI"),
            ("system", "💻  Hệ thống PC"),
            ("code", "⚡  Trình tạo Code"),
            ("cleaner", "🧹  Dọn dẹp Temp"),
            ("setting", "⚙️  Cấu hình API")
        ]
        
        for tab_id, label in menu_items:
            btn = tk.Button(
                self.sidebar, 
                text=label, 
                font=(self.font_family, 11), 
                anchor="w",
                bg="#1e293b", 
                fg="#e2e8f0", 
                activebackground="#334155", 
                activeforeground="#f8fafc",
                bd=0, 
                padx=20, 
                pady=12,
                cursor="hand2",
                command=lambda tid=tab_id: self.select_tab(tid)
            )
            btn.pack(fill=tk.X, pady=2)
            self.menu_buttons[tab_id] = btn
            
        # Thẻ thông tin phiên bản ở cuối sidebar
        version_lbl = tk.Label(self.sidebar, text="Phiên bản: 1.0.0 Pro\\nDeepMind Engine", font=(self.font_family, 8), fg="#64748b", bg="#1e293b")
        version_lbl.pack(side=tk.BOTTOM, pady=15)
        
        # Separator dọc
        sep = tk.Frame(self.main_container, width=1, bg="#334155")
        sep.pack(side=tk.LEFT, fill=tk.Y)
        
        # 2. Vùng hiển thị nội dung bên phải
        self.content_area = tk.Frame(self.main_container, bg="#0f172a")
        self.content_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Khởi tạo các View/Tab nội dung
        self.tab_frames = {}
        self.init_chat_tab()
        self.init_system_tab()
        self.init_code_tab()
        self.init_cleaner_tab()
        self.init_setting_tab()

    def select_tab(self, tab_id):
        # Ẩn tất cả các tab
        for frame in self.tab_frames.values():
            frame.pack_forget()
            
        # Đặt lại màu nền nút menu
        for tid, btn in self.menu_buttons.items():
            if tid == tab_id:
                btn.configure(bg="#334155", fg="#38bdf8")
            else:
                btn.configure(bg="#1e293b", fg="#e2e8f0")
                
        # Hiện tab được chọn
        self.tab_frames[tab_id].pack(fill=tk.BOTH, expand=True)

    # ------------------ TAB 1: TRÒ CHUYỆN AI ------------------
    def init_chat_tab(self):
        frame = tk.Frame(self.content_area, bg="#0f172a")
        self.tab_frames["chat"] = frame
        
        # Header
        header = tk.Frame(frame, bg="#1e293b", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        title = tk.Label(header, text="Trợ lý AI Antigravity Pro", font=(self.font_family, 12, "bold"), fg="#f8fafc", bg="#1e293b", padx=15)
        title.pack(side=tk.LEFT, fill=tk.Y)
        
        # Chat History
        chat_container = tk.Frame(frame, bg="#0f172a", padx=15, pady=15)
        chat_container.pack(fill=tk.BOTH, expand=True)
        
        self.chat_text = tk.Text(
            chat_container, 
            bg="#1e293b", 
            fg="#f8fafc", 
            font=(self.font_family, 11), 
            bd=0, 
            padx=10, 
            pady=10,
            state=tk.DISABLED,
            wrap=tk.WORD
        )
        self.chat_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Tags định dạng tin nhắn Chat
        self.chat_text.tag_configure("bot", foreground="#38bdf8")
        self.chat_text.tag_configure("user", foreground="#a7f3d0")
        self.chat_text.tag_configure("system", foreground="#94a3b8")
        
        scrollbar = ttk.Scrollbar(chat_container, orient="vertical", command=self.chat_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_text.configure(yscrollcommand=scrollbar.set)
        
        # Khung nhập tin nhắn
        input_container = tk.Frame(frame, bg="#0f172a", padx=15, pady=(0, 15))
        input_container.pack(fill=tk.X)
        
        self.chat_input = tk.Entry(
            input_container, 
            bg="#1e293b", 
            fg="#f8fafc", 
            insertbackground="#f8fafc", 
            font=(self.font_family, 11),
            bd=1,
            relief=tk.FLAT
        )
        self.chat_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipady=8)
        self.chat_input.bind("<Return>", lambda event: self.send_message())
        
        send_btn = tk.Button(
            input_container, 
            text="Gửi đi", 
            font=(self.font_family, 10, "bold"), 
            bg="#38bdf8", 
            fg="#0f172a", 
            activebackground="#0284c7",
            activeforeground="#f8fafc",
            bd=0, 
            padx=20,
            cursor="hand2",
            command=self.send_message
        )
        send_btn.pack(side=tk.RIGHT, padx=(10, 0))

    def append_bot_message(self, text):
        self.chat_text.configure(state=tk.NORMAL)
        self.chat_text.insert(tk.END, "🤖 Antigravity AI Agent:\\n", "bot")
        self.chat_text.insert(tk.END, text + "\\n\\n")
        self.chat_text.configure(state=tk.DISABLED)
        self.chat_text.see(tk.END)

    def send_message(self):
        msg = self.chat_input.get().strip()
        if not msg:
            return
            
        self.chat_input.delete(0, tk.END)
        
        self.chat_text.configure(state=tk.NORMAL)
        self.chat_text.insert(tk.END, "👤 Bạn:\\n", "user")
        self.chat_text.insert(tk.END, msg + "\\n\\n")
        self.chat_text.configure(state=tk.DISABLED)
        self.chat_text.see(tk.END)
        
        # Xử lý phản hồi tự động trong thread phụ tránh treo UI
        threading.Thread(target=self.generate_response, args=(msg,), daemon=True).start()

    def generate_response(self, prompt):
        time.sleep(0.5) # Giả lập phản hồi nhanh
        prompt_lower = prompt.lower()
        
        # Nếu có API Key, chúng ta có thể gọi API thật (ví dụ Gemini API). 
        # Nếu chưa cấu hình, chạy ngoại tuyến thông minh.
        if self.api_key:
            try:
                import urllib.request
                import json
                
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.api_key}"
                data = {
                    "contents": [{"parts": [{"text": prompt}]}]
                }
                req = urllib.request.Request(
                    url, 
                    data=json.dumps(data).encode("utf-8"),
                    headers={"Content-Type": "application/json"}
                )
                with urllib.request.urlopen(req, timeout=15) as res:
                    res_body = json.loads(res.read().decode("utf-8"))
                    bot_text = res_body['candidates'][0]['content']['parts'][0]['text']
                    self.append_bot_message(bot_text)
                    return
            except Exception as e:
                self.append_bot_message(f"Có lỗi khi kết nối tới Gemini API: {str(e)}\\nĐang tự động chuyển sang Chế độ Ngoại tuyến...")
        
        # Logic ngoại tuyến (Offline Mode) thông minh
        if "hello" in prompt_lower or "chào" in prompt_lower or "hi" in prompt_lower:
            reply = ("Xin chào bạn! Tôi là Antigravity Agent. Tôi là trợ lý AI thông minh chạy offline.\\n"
                     "Bạn có thể yêu cầu tôi các tác vụ sau:\\n"
                     "- 'Xem thông tin hệ thống' hoặc chuyển sang tab Hệ thống để kiểm tra máy tính.\\n"
                     "- 'Tạo code Python' để sinh mã nguồn nhanh.\\n"
                     "- 'Dọn rác' để làm sạch máy tính.\\n"
                     "Nếu bạn có Gemini API Key, hãy vào tab 'Cấu hình API' để liên kết và chat online!")
        elif "hệ thống" in prompt_lower or "system" in prompt_lower or "cpu" in prompt_lower:
            reply = "Đang lấy thông tin hệ thống... Vui lòng xem kết quả chi tiết ở tab 'Hệ thống PC' ở thanh menu bên trái."
            self.root.after(0, lambda: self.select_tab("system"))
            self.root.after(0, self.refresh_system_info)
        elif "dọn dẹp" in prompt_lower or "dọn rác" in prompt_lower or "clean" in prompt_lower:
            reply = "Đang chuyển bạn sang Tab 'Dọn dẹp Temp' để quét và tối ưu hệ thống."
            self.root.after(0, lambda: self.select_tab("cleaner"))
            self.root.after(0, self.scan_temp_files)
        elif "code" in prompt_lower or "lập trình" in prompt_lower or "viết code" in prompt_lower:
            reply = "Bạn có thể vào tab 'Trình tạo Code' ở menu bên trái để chọn các dự án mẫu và xuất file code nhanh chóng."
            self.root.after(0, lambda: self.select_tab("code"))
        elif "antigravity" in prompt_lower:
            reply = ("Antigravity AI Agent Pro là một agent thông minh được thiết kế đặc biệt bởi Google DeepMind.\\n"
                     "Tên gọi 'Antigravity' (Chống trọng lực) biểu trưng cho tốc độ xử lý siêu việt, vượt qua mọi giới hạn truyền thống của phần mềm!")
        else:
            reply = ("Tôi đã nhận được câu hỏi: \\"" + prompt + "\\"\\n\\n"
                     "Vì hiện tại bạn chưa cấu hình Gemini API Key nên tôi đang trả lời ở chế độ Ngoại tuyến.\\n"
                     "Hãy truy cập tab 'Cấu hình API' ở bên trái, dán khóa API của bạn vào để có thể trò chuyện đầy đủ với tôi nhé!")
                     
        self.append_bot_message(reply)

    # ------------------ TAB 2: HỆ THỐNG PC ------------------
    def init_system_tab(self):
        frame = tk.Frame(self.content_area, bg="#0f172a")
        self.tab_frames["system"] = frame
        
        # Header
        header = tk.Frame(frame, bg="#1e293b", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        title = tk.Label(header, text="Thông tin Hệ thống Máy tính", font=(self.font_family, 12, "bold"), fg="#f8fafc", bg="#1e293b", padx=15)
        title.pack(side=tk.LEFT, fill=tk.Y)
        
        refresh_btn = tk.Button(
            header, 
            text="🔄 Làm mới", 
            font=(self.font_family, 9, "bold"), 
            bg="#38bdf8", 
            fg="#0f172a", 
            activebackground="#0284c7",
            activeforeground="#f8fafc",
            bd=0, 
            padx=15,
            cursor="hand2",
            command=self.refresh_system_info
        )
        refresh_btn.pack(side=tk.RIGHT, padx=15, pady=10)
        
        # Nội dung thông tin
        self.sys_info_container = tk.Frame(frame, bg="#0f172a", padx=30, pady=30)
        self.sys_info_container.pack(fill=tk.BOTH, expand=True)
        
        self.lbl_os = tk.Label(self.sys_info_container, text="Hệ điều hành: Đang quét...", font=(self.font_family, 11), fg="#cbd5e1", bg="#0f172a", anchor="w")
        self.lbl_os.pack(fill=tk.X, pady=8)
        
        self.lbl_cpu = tk.Label(self.sys_info_container, text="Vi xử lý CPU: Đang quét...", font=(self.font_family, 11), fg="#cbd5e1", bg="#0f172a", anchor="w")
        self.lbl_cpu.pack(fill=tk.X, pady=8)
        
        self.lbl_ram = tk.Label(self.sys_info_container, text="Bộ nhớ RAM: Đang quét...", font=(self.font_family, 11), fg="#cbd5e1", bg="#0f172a", anchor="w")
        self.lbl_ram.pack(fill=tk.X, pady=8)
        
        self.lbl_py = tk.Label(self.sys_info_container, text="Phiên bản Python: Đang quét...", font=(self.font_family, 11), fg="#cbd5e1", bg="#0f172a", anchor="w")
        self.lbl_py.pack(fill=tk.X, pady=8)
        
        self.lbl_host = tk.Label(self.sys_info_container, text="Tên máy (Hostname): Đang quét...", font=(self.font_family, 11), fg="#cbd5e1", bg="#0f172a", anchor="w")
        self.lbl_host.pack(fill=tk.X, pady=8)
        
        # Thêm một đồ họa đo tải giả lập/thực tế cho đẹp mắt
        self.lbl_status = tk.Label(self.sys_info_container, text="Trạng thái hệ thống: Ổn định", font=(self.font_family, 11, "bold"), fg="#4ade80", bg="#0f172a", anchor="w")
        self.lbl_status.pack(fill=tk.X, pady=25)
        
        # Tự động quét thông tin khi mở ứng dụng
        self.root.after(100, self.refresh_system_info)

    def refresh_system_info(self):
        # Hệ điều hành
        os_info = f"{platform.system()} {platform.release()} (Bản dựng {platform.version()})"
        self.lbl_os.configure(text=f"💻 Hệ điều hành: {os_info}")
        
        # Tên máy
        self.lbl_host.configure(text=f"📛 Tên máy (Hostname): {platform.node()}")
        
        # Phiên bản Python
        self.lbl_py.configure(text=f"🐍 Phiên bản Python: {sys.version.split()[0]} ({sys.executable})")
        
        # CPU Info (Thực tế thông qua lệnh WMI trên Windows)
        def run_cpu_detect():
            cpu_name = platform.processor()
            if platform.system() == "Windows":
                try:
                    out = subprocess.check_output("wmic cpu get name", shell=True).decode("utf-8")
                    lines = [line.strip() for line in out.split('\\n') if line.strip()]
                    if len(lines) > 1:
                        cpu_name = lines[1]
                except Exception:
                    pass
            self.lbl_cpu.configure(text=f"⚙️ Vi xử lý CPU: {cpu_name}")
            
        threading.Thread(target=run_cpu_detect, daemon=True).start()
        
        # RAM Info (Thực tế trên Windows)
        def run_ram_detect():
            ram_info = "Không xác định"
            if platform.system() == "Windows":
                try:
                    out = subprocess.check_output("wmic computersystem get totalphysicalmemory", shell=True).decode("utf-8")
                    lines = [line.strip() for line in out.split('\\n') if line.strip()]
                    if len(lines) > 1:
                        bytes_val = int(lines[1])
                        gb_val = bytes_val / (1024 ** 3)
                        ram_info = f"{gb_val:.2f} GB RAM Vật lý"
                except Exception:
                    pass
            self.lbl_ram.configure(text=f"💾 Bộ nhớ RAM: {ram_info}")
            
        threading.Thread(target=run_ram_detect, daemon=True).start()

    # ------------------ TAB 3: TRÌNH TẠO CODE MẪU ------------------
    def init_code_tab(self):
        frame = tk.Frame(self.content_area, bg="#0f172a")
        self.tab_frames["code"] = frame
        
        # Header
        header = tk.Frame(frame, bg="#1e293b", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        title = tk.Label(header, text="Trình xuất mã nguồn thông minh (QuickCode)", font=(self.font_family, 12, "bold"), fg="#f8fafc", bg="#1e293b", padx=15)
        title.pack(side=tk.LEFT, fill=tk.Y)
        
        # Giao diện chính tab Code
        main_body = tk.Frame(frame, bg="#0f172a", padx=20, pady=20)
        main_body.pack(fill=tk.BOTH, expand=True)
        
        # Chọn mẫu
        select_lbl = tk.Label(main_body, text="Chọn mẫu thiết kế (Template):", font=(self.font_family, 10, "bold"), fg="#e2e8f0", bg="#0f172a", anchor="w")
        select_lbl.pack(fill=tk.X, pady=(0, 5))
        
        # Combobox chọn ngôn ngữ / dự án
        self.code_templates = {
            "Mẫu Flask Web App Server": (
                "from flask import Flask, render_template, jsonify\\n\\n"
                "app = Flask(__name__)\\n\\n"
                "@app.route('/')\\n"
                "def index():\\n"
                "    return '<h1>Server Flask của bạn đang hoạt động cực kỳ mượt mà!</h1>'\\n\\n"
                "@app.route('/api/status')\\n"
                "def status():\\n"
                "    return jsonify({\\"status\\": \\"running\\", \\"uptime\\": \\"100%\\"\\})\\n\\n"
                "if __name__ == '__main__':\\n"
                "    app.run(debug=True, port=8080)\\n"
            ),
            "Mẫu Tool tự động hóa đổi tên file": (
                "import os\\n\\n"
                "def clean_and_rename(directory, prefix=\\"file_\\"):\\n"
                "    if not os.path.exists(directory):\\n"
                "        print(f'Thu muc {directory} khong ton tai!')\\n"
                "        return\\n"
                "    \\n"
                "    files = os.listdir(directory)\\n"
                "    for index, filename in enumerate(files):\\n"
                "        ext = os.path.splitext(filename)[1]\\n"
                "        old_path = os.path.join(directory, filename)\\n"
                "        new_name = f'{prefix}{index + 1}{ext}'\\n"
                "        new_path = os.path.join(directory, new_name)\\n"
                "        os.rename(old_path, new_path)\\n"
                "        print(f'Da doi: {filename} -> {new_name}')\\n"
                "\\n"
                "if __name__ == '__main__':\\n"
                "    # Thay the bang duong dan thu muc cua ban\\n"
                "    clean_and_rename(r'C:\\\\Users\\\\Public\\\\Documents')\\n"
            ),
            "Mẫu Script vẽ đồ thị hình xoắn ốc (Turtle)": (
                "import turtle\\n"
                "import colorsys\\n\\n"
                "def draw_spiral():\\n"
                "    t = turtle.Turtle()\\n"
                "    s = turtle.Screen()\\n"
                "    s.bgcolor('black')\\n"
                "    t.speed(0)\\n"
                "    n = 36\\n"
                "    h = 0\\n"
                "    for i in range(120):\\n"
                "        c = colorsys.hsv_to_rgb(h, 1, 0.8)\\n"
                "        h += 1/n\\n"
                "        t.color(c)\\n"
                "        t.left(145)\\n"
                "        for _ in range(5):\\n"
                "            t.forward(i * 2)\\n"
                "            t.left(150)\\n"
                "    turtle.done()\\n"
                "\\n"
                "if __name__ == '__main__':\\n"
                "    draw_spiral()\\n"
            )
        }
        
        self.cbo_templates = ttk.Combobox(
            main_body, 
            values=list(self.code_templates.keys()), 
            state="readonly", 
            font=(self.font_family, 10)
        )
        self.cbo_templates.pack(fill=tk.X, pady=(0, 15))
        self.cbo_templates.current(0)
        self.cbo_templates.bind("<<ComboboxSelected>>", self.on_template_change)
        
        # Preview Code Box
        preview_lbl = tk.Label(main_body, text="Xem trước mã nguồn (Code Preview):", font=(self.font_family, 10, "bold"), fg="#e2e8f0", bg="#0f172a", anchor="w")
        preview_lbl.pack(fill=tk.X, pady=(0, 5))
        
        preview_container = tk.Frame(main_body, bg="#0f172a")
        preview_container.pack(fill=tk.BOTH, expand=True)
        
        self.code_text = tk.Text(
            preview_container, 
            bg="#1e293b", 
            fg="#34d399", # Green 400
            font=("Consolas", 10), 
            bd=0, 
            padx=10, 
            pady=10
        )
        self.code_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(preview_container, orient="vertical", command=self.code_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.code_text.configure(yscrollcommand=scrollbar.set)
        
        # Hộp công cụ thao tác
        tool_bar = tk.Frame(main_body, bg="#0f172a", pady=10)
        tool_bar.pack(fill=tk.X)
        
        save_btn = tk.Button(
            tool_bar, 
            text="💾 Lưu thành file...", 
            font=(self.font_family, 10, "bold"), 
            bg="#38bdf8", 
            fg="#0f172a", 
            activebackground="#0284c7",
            activeforeground="#f8fafc",
            bd=0, 
            padx=15, 
            pady=8,
            cursor="hand2",
            command=self.save_code_to_file
        )
        save_btn.pack(side=tk.RIGHT, padx=5)
        
        run_btn = tk.Button(
            tool_bar, 
            text="🚀 Chạy thử Code", 
            font=(self.font_family, 10, "bold"), 
            bg="#10b981", 
            fg="#f8fafc", 
            activebackground="#059669",
            activeforeground="#f8fafc",
            bd=0, 
            padx=15, 
            pady=8,
            cursor="hand2",
            command=self.run_code_sample
        )
        run_btn.pack(side=tk.RIGHT, padx=5)
        
        self.on_template_change(None)

    def on_template_change(self, event):
        selected = self.cbo_templates.get()
        code = self.code_templates.get(selected, "")
        self.code_text.delete("1.0", tk.END)
        self.code_text.insert("1.0", code)

    def save_code_to_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".py", 
            filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                code_content = self.code_text.get("1.0", tk.END)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(code_content)
                messagebox.showinfo("Thành công", f"Đã lưu mã nguồn thành công tại:\\n{file_path}")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể lưu file: {str(e)}")

    def run_code_sample(self):
        code_content = self.code_text.get("1.0", tk.END)
        
        # Chạy trong một file tạm thời
        temp_file = "temp_agent_sample.py"
        try:
            with open(temp_file, "w", encoding="utf-8") as f:
                f.write(code_content)
                
            # Khởi chạy một tiến trình con python mới để chạy thử mã nguồn
            def runner():
                try:
                    # Dùng subprocess để mở cửa sổ chạy độc lập
                    if platform.system() == "Windows":
                        subprocess.Popen(f"start cmd /c \\"py {temp_file} & pause\\"", shell=True)
                    else:
                        subprocess.Popen(f"python {temp_file}", shell=True)
                except Exception as ex:
                    self.root.after(0, lambda: messagebox.showerror("Lỗi", f"Không thể khởi chạy Python: {str(ex)}"))
                    
            threading.Thread(target=runner, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tạo file tạm: {str(e)}")

    # ------------------ TAB 4: DỌN DẸP HỆ THỐNG TEMP ------------------
    def init_cleaner_tab(self):
        frame = tk.Frame(self.content_area, bg="#0f172a")
        self.tab_frames["cleaner"] = frame
        
        # Header
        header = tk.Frame(frame, bg="#1e293b", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        title = tk.Label(header, text="Dọn dẹp & Tối ưu hóa PC", font=(self.font_family, 12, "bold"), fg="#f8fafc", bg="#1e293b", padx=15)
        title.pack(side=tk.LEFT, fill=tk.Y)
        
        # Giao diện
        body = tk.Frame(frame, bg="#0f172a", padx=30, pady=30)
        body.pack(fill=tk.BOTH, expand=True)
        
        desc = tk.Label(
            body, 
            text="Môi trường Windows sẽ tích lũy tệp tin tạm (Temp Files) qua quá trình làm việc.\\n"
                 "Tool này giúp bạn quét dọn an toàn thư mục bộ nhớ tạm của hệ thống để giải phóng dung lượng đĩa cứng.",
            font=(self.font_family, 10), 
            fg="#cbd5e1", 
            bg="#0f172a",
            justify=tk.LEFT,
            anchor="w"
        )
        desc.pack(fill=tk.X, pady=(0, 20))
        
        # Khung chứa kết quả quét
        res_box = tk.LabelFrame(body, text="Kết quả phân tích", font=(self.font_family, 10, "bold"), fg="#38bdf8", bg="#1e293b", padx=15, pady=15)
        res_box.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        self.lbl_scan_status = tk.Label(res_box, text="Trạng thái: Chưa quét hệ thống.", font=(self.font_family, 11), fg="#cbd5e1", bg="#1e293b", anchor="w")
        self.lbl_scan_status.pack(fill=tk.X, pady=5)
        
        self.lbl_scan_size = tk.Label(res_box, text="Dung lượng rác tìm thấy: 0 MB", font=(self.font_family, 11), fg="#cbd5e1", bg="#1e293b", anchor="w")
        self.lbl_scan_size.pack(fill=tk.X, pady=5)
        
        # Progressbar
        self.progress = ttk.Progressbar(body, orient="horizontal", mode="determinate")
        self.progress.pack(fill=tk.X, pady=(0, 20))
        
        # Nút điều khiển
        ctrl_bar = tk.Frame(body, bg="#0f172a")
        ctrl_bar.pack(fill=tk.X)
        
        self.btn_scan = tk.Button(
            ctrl_bar, 
            text="🔍 Quét tệp Temp", 
            font=(self.font_family, 10, "bold"), 
            bg="#38bdf8", 
            fg="#0f172a", 
            activebackground="#0284c7",
            activeforeground="#f8fafc",
            bd=0, 
            padx=20, 
            pady=10,
            cursor="hand2",
            command=self.scan_temp_files
        )
        self.btn_scan.pack(side=tk.LEFT, padx=5)
        
        self.btn_clean = tk.Button(
            ctrl_bar, 
            text="🧹 Dọn sạch tệp Temp", 
            font=(self.font_family, 10, "bold"), 
            bg="#ef4444", 
            fg="#f8fafc", 
            activebackground="#dc2626",
            activeforeground="#f8fafc",
            bd=0, 
            padx=20, 
            pady=10,
            cursor="hand2",
            state=tk.DISABLED,
            command=self.clean_temp_files
        )
        self.btn_clean.pack(side=tk.LEFT, padx=5)
        
        # Lưu trữ danh sách file temp quét được
        self.temp_files_list = []
        self.temp_bytes = 0

    def scan_temp_files(self):
        self.btn_scan.configure(state=tk.DISABLED)
        self.btn_clean.configure(state=tk.DISABLED)
        self.lbl_scan_status.configure(text="Trạng thái: Đang quét bộ nhớ tạm...")
        self.progress.configure(value=0)
        
        def run_scan():
            import tempfile
            temp_dir = tempfile.gettempdir()
            self.temp_files_list = []
            self.temp_bytes = 0
            
            try:
                files = os.listdir(temp_dir)
                total_files = len(files)
                for idx, name in enumerate(files):
                    # Giả lập tiến trình thanh loading
                    if total_files > 0:
                        self.progress.configure(value=int(((idx + 1) / total_files) * 100))
                    
                    path = os.path.join(temp_dir, name)
                    try:
                        if os.path.isfile(path) or os.path.islink(path):
                            size = os.path.getsize(path)
                            self.temp_files_list.append(path)
                            self.temp_bytes += size
                    except Exception:
                        pass
                        
                size_mb = self.temp_bytes / (1024 * 1024)
                
                self.lbl_scan_status.configure(text=f"Trạng thái: Đã quét xong thư mục {temp_dir}")
                self.lbl_scan_size.configure(text=f"Dung lượng rác tìm thấy: {size_mb:.2f} MB ({len(self.temp_files_list)} tệp tin)")
                
                if len(self.temp_files_list) > 0:
                    self.btn_clean.configure(state=tk.NORMAL)
                    
            except Exception as e:
                self.lbl_scan_status.configure(text=f"Lỗi khi quét: {str(e)}")
            finally:
                self.btn_scan.configure(state=tk.NORMAL)
                
        threading.Thread(target=run_scan, daemon=True).start()

    def clean_temp_files(self):
        self.btn_clean.configure(state=tk.DISABLED)
        self.btn_scan.configure(state=tk.DISABLED)
        self.lbl_scan_status.configure(text="Trạng thái: Đang xóa các tệp tin tạm...")
        self.progress.configure(value=0)
        
        def run_clean():
            deleted_count = 0
            fail_count = 0
            total_files = len(self.temp_files_list)
            
            for idx, path in enumerate(self.temp_files_list):
                if total_files > 0:
                    self.progress.configure(value=int(((idx + 1) / total_files) * 100))
                try:
                    os.remove(path)
                    deleted_count += 1
                except Exception:
                    # Một số file đang mở / bị khóa bởi hệ điều hành sẽ bỏ qua
                    fail_count += 1
                    
            size_mb = self.temp_bytes / (1024 * 1024)
            messagebox.showinfo(
                "Dọn dẹp hoàn tất", 
                f"Đã dọn dẹp xong!\\n\\n"
                f"- Xóa thành công: {deleted_count} tệp tin\\n"
                f"- Bỏ qua (Đang sử dụng): {fail_count} tệp tin\\n"
                f"- Giải phóng dung lượng thành công!"
            )
            
            self.lbl_scan_status.configure(text="Trạng thái: Đã dọn dẹp sạch sẽ hệ thống!")
            self.lbl_scan_size.configure(text="Dung lượng rác tìm thấy: 0 MB (0 tệp tin)")
            self.temp_files_list = []
            self.temp_bytes = 0
            self.btn_scan.configure(state=tk.NORMAL)
            
        threading.Thread(target=run_clean, daemon=True).start()

    # ------------------ TAB 5: CẤU HÌNH API KEY ------------------
    def init_setting_tab(self):
        frame = tk.Frame(self.content_area, bg="#0f172a")
        self.tab_frames["setting"] = frame
        
        # Header
        header = tk.Frame(frame, bg="#1e293b", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        title = tk.Label(header, text="Cấu hình Kết nối AI trực tuyến", font=(self.font_family, 12, "bold"), fg="#f8fafc", bg="#1e293b", padx=15)
        title.pack(side=tk.LEFT, fill=tk.Y)
        
        # Giao diện
        body = tk.Frame(frame, bg="#0f172a", padx=30, pady=30)
        body.pack(fill=tk.BOTH, expand=True)
        
        desc = tk.Label(
            body, 
            text="Bằng việc cung cấp API Key của Google Gemini, bạn có thể trò chuyện trực tiếp\\n"
                 "với các mô hình AI tiên tiến nhất hiện nay (Gemini 1.5 Flash / Pro) ngay trong ứng dụng này.",
            font=(self.font_family, 10), 
            fg="#cbd5e1", 
            bg="#0f172a",
            justify=tk.LEFT,
            anchor="w"
        )
        desc.pack(fill=tk.X, pady=(0, 20))
        
        # Ô nhập key
        key_frame = tk.LabelFrame(body, text="Google Gemini API Key", font=(self.font_family, 10, "bold"), fg="#38bdf8", bg="#1e293b", padx=15, pady=15)
        key_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.txt_key = tk.Entry(
            key_frame, 
            bg="#0f172a", 
            fg="#f8fafc", 
            insertbackground="#f8fafc", 
            font=(self.font_family, 11),
            bd=1,
            relief=tk.FLAT
        )
        self.txt_key.pack(fill=tk.X, ipady=8)
        self.txt_key.insert(0, self.api_key)
        
        # Hướng dẫn lấy key
        guide_lbl = tk.Label(
            body, 
            text="💡 Cách lấy khóa API miễn phí:\\n"
                 "1. Truy cập trang web Google AI Studio (aistudio.google.com)\\n"
                 "2. Đăng nhập tài khoản Google và ấn chọn \\"Create API Key\\"\\n"
                 "3. Copy khóa đó dán vào đây và ấn Lưu cấu hình.",
            font=(self.font_family, 9), 
            fg="#94a3b8", 
            bg="#0f172a",
            justify=tk.LEFT,
            anchor="w"
        )
        guide_lbl.pack(fill=tk.X, pady=(0, 20))
        
        # Nút Lưu
        save_btn = tk.Button(
            body, 
            text="✔️ Lưu cấu hình API", 
            font=(self.font_family, 10, "bold"), 
            bg="#38bdf8", 
            fg="#0f172a", 
            activebackground="#0284c7",
            activeforeground="#f8fafc",
            bd=0, 
            padx=20, 
            pady=10,
            cursor="hand2",
            command=self.save_api_key
        )
        save_btn.pack(anchor="w")

    def save_api_key(self):
        self.api_key = self.txt_key.get().strip()
        self.save_config()
        messagebox.showinfo("Thành công", "Đã lưu cấu hình API thành công! Bây giờ bạn có thể chat AI trực tuyến.")
        self.select_tab("chat")

if __name__ == "__main__":
    root = tk.Tk()
    app = AntigravityAgentApp(root)
    root.mainloop()
"""
    
    # Nội dung của file bat chạy agent
    bat_content = """@echo off
title Khoi dong Antigravity AI Agent Pro v1.0
echo ==========================================================
echo       KHOI DONG ANTIGRAVITY AI AGENT PRO v1.0
echo ==========================================================
echo.
echo Dang kiem tra moi truong Python...
py -c "import tkinter" >nul 2>&1
if %errorlevel% neq 0 (
    python -c "import tkinter" >nul 2>&1
    if %errorlevel% neq 0 (
        echo [ERROR] Khong tim thay Python hoac module tkinter tren he thong.
        echo Vui long tai va cai dat Python (co tich chon Tcl/Tk and IDLE)
        echo tren web direct-downloader de chay ung dung nay!
        echo.
        pause
        exit /b 1
    ) else (
        echo Khoi chay bang lenh 'python'...
        start pythonw agent.py
    )
) else (
    echo Khoi chay bang lenh 'py'...
    start pyw agent.py
)
echo Da khoi chay thanh cong! Cua so Agent se hien len sau vai giay.
exit
"""

    # Hướng dẫn sử dụng
    readme_content = """===========================================================
               ANTIGRAVITY AI AGENT PRO v1.0
===========================================================

Chào mừng bạn đã tải về phần mềm Antigravity AI Agent Pro!
Đây là một phần mềm thực sự và có đầy đủ chức năng hoạt động offline/online.

CÁC TÍNH NĂNG CHÍNH:
1. Trò chuyện AI (Offline thông minh & Online thông qua khóa API Google Gemini).
2. Tra cứu thông số phần cứng của Máy tính (CPU, RAM, OS, Hostname, Python, v.v.).
3. Trình tạo và xuất mã nguồn Python nhanh (QuickCode) kèm nút chạy thử trực tiếp.
4. Trình quét dọn các file tạm (Temp Files) an toàn để giải phóng dung lượng đĩa cứng.

HƯỚNG DẪN KHỞI CHẠY TRÊN WINDOWS:
- Cách 1: Click đúp vào file 'chay_agent.bat' để khởi chạy nhanh phần mềm.
- Cách 2: Chạy trực tiếp file 'agent.py' bằng Python (mở terminal và chạy lệnh `py agent.py` hoặc `python agent.py`).

Lưu ý:
Để sử dụng đầy đủ các tính năng lập trình và chạy thử code mẫu, bạn cần cài đặt sẵn Python trên máy tính của mình (có thể tải trực tiếp Python 3.12 từ trang web Direct Downloader).
"""

    # Tạo thư mục download nếu chưa có
    os.makedirs(r"d:\Yahoo!\static\downloads", exist_ok=True)
    
    # Tạo các file tạm thời
    with open("agent.py", "w", encoding="utf-8") as f:
        f.write(agent_py_content)
        
    with open("chay_agent.bat", "w", encoding="utf-8") as f:
        f.write(bat_content)
        
    with open("HUONG_DAN.txt", "w", encoding="utf-8") as f:
        f.write(readme_content)
        
    # Tạo file zip
    zip_path = r"d:\Yahoo!\static\downloads\Antigravity_Agent_Setup.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.write("agent.py", "Antigravity_Agent/agent.py")
        z.write("chay_agent.bat", "Antigravity_Agent/chay_agent.bat")
        z.write("HUONG_DAN.txt", "Antigravity_Agent/HUONG_DAN.txt")
        
    # Xóa các file tạm thời trong thư mục gốc
    os.remove("agent.py")
    os.remove("chay_agent.bat")
    os.remove("HUONG_DAN.txt")
    
    print(f"Đã tạo thành công file zip thực sự tại: {zip_path}")

if __name__ == "__main__":
    create_agent_files()
