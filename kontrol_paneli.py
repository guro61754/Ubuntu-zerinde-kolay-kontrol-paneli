import tkinter as tk
from tkinter import messagebox
import subprocess
import platform
import psutil
import socket

def get_system_info():
    info = f"""
Sistem: {platform.system()}
Sürüm: {platform.release()}
İşlemci: {platform.processor()}
RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB
"""
    messagebox.showinfo("Sistem Bilgisi", info)

def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    messagebox.showinfo("Ağ Bilgisi", f"Hostname: {hostname}\nIP Adresi: {ip_address}")

def update_system():
    result = subprocess.run(["sudo", "apt", "update"], capture_output=True, text=True)
    messagebox.showinfo("Güncelleme", result.stdout)

def list_services():
    result = subprocess.run(["systemctl", "list-units", "--type=service", "--state=running"], capture_output=True, text=True)
    show_large_output("Çalışan Servisler", result.stdout)

def show_large_output(title, content):
    output_window = tk.Toplevel(root)
    output_window.title(title)
    text_area = tk.Text(output_window, wrap='word')
    text_area.insert('1.0', content)
    text_area.pack(expand=True, fill='both')

root = tk.Tk()
root.title("Ubuntu Kontrol Paneli")
root.geometry("400x300")

tk.Label(root, text="Kontrol Paneli", font=("Helvetica", 16)).pack(pady=10)

tk.Button(root, text="Sistem Bilgisi", width=30, command=get_system_info).pack(pady=5)
tk.Button(root, text="Ağ Bilgisi", width=30, command=get_network_info).pack(pady=5)
tk.Button(root, text="Güncellemeleri Kontrol Et", width=30, command=update_system).pack(pady=5)
tk.Button(root, text="Çalışan Servisleri Görüntüle", width=30, command=list_services).pack(pady=5)

tk.Button(root, text="Çıkış", width=30, command=root.quit).pack(pady=20)

root.mainloop()
