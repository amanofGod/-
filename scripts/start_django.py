#!/usr/bin/env python
import os
import sys
import subprocess

# 设置项目目录
project_dir = r'd:\good job\study\wk\ks\1\warehouse_management_system'
os.chdir(project_dir)

# 启动服务器
try:
    print(f"工作目录: {os.getcwd()}")
    print("启动Django开发服务器...")
    subprocess.run([sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000'])
except KeyboardInterrupt:
    print("\n服务器已停止")