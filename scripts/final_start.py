#!/usr/bin/env python
import os
import sys
import subprocess

# 设置绝对路径
project_path = r'd:\good job\study\wk\ks\1\warehouse_management_system'
manage_path = os.path.join(project_path, 'manage.py')

print(f"项目路径: {project_path}")
print(f"manage.py路径: {manage_path}")
print(f"文件存在: {os.path.exists(manage_path)}")

if not os.path.exists(manage_path):
    print("❌ manage.py文件不存在")
    sys.exit(1)

# 切换工作目录
os.chdir(project_path)
print(f"当前工作目录: {os.getcwd()}")

# 添加到Python路径
sys.path.insert(0, project_path)

# 设置环境变量
os.environ['DJANGO_SETTINGS_MODULE'] = 'warehouse_management_system.settings'

print("\n=== 启动信息 ===")
print("数据库: MySQL (warehouse_management)")
print("用户名: root")
print("密码: 123456")
print("主机: localhost:3306")

print("\n访问地址:")
print("- 首页: http://127.0.0.1:8000/")
print("- 货物管理: http://127.0.0.1:8000/goods/list/")
print("- 仓库管理: http://127.0.0.1:8000/warehouse/list/")

print("\n正在启动服务器...")
print("按 Ctrl+C 停止服务器\n")

# 启动服务器
try:
    subprocess.run([sys.executable, manage_path, 'runserver', '127.0.0.1:8000'])
except KeyboardInterrupt:
    print("\n✅ 服务器已停止")