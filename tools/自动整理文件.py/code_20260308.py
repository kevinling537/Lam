import os
import shutil

# 自动整理下载文件夹
path = r"C:\Users\14762\Downloads"

ext_map = {
    "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "视频": [".mp4", ".mov", ".avi", ".mkv"],
    "文档": [".doc", ".docx", ".pdf", ".txt", ".xlsx", ".ppt"],
    "压缩包": [".zip", ".rar", ".7z", ".tar"],
    "软件": [".exe", ".msi"],
}

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[-1].lower()
        for folder, exts in ext_map.items():
            if ext in exts:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file))
                break
