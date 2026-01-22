import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import subprocess
import threading
import re
import os
import sys

# =========================
# FFmpeg yolu (exe içinde çalışsın diye)
# =========================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

ffmpeg_path = resource_path("ffmpeg/ffmpeg.exe")

# =========================
# Video süresini al
# =========================
def get_video_duration(video):
    cmd = [ffmpeg_path, "-i", video]
    result = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)

    match = re.search(r"Duration: (\d+):(\d+):(\d+)", result.stderr)
    if match:
        h, m, s = map(int, match.groups())
        return h * 3600 + m * 60 + s
    return 1

# =========================
# Dönüştürme işlemi (THREAD)
# =========================
def convert_audio():
    video = video_entry.get()
    output = output_entry.get()

    if not video or not output:
        messagebox.showerror("Hata", "Dosyaları seç!")
        return

    progress_bar["value"] = 0
    status_label.config(text="Dönüştürülüyor...")

    duration = get_video_duration(video)

    cmd = [
        ffmpeg_path,
        "-i", video,
        "-vn",
        "-acodec", "libmp3lame",
        output,
        "-y"
    ]

    process = subprocess.Popen(
        cmd,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )

    for line in process.stderr:
        match = re.search(r"time=(\d+):(\d+):(\d+)", line)
        if match:
            h, m, s = map(int, match.groups())
            current = h * 3600 + m * 60 + s
            percent = (current / duration) * 100
            progress_bar["value"] = percent
            root.update_idletasks()

    process.wait()
    progress_bar["value"] = 100
    status_label.config(text="✔ Tamamlandı")

# =========================
# Thread başlat
# =========================
def start_conversion():
    threading.Thread(target=convert_audio, daemon=True).start()

# =========================
# Dosya seçiciler
# =========================
def select_video():
    path = filedialog.askopenfilename(filetypes=[("Video", "*.mp4 *.mkv *.avi")])
    if path:
        video_entry.delete(0, tk.END)
        video_entry.insert(0, path)

def select_output():
    path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                        filetypes=[("MP3", "*.mp3")])
    if path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, path)

# =========================
# GUI
# =========================
root = tk.Tk()
root.title("Audio / Video Converter")
root.geometry("500x300")

tk.Label(root, text="Video Dosyası:").pack()
video_entry = tk.Entry(root, width=60)
video_entry.pack()
tk.Button(root, text="Video Seç", command=select_video).pack(pady=5)

tk.Label(root, text="Çıkış Audio Dosyası:").pack()
output_entry = tk.Entry(root, width=60)
output_entry.pack()
tk.Button(root, text="Kaydetme Yeri", command=select_output).pack(pady=5)

progress_bar = ttk.Progressbar(root, length=400, mode="determinate")
progress_bar.pack(pady=15)

status_label = tk.Label(root, text="")
status_label.pack()

tk.Button(root, text="Başlat", command=start_conversion).pack(pady=10)

root.mainloop()
