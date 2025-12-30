#!/usr/bin/env python
import os
import sys
import subprocess

# 设置项目目录
project_dir = r'd:\good job\study\wk\ks\1\warehouse_management_system'
os.chdir(project_dir)
sys.path.insert(0, project_dir)

print(f"工作目录: {os.getcwd()}")

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

import django
django.setup()

print("正在运行数据库迁移...")
try:
    subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
    print("数据库迁移完成")
except subprocess.CalledProcessError as e:
    print(f"数据库迁移失败: {e}")

print("\n=== 服务器启动信息 ===")
print("- 首页: http://127.0.0.1:8000/")
print("- 货物管理: http://127.0.0.1:8000/goods/list/")
print("- 仓库管理: http://127.0.0.1:8000/warehouse/list/")
print("- 用户注册: http://127.0.0.1:8000/users/register/")
print("\n按Ctrl+C停止服务器")

print("\n正在启动Django开发服务器...")
try:
    subprocess.run([sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000'])
except KeyboardInterrupt:
    print("\n服务器已停止")