import subprocess
import sys
import os

manage_file = r"d:\good job\study\wk\ks\1\warehouse_management_system\manage.py"

print(f"执行文件: {manage_file}")
print(f"文件存在: {os.path.exists(manage_file)}")

try:
    # 直接运行命令
    result = subprocess.run([
        sys.executable, manage_file, 
        "runserver", "127.0.0.1:8000"
    ], check=True)
except subprocess.CalledProcessError as e:
    print(f"命令执行失败: {e}")
except KeyboardInterrupt:
    print("\n用户停止")