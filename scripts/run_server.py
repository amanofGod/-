#!/usr/bin/env python
import subprocess
import sys
import os

print("🚀 启动仓库管理系统")
print("=" * 50)

# 直接运行Django服务器
manage_path = r'd:\good job\study\wk\ks\1\warehouse_management_system\manage.py'
command = [sys.executable, manage_path, 'runserver', '127.0.0.1:8000']

print(f"执行命令: {' '.join(command)}")
print("📍 访问地址: http://127.0.0.1:8000/")
print("👤 管理员账号: admin / admin123")
print("🛑 按Ctrl+C停止服务器")
print("=" * 50)

try:
    subprocess.run(command)
except KeyboardInterrupt:
    print("\n🛑 服务器已停止")
except Exception as e:
    print(f"❌ 错误: {e}")