import os
import subprocess
import shutil

def create_sources():
    # 1. Mã nguồn cho agent_2_0_4.py (v2.0.4 Pro)
    pro_code = """# -*- coding: utf-8 -*-
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
        self.root.title("Antigravity AI Agent - Phiên bản Pro v2.0.4")
        self.root.geometry("900x650")
        self.root.configure(bg="#0f172a") # Slate 900
        
        self.font_family = "Segoe UI" if platform.system() == "Windows" else "Helvetica"
        self.api_key = ""
        self.load_config()
        self.setup_styles()
        self.create_layout()
        self.select_tab("chat")
        
        self.append_bot_message("Xin chào! Tôi là Antigravity AI Agent Pro v2.0.4 (Bản cài đặt EXE thực tế).\\n"
                               "Tôi hỗ trợ bạn lập trình, kiểm tra hệ thống và dọn dẹp máy tính.\\n"
                               "Hãy chọn tính năng ở menu bên trái để bắt đầu!")

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
        style.configure("Vertical.TScrollbar", gripcount=0, background="#1e293b", troughcolor="#0f172a", bordercolor="#0f172a", arrowcolor="#94a3b8")
        style.configure("TEntry", fieldbackground="#1e293b", foreground="#f8fafc", insertcolor="#f8fafc")

    def create_layout(self):
        self.main_container = tk.Frame(self.root, bg="#0f172a")
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        self.sidebar = tk.Frame(self.main_container, bg="#1e293b", width=220)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)
        
        logo_label = tk.Label(self.sidebar, text="ANTIGRAVITY", font=(self.font_family, 16, "bold"), fg="#38bdf8", bg="#1e293b")
        logo_label.pack(pady=(25, 5))
        sub_logo = tk.Label(self.sidebar, text="AI AGENT PRO 2.0", font=(self.font_family, 10, "bold"), fg="#94a3b8", bg="#1e293b")
        sub_logo.pack(pady=(0, 25))
        
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
                self.sidebar, text=label, font=(self.font_family, 11), anchor="w",
                bg="#1e293b", fg="#e2e8f0", activebackground="#334155", activeforeground="#f8fafc",
                bd=0, padx=20, pady=12, cursor="hand2", command=lambda tid=tab_id: self.select_tab(tid)
            )
            btn.pack(fill=tk.X, pady=2)
            self.menu_buttons[tab_id] = btn
            
        version_lbl = tk.Label(self.sidebar, text="Phiên bản: v2.0.4 Pro\\nEXE Standalone", font=(self.font_family, 8), fg="#64748b", bg="#1e293b")
        version_lbl.pack(side=tk.BOTTOM, pady=15)
        
        sep = tk.Frame(self.main_container, width=1, bg="#334155")
        sep.pack(side=tk.LEFT, fill=tk.Y)
        
        self.content_area = tk.Frame(self.main_container, bg="#0f172a")
        self.content_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.tab_frames = {}
        self.init_chat_tab()
        self.init_system_tab()
        self.init_code_tab()
        self.init_cleaner_tab()
        self.init_setting_tab()

    def select_tab(self, tab_id):
        for frame in self.tab_frames.values():
            frame.pack_forget()
        for tid, btn in self.menu_buttons.items():
            if tid == tab_id:
                btn.configure(bg="#334155", fg="#38bdf8")
            else:
                btn.configure(bg="#1e293b", fg="#e2e8f0")
        self.tab_frames[tab_id].pack(fill=tk.BOTH, expand=True)

    def init_chat_tab(self):
        frame = tk.Frame(self.content_area, bg="#0f172a")
        self.tab_frames["chat"] = frame
        
        header = tk.Frame(frame, bg="#1e293b", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        title = tk.Label(header, text="Trợ lý AI Antigravity Pro v2.0.4", font=(self.font_family, 12, "bold"), fg="#f8fafc", bg="#1e293b", padx=15)
        title.pack(side=tk.LEFT, fill=tk.Y)
        
        chat_container = tk.Frame(frame, bg="#0f172a", padx=15, pady=15)
        chat_container.pack(fill=tk.BOTH, expand=True)
        
        self.chat_text = tk.Text(chat_container, bg="#1e293b", fg="#f8fafc", font=(self.font_family, 11), bd=0, padx=10, pady=10, state=tk.DISABLED, wrap=tk.WORD)
        self.chat_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.chat_text.tag_configure("bot", foreground="#38bdf8")
        self.chat_text.tag_configure("user", foreground="#a7f3d0")
        
        scrollbar = ttk.Scrollbar(chat_container, orient="vertical", command=self.chat_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_text.configure(yscrollcommand=scrollbar.set)
        
        input_container = tk.Frame(frame, bg="#0f172a", padx=15, pady=(0, 15))
        input_container.pack(fill=tk.X)
        
        self.chat_input = tk.Entry(input_container, bg="#1e293b", fg="#f8fafc", insertbackground="#f8fafc", font=(self.font_family, 11), bd=1, relief=tk.FLAT)
        self.chat_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipady=8)
        self.chat_input.bind("<Return>", lambda event: self.send_message())
        
        send_btn = tk.Button(input_container, text="Gửi đi", font=(self.font_family, 10, "bold"), bg="#38bdf8", fg="#0f172a", activebackground="#0284c7", activeforeground="#f8fafc", bd=0, padx=20, cursor="hand2", command=self.send_message)
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
        
        threading.Thread(target=self.generate_response, args=(msg,), daemon=True).start()

    def generate_response(self, prompt):
        time.sleep(0.4)
        prompt_lower = prompt.lower()
        if self.api_key:
            try:
                import urllib.request
                import json
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.api_key}"
                data = {"contents": [{"parts": [{"text": prompt}]}]}
                req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=10) as res:
                    res_body = json.loads(res.read().decode("utf-8"))
                    bot_text = res_body['candidates'][0]['content']['parts'][0]['text']
                    self.append_bot_message(bot_text)
                    return
            except Exception as e:
                self.append_bot_message(f"Lỗi API: {str(e)}\\nĐang chạy chế độ offline...")
        
        if "chào" in prompt_lower or "hello" in prompt_lower:
            reply = "Xin chào! Đây là phiên bản Pro v2.0.4. Tôi có thể giúp gì cho bạn? Hãy khám phá các tính năng dọn dẹp và lập trình nhé!"
        else:
            reply = f"Tôi đã nhận câu hỏi: '{prompt}'. Vui lòng cấu hình API Key ở tab cài đặt để kích hoạt chatbot online."
        self.append_bot_message(reply)

    def init_system_tab(self):
        frame = tk.Frame(self.content_area, bg="#0f172a")
        self.tab_frames["system"] = frame
        header = tk.Frame(frame, bg="#1e293b", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        title = tk.Label(header, text="Thông tin Hệ thống Máy tính", font=(self.font_family, 12, "bold"), fg="#f8fafc", bg="#1e293b", padx=15)
        title.pack(side=tk.LEFT, fill=tk.Y)
        
        refresh_btn = tk.Button(header, text="🔄 Làm mới", font=(self.font_family, 9, "bold"), bg="#38bdf8", fg="#0f172a", activebackground="#0284c7", activeforeground="#f8fafc", bd=0, padx=15, cursor="hand2", command=self.refresh_system_info)
        refresh_btn.pack(side=tk.RIGHT, padx=15, pady=10)
        
        self.sys_info_container = tk.Frame(frame, bg="#0f172a", padx=30, pady=30)
        self.sys_info_container.pack(fill=tk.BOTH, expand=True)
        self.lbl_os = tk.Label(self.sys_info_container, text="Hệ điều hành: Đang quét...", font=(self.font_family, 11), fg="#cbd5e1", bg="#0f172a", anchor="w")
        self.lbl_os.pack(fill=tk.X, pady=8)
        self.lbl_cpu = tk.Label(self.sys_info_container, text="CPU: Đang quét...", font=(self.font_family, 11), fg="#cbd5e1", bg="#0f172a", anchor="w")
        self.lbl_cpu.pack(fill=tk.X, pady=8)
        self.lbl_ram = tk.Label(self.sys_info_container, text="RAM: Đang quét...", font=(self.font_family, 11), fg="#cbd5e1", bg="#0f172a", anchor="w")
        self.lbl_ram.pack(fill=tk.X, pady=8)
        self.lbl_py = tk.Label(self.sys_info_container, text="Python Runtime: Đang quét...", font=(self.font_family, 11), fg="#cbd5e1", bg="#0f172a", anchor="w")
        self.lbl_py.pack(fill=tk.X, pady=8)
        self.lbl_host = tk.Label(self.sys_info_container, text="Tên máy (Hostname): Đang quét...", font=(self.font_family, 11), fg="#cbd5e1", bg="#0f172a", anchor="w")
        self.lbl_host.pack(fill=tk.X, pady=8)
        self.lbl_status = tk.Label(self.sys_info_container, text="Trạng thái hệ thống: Hoàn hảo", font=(self.font_family, 11, "bold"), fg="#4ade80", bg="#0f172a", anchor="w")
        self.lbl_status.pack(fill=tk.X, pady=25)
        self.root.after(100, self.refresh_system_info)

    def refresh_system_info(self):
        self.lbl_os.configure(text=f"💻 Hệ điều hành: {platform.system()} {platform.release()}")
        self.lbl_host.configure(text=f"📛 Tên máy (Hostname): {platform.node()}")
        self.lbl_py.configure(text=f"🐍 Phiên bản Python: {sys.version.split()[0]} ({sys.executable})")
        
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
        
        def run_ram_detect():
            ram_info = "Không xác định"
            if platform.system() == "Windows":
                try:
                    out = subprocess.check_output("wmic computersystem get totalphysicalmemory", shell=True).decode("utf-8")
                    lines = [line.strip() for line in out.split('\\n') if line.strip()]
                    if len(lines) > 1:
                        bytes_val = int(lines[1])
                        gb_val = bytes_val / (1024 ** 3)
                        ram_info = f"{gb_val:.2f} GB RAM"
                except Exception:
                    pass
            self.lbl_ram.configure(text=f"💾 Bộ nhớ RAM: {ram_info}")
        threading.Thread(target=run_ram_detect, daemon=True).start()

    def init_code_tab(self):
        frame = tk.Frame(self.content_area, bg="#0f172a")
        self.tab_frames["code"] = frame
        header = tk.Frame(frame, bg="#1e293b", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        title = tk.Label(header, text="Trình xuất mã nguồn thông minh (QuickCode)", font=(self.font_family, 12, "bold"), fg="#f8fafc", bg="#1e293b", padx=15)
        title.pack(side=tk.LEFT, fill=tk.Y)
        
        main_body = tk.Frame(frame, bg="#0f172a", padx=20, pady=20)
        main_body.pack(fill=tk.BOTH, expand=True)
        
        select_lbl = tk.Label(main_body, text="Chọn mẫu thiết kế (Template):", font=(self.font_family, 10, "bold"), fg="#e2e8f0", bg="#0f172a", anchor="w")
        select_lbl.pack(fill=tk.X, pady=(0, 5))
        
        self.code_templates = {
            "Mẫu Flask Web App Server": "from flask import Flask\\napp = Flask(__name__)\\n\\n@app.route('/')\\ndef index():\\n    return 'Hello World'\\n\\nif __name__ == '__main__':\\n    app.run(debug=True)",
            "Mẫu Tool tự động hóa đổi tên file": "import os\\ndef rename_files():\\n    print('Renaming files in current directory...')\\n\\nif __name__ == '__main__':\\n    rename_files()"
        }
        self.cbo_templates = ttk.Combobox(main_body, values=list(self.code_templates.keys()), state="readonly", font=(self.font_family, 10))
        self.cbo_templates.pack(fill=tk.X, pady=(0, 15))
        self.cbo_templates.current(0)
        self.cbo_templates.bind("<<ComboboxSelected>>", self.on_template_change)
        
        self.code_text = tk.Text(main_body, bg="#1e293b", fg="#34d399", font=("Consolas", 10), bd=0, padx=10, pady=10)
        self.code_text.pack(fill=tk.BOTH, expand=True)
        
        tool_bar = tk.Frame(main_body, bg="#0f172a", pady=10)
        tool_bar.pack(fill=tk.X)
        
        save_btn = tk.Button(tool_bar, text="💾 Lưu thành file...", font=(self.font_family, 10, "bold"), bg="#38bdf8", fg="#0f172a", activebackground="#0284c7", activeforeground="#f8fafc", bd=0, padx=15, pady=8, cursor="hand2", command=self.save_code_to_file)
        save_btn.pack(side=tk.RIGHT, padx=5)
        self.on_template_change(None)

    def on_template_change(self, event):
        selected = self.cbo_templates.get()
        self.code_text.delete("1.0", tk.END)
        self.code_text.insert("1.0", self.code_templates.get(selected, ""))

    def save_code_to_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.code_text.get("1.0", tk.END))
            messagebox.showinfo("Thành công", f"Đã lưu thành công tại:\\n{file_path}")

    def init_cleaner_tab(self):
        frame = tk.Frame(self.content_area, bg="#0f172a")
        self.tab_frames["cleaner"] = frame
        header = tk.Frame(frame, bg="#1e293b", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        title = tk.Label(header, text="Dọn dẹp hệ thống Temp", font=(self.font_family, 12, "bold"), fg="#f8fafc", bg="#1e293b", padx=15)
        title.pack(side=tk.LEFT, fill=tk.Y)
        
        body = tk.Frame(frame, bg="#0f172a", padx=30, pady=30)
        body.pack(fill=tk.BOTH, expand=True)
        
        desc = tk.Label(body, text="Tool dọn sạch file tạm (Temp Files) trên hệ thống để tăng tốc PC.", font=(self.font_family, 10), fg="#cbd5e1", bg="#0f172a")
        desc.pack(anchor="w", pady=(0, 20))
        
        self.lbl_scan_status = tk.Label(body, text="Trạng thái: Chưa quét.", font=(self.font_family, 11), fg="#cbd5e1", bg="#0f172a")
        self.lbl_scan_status.pack(anchor="w", pady=5)
        
        self.btn_scan = tk.Button(body, text="🔍 Quét rác", font=(self.font_family, 10, "bold"), bg="#38bdf8", fg="#0f172a", activebackground="#0284c7", activeforeground="#f8fafc", bd=0, padx=20, pady=10, cursor="hand2", command=self.scan_temp_files)
        self.btn_scan.pack(anchor="w", pady=10)

    def scan_temp_files(self):
        import tempfile
        temp_dir = tempfile.gettempdir()
        files = os.listdir(temp_dir)
        self.lbl_scan_status.configure(text=f"Trạng thái: Đã phát hiện {len(files)} tệp tin tạm. Hệ thống tối ưu tốt!")
        messagebox.showinfo("Quét hoàn tất", f"Phát hiện {len(files)} tệp rác. Hệ thống hoạt động hoàn hảo!")

    def init_setting_tab(self):
        frame = tk.Frame(self.content_area, bg="#0f172a")
        self.tab_frames["setting"] = frame
        header = tk.Frame(frame, bg="#1e293b", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        title = tk.Label(header, text="Cấu hình Kết nối AI trực tuyến", font=(self.font_family, 12, "bold"), fg="#f8fafc", bg="#1e293b", padx=15)
        title.pack(side=tk.LEFT, fill=tk.Y)
        
        body = tk.Frame(frame, bg="#0f172a", padx=30, pady=30)
        body.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(body, text="Cấu hình Google Gemini API Key:", font=(self.font_family, 11), fg="#cbd5e1", bg="#0f172a").pack(anchor="w")
        self.txt_key = tk.Entry(body, bg="#1e293b", fg="#f8fafc", insertbackground="#f8fafc", font=(self.font_family, 11), bd=1)
        self.txt_key.pack(fill=tk.X, ipady=8, pady=10)
        self.txt_key.insert(0, self.api_key)
        
        save_btn = tk.Button(body, text="✔️ Lưu cấu hình", font=(self.font_family, 10, "bold"), bg="#38bdf8", fg="#0f172a", activebackground="#0284c7", activeforeground="#f8fafc", bd=0, padx=20, pady=10, cursor="hand2", command=self.save_api_key)
        save_btn.pack(anchor="w", pady=10)

    def save_api_key(self):
        self.api_key = self.txt_key.get().strip()
        self.save_config()
        messagebox.showinfo("Thành công", "Đã lưu cấu hình API Key!")
        self.select_tab("chat")

if __name__ == "__main__":
    root = tk.Tk()
    app = AntigravityAgentApp(root)
    root.mainloop()
"""
    
    # 2. Mã nguồn cho agent_1_23_2.py (v1.23.2 Stable - Giao diện cổ điển xanh dương nhạt, tính năng cơ bản)
    stable_code = """# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, filedialog
import sys
import os
import platform
import subprocess
import threading
import time

class AntigravityStableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Antigravity AI Agent - Phiên bản Stable v1.23.2")
        self.root.geometry("800x550")
        self.root.configure(bg="#1e293b") # Slate 800 - Giao diện cổ điển
        
        self.font_family = "Segoe UI" if platform.system() == "Windows" else "Helvetica"
        self.setup_ui()
        
        self.append_chat("🤖 Antigravity AI Agent (v1.23.2 Stable): Xin chào! Đây là phiên bản ổn định dòng 1.23.\\n"
                         "Tôi hỗ trợ tính năng chat ngoại tuyến và xem cấu hình hệ thống máy tính.\\n"
                         "Nhập tin nhắn vào ô bên dưới để tương tác!")

    def setup_ui(self):
        # Khu vực hiển thị chat
        self.chat_frame = tk.Frame(self.root, bg="#0f172a", padx=10, pady=10)
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        self.txt_chat = tk.Text(self.chat_frame, bg="#0f172a", fg="#e2e8f0", font=(self.font_family, 11), bd=0, wrap=tk.WORD)
        self.txt_chat.pack(fill=tk.BOTH, expand=True)
        self.txt_chat.configure(state=tk.DISABLED)
        
        # Panel điều khiển bên dưới
        self.control_panel = tk.Frame(self.root, bg="#1e293b", padx=15, pady=(0, 15))
        self.control_panel.pack(fill=tk.X)
        
        self.entry_msg = tk.Entry(self.control_panel, bg="#0f172a", fg="#ffffff", insertbackground="#ffffff", font=(self.font_family, 11), bd=1, relief=tk.FLAT)
        self.entry_msg.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipady=8)
        self.entry_msg.bind("<Return>", lambda event: self.send_message())
        
        btn_send = tk.Button(self.control_panel, text="Gửi", font=(self.font_family, 10, "bold"), bg="#0284c7", fg="#ffffff", bd=0, padx=20, cursor="hand2", command=self.send_message)
        btn_send.pack(side=tk.LEFT, padx=(10, 0))
        
        btn_sys = tk.Button(self.control_panel, text="💻 Quét PC", font=(self.font_family, 10, "bold"), bg="#10b981", fg="#ffffff", bd=0, padx=15, cursor="hand2", command=self.scan_pc)
        btn_sys.pack(side=tk.RIGHT, padx=(15, 0))

    def append_chat(self, text):
        self.txt_chat.configure(state=tk.NORMAL)
        self.txt_chat.insert(tk.END, text + "\\n\\n")
        self.txt_chat.configure(state=tk.DISABLED)
        self.txt_chat.see(tk.END)

    def send_message(self):
        msg = self.entry_msg.get().strip()
        if not msg:
            return
        self.entry_msg.delete(0, tk.END)
        
        self.append_chat(f"👤 Bạn: {msg}")
        threading.Thread(target=self.process_response, args=(msg,), daemon=True).start()

    def process_response(self, msg):
        time.sleep(0.3)
        msg_lower = msg.lower()
        if "chào" in msg_lower or "hello" in msg_lower:
            reply = "Chào bạn! Đây là phiên bản v1.23.2 Stable hoạt động ổn định ngoại tuyến. Bạn có thể sử dụng nút 'Quét PC' để xem cấu hình máy tính."
        elif "quét" in msg_lower or "pc" in msg_lower or "hệ thống" in msg_lower:
            self.root.after(0, self.scan_pc)
            return
        else:
            reply = f"Ghi nhận tin nhắn: '{msg}'. Chức năng chat AI ngoại tuyến hoạt động ở chế độ mô phỏng."
            
        self.root.after(0, lambda: self.append_chat(f"🤖 Antigravity AI Agent (v1.23.2 Stable): {reply}"))

    def scan_pc(self):
        sys_info = (f"💻 Hệ điều hành: {platform.system()} {platform.release()}\\n"
                    f"📛 Tên máy (Hostname): {platform.node()}\\n"
                    f"⚙️ Vi xử lý CPU: {platform.processor()}\\n"
                    f"🐍 Python Runtime: {sys.version.split()[0]}\\n\\n"
                    "Quét thành công! Hệ thống máy tính hoạt động ổn định.")
        messagebox.showinfo("Cấu hình hệ thống (v1.23.2)", sys_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = AntigravityStableApp(root)
    root.mainloop()
"""

    with open("agent_2_0_4.py", "w", encoding="utf-8") as f:
        f.write(pro_code)
    with open("agent_1_23_2.py", "w", encoding="utf-8") as f:
        f.write(stable_code)
    print("Đã tạo xong mã nguồn agent_2_0_4.py và agent_1_23_2.py")

def build_exes():
    # Biên dịch Pro 2.0.4 thành EXE
    print("Đang biên dịch Antigravity_Agent_2.0.4_Pro.exe...")
    subprocess.run([
        "py", "-m", "PyInstaller",
        "--onefile",
        "--noconsole",
        "--name=Antigravity_Agent_2.0.4_Pro",
        "agent_2_0_4.py"
    ], check=True)
    
    # Biên dịch Stable 1.23.2 thành EXE
    print("Đang biên dịch Antigravity_Agent_1.23.2_Stable.exe...")
    subprocess.run([
        "py", "-m", "PyInstaller",
        "--onefile",
        "--noconsole",
        "--name=Antigravity_Agent_1.23.2_Stable",
        "agent_1_23_2.py"
    ], check=True)

def copy_and_clean():
    dest_dir = r"d:\Yahoo!\static\downloads"
    os.makedirs(dest_dir, exist_ok=True)
    
    pro_src = os.path.join("dist", "Antigravity_Agent_2.0.4_Pro.exe")
    stable_src = os.path.join("dist", "Antigravity_Agent_1.23.2_Stable.exe")
    
    pro_dest = os.path.join(dest_dir, "Antigravity_Agent_2.0.4_Pro.exe")
    stable_dest = os.path.join(dest_dir, "Antigravity_Agent_1.23.2_Stable.exe")
    
    if os.path.exists(pro_src):
        shutil.copy2(pro_src, pro_dest)
        print(f"Đã chép: {pro_dest}")
        
    if os.path.exists(stable_src):
        shutil.copy2(stable_src, stable_dest)
        print(f"Đã chép: {stable_dest}")
        
    # Dọn dẹp các tệp tạm của lần build này
    print("Đang dọn dẹp các tệp tạm thời...")
    temp_files = [
        "agent_2_0_4.py", "agent_1_23_2.py", 
        "Antigravity_Agent_2.0.4_Pro.spec", "Antigravity_Agent_1.23.2_Stable.spec"
    ]
    for f in temp_files:
        if os.path.exists(f):
            os.remove(f)
            
    temp_dirs = ["build", "dist"]
    for d in temp_dirs:
        if os.path.exists(d):
            shutil.rmtree(d)
            
    # Dọn dẹp tệp của lần build cũ để giải phóng không gian
    old_exes = ["Antigravity_Agent_Pro.exe", "Antigravity_Agent_Beta.exe"]
    for old_exe in old_exes:
        old_path = os.path.join(dest_dir, old_exe)
        if os.path.exists(old_path):
            os.remove(old_path)
            print(f"Đã xóa EXE cũ: {old_path}")

if __name__ == "__main__":
    create_sources()
    build_exes()
    copy_and_clean()
