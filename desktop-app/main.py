#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正宗土豆服务器 - 桌面管理工具
功能：启动/停止/重启服务器、查看日志、发送指令、AI助手、数据备份
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
import json
import threading
import time
import os

# 配置
API_BASE = 'http://tudoumc.fucku.top:56768'
API_KEY = 'mc-admin-2024-key'
CONFIG_FILE = os.path.join(os.path.expanduser('~'), '.mc_server_config.json')

class MCServerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🥔 正宗土豆服务器 - 管理工具")
        self.root.geometry("900x650")
        self.root.configure(bg='#1a1a2e')
        
        # 加载配置
        self.load_config()
        
        # 创建界面
        self.create_widgets()
        
        # 自动刷新
        self.refresh_status()
        self.auto_refresh_logs()
    
    def load_config(self):
        global API_BASE
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, 'r') as f:
                    config = json.load(f)
                    API_BASE = config.get('api_base', API_BASE)
        except:
            pass
    
    def save_config(self):
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump({'api_base': API_BASE}, f)
        except:
            pass
    
    def create_widgets(self):
        # 顶部标题栏
        title_frame = tk.Frame(self.root, bg='#16213e', height=60)
        title_frame.pack(fill='x')
        title_frame.pack_propagate(False)
        
        tk.Label(title_frame, text="🥔 正宗土豆服务器", font=('微软雅黑', 18, 'bold'),
                bg='#16213e', fg='#00d4ff').pack(side='left', padx=20, pady=10)
        
        self.status_label = tk.Label(title_frame, text="● 检查中...", font=('微软雅黑', 12),
                                    bg='#16213e', fg='#ffd700')
        self.status_label.pack(side='right', padx=20)
        
        # 控制面板
        control_frame = tk.Frame(self.root, bg='#1a1a2e')
        control_frame.pack(fill='x', padx=10, pady=10)
        
        # 按钮样式
        btn_style = {'font': ('微软雅黑', 11), 'width': 12, 'height': 2, 'relief': 'flat', 'cursor': 'hand2'}
        
        self.start_btn = tk.Button(control_frame, text="▶ 启动服务器", bg='#00b894', fg='white',
                                   command=self.start_server, **btn_style)
        self.start_btn.pack(side='left', padx=5)
        
        self.stop_btn = tk.Button(control_frame, text="⏹ 停止服务器", bg='#e74c3c', fg='white',
                                  command=self.stop_server, **btn_style)
        self.stop_btn.pack(side='left', padx=5)
        
        self.restart_btn = tk.Button(control_frame, text="🔄 智能重启", bg='#f39c12', fg='white',
                                     command=self.restart_server, **btn_style)
        self.restart_btn.pack(side='left', padx=5)
        
        self.backup_btn = tk.Button(control_frame, text="📦 备份数据", bg='#9b59b6', fg='white',
                                    command=self.backup_server, **btn_style)
        self.backup_btn.pack(side='left', padx=5)
        
        self.optimize_btn = tk.Button(control_frame, text="🤖 AI优化", bg='#3498db', fg='white',
                                      command=self.ai_optimize, **btn_style)
        self.optimize_btn.pack(side='left', padx=5)
        
        # 状态信息
        info_frame = tk.Frame(self.root, bg='#16213e')
        info_frame.pack(fill='x', padx=10, pady=5)
        
        self.info_labels = {}
        info_items = [('players', '👥 在线玩家', '0'), ('cpu', '💻 CPU', '--'), 
                      ('mem', '💾 内存', '--'), ('uptime', '⏱ 运行时间', '--')]
        
        for i, (key, label, default) in enumerate(info_items):
            frame = tk.Frame(info_frame, bg='#16213e')
            frame.grid(row=0, column=i, padx=15, pady=10, sticky='w')
            tk.Label(frame, text=label, font=('微软雅黑', 10), bg='#16213e', fg='#888').pack()
            self.info_labels[key] = tk.Label(frame, text=default, font=('微软雅黑', 14, 'bold'),
                                             bg='#16213e', fg='#00d4ff')
            self.info_labels[key].pack()
        
        # 日志区域
        log_frame = tk.Frame(self.root, bg='#1a1a2e')
        log_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        tk.Label(log_frame, text="📜 服务器日志", font=('微软雅黑', 11, 'bold'),
                bg='#1a1a2e', fg='#00d4ff').pack(anchor='w')
        
        self.log_text = scrolledtext.ScrolledText(log_frame, bg='#0d0d1a', fg='#00ff00',
                                                   font=('Consolas', 10), wrap='word')
        self.log_text.pack(fill='both', expand=True, pady=5)
        
        # 指令输入
        cmd_frame = tk.Frame(self.root, bg='#1a1a2e')
        cmd_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(cmd_frame, text="指令:", font=('微软雅黑', 11), bg='#1a1a2e', fg='#fff').pack(side='left')
        
        self.cmd_entry = tk.Entry(cmd_frame, bg='#0d0d1a', fg='#fff', font=('微软雅黑', 11),
                                  insertbackground='#fff')
        self.cmd_entry.pack(side='left', fill='x', expand=True, padx=10, ipady=5)
        self.cmd_entry.bind('<Return>', lambda e: self.send_command())
        
        tk.Button(cmd_frame, text="发送", bg='#00b894', fg='white', font=('微软雅黑', 10),
                  command=self.send_command, relief='flat', cursor='hand2').pack(side='left', padx=5)
        
        # 底部状态栏
        status_bar = tk.Frame(self.root, bg='#16213e', height=30)
        status_bar.pack(fill='x', side='bottom')
        status_bar.pack_propagate(False)
        
        self.bottom_status = tk.Label(status_bar, text=f"API: {API_BASE}", font=('微软雅黑', 9),
                                      bg='#16213e', fg='#666')
        self.bottom_status.pack(side='left', padx=10)
        
        tk.Button(status_bar, text="⚙️ 设置", bg='#16213e', fg='#888', font=('微软雅黑', 9),
                  relief='flat', command=self.show_settings, cursor='hand2').pack(side='right', padx=10)
    
    def api_request(self, endpoint, method='GET', data=None):
        try:
            url = f"{API_BASE}{endpoint}"
            headers = {'X-API-Key': API_KEY, 'Content-Type': 'application/json'}
            if method == 'GET':
                resp = requests.get(url, headers=headers, timeout=5)
            else:
                resp = requests.post(url, headers=headers, json=data or {}, timeout=5)
            return resp.json()
        except Exception as e:
            return {'success': False, 'message': str(e)}
    
    def refresh_status(self):
        def task():
            try:
                result = self.api_request('/api/status')
                if result.get('running'):
                    self.root.after(0, lambda: self.status_label.config(text="● 运行中", fg='#00ff00'))
                    sys_info = result.get('system', {})
                    self.root.after(0, lambda: self.info_labels['cpu'].config(text=sys_info.get('cpu', '--')))
                    self.root.after(0, lambda: self.info_labels['mem'].config(text=sys_info.get('mem_percent', '--')))
                    self.root.after(0, lambda: self.info_labels['players'].config(text=str(result.get('players', 0))))
                else:
                    self.root.after(0, lambda: self.status_label.config(text="● 已停止", fg='#ff4444'))
            except:
                self.root.after(0, lambda: self.status_label.config(text="● 连接失败", fg='#ff8800'))
            self.root.after(5000, self.refresh_status)
        threading.Thread(target=task, daemon=True).start()
    
    def auto_refresh_logs(self):
        def task():
            try:
                result = self.api_request('/api/logs')
                if result.get('success'):
                    logs = result.get('logs', '')
                    self.root.after(0, lambda: self.update_logs(logs))
            except:
                pass
            self.root.after(3000, self.auto_refresh_logs)
        threading.Thread(target=task, daemon=True).start()
    
    def update_logs(self, logs):
        self.log_text.delete('1.0', 'end')
        self.log_text.insert('end', logs)
        self.log_text.see('end')
    
    def start_server(self):
        result = self.api_request('/api/start', 'POST')
        messagebox.showinfo("提示", result.get('message', '操作完成'))
    
    def stop_server(self):
        if messagebox.askyesno("确认", "确定要停止服务器吗？"):
            result = self.api_request('/api/stop', 'POST')
            messagebox.showinfo("提示", result.get('message', '操作完成'))
    
    def restart_server(self):
        if messagebox.askyesno("确认", "确定要智能重启服务器吗？"):
            result = self.api_request('/api/smart-action', 'POST', {'action': 'restart'})
            messagebox.showinfo("提示", result.get('message', '操作完成'))
    
    def backup_server(self):
        result = self.api_request('/api/backup', 'POST')
        messagebox.showinfo("提示", result.get('message', '操作完成'))
    
    def ai_optimize(self):
        result = self.api_request('/api/smart-action', 'POST', {'action': 'clean-logs'})
        messagebox.showinfo("AI助手", f"AI优化完成！\n\n{result.get('message', '')}")
    
    def send_command(self):
        cmd = self.cmd_entry.get().strip()
        if not cmd:
            return
        result = self.api_request('/api/command', 'POST', {'command': cmd})
        self.cmd_entry.delete(0, 'end')
        self.log_text.insert('end', f"> {cmd}\n")
        self.log_text.see('end')
    
    def show_settings(self):
        global API_BASE
        win = tk.Toplevel(self.root)
        win.title("设置")
        win.geometry("400x200")
        win.configure(bg='#1a1a2e')
        win.transient(self.root)
        win.grab_set()
        
        tk.Label(win, text="API地址设置", font=('微软雅黑', 14, 'bold'),
                bg='#1a1a2e', fg='#00d4ff').pack(pady=15)
        
        tk.Label(win, text="服务器API地址:", bg='#1a1a2e', fg='#fff').pack()
        entry = tk.Entry(win, width=40, font=('微软雅黑', 10))
        entry.insert(0, API_BASE)
        entry.pack(pady=10, ipady=5)
        
        def save():
            global API_BASE
            API_BASE = entry.get().strip().rstrip('/')
            self.save_config()
            self.bottom_status.config(text=f"API: {API_BASE}")
            messagebox.showinfo("提示", "设置已保存！")
            win.destroy()
        
        tk.Button(win, text="保存", bg='#00b894', fg='white', font=('微软雅黑', 11),
                  command=save, relief='flat', width=10).pack(pady=10)

def main():
    root = tk.Tk()
    app = MCServerApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
