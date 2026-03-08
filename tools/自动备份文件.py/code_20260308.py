import shutil
from datetime import datetime

source = r"D:\重要文件"
target = r"D:\备份\备份_" + datetime.now().strftime("%Y%m%d_%H%M%S")

shutil.copytree(source, target)
print("✅ 备份完成：" + target)
