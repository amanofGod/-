#!/usr/bin/env python
import os
import sys
import subprocess

# 设置Django项目路径
django_project_path = os.path.dirname(os.path.abspath(__file__))
warehouse_path = os.path.join(django_project_path, 'warehouse_management_system')

# 切换到Django项目目录
os.chdir(warehouse_path)

print(f"🚀 启动仓库管理系统")
print(f"📍 项目路径: {warehouse_path}")
print(f"🌐 访问地址: http://127.0.0.1:8000/")
print(f"👤 管理员账号: admin / admin123")
print("=" * 50)

# 启动Django服务器
try:
    subprocess.run([sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000'])
except KeyboardInterrupt:
    print("\n🛑 服务器已停止")
except Exception as e:
    print(f"❌ 错误: {e}")