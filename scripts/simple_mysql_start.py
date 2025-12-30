import os
import sys
import subprocess

# 切换到项目目录
os.chdir(r'd:\good job\study\wk\ks\1\warehouse_management_system')
print(f"当前目录: {os.getcwd()}")

# 检查manage.py
if not os.path.exists('manage.py'):
    print("❌ manage.py 不存在")
    sys.exit(1)

print("✅ 找到manage.py")

# 直接运行迁移和启动服务器
print("正在运行数据库迁移...")
result = subprocess.run([sys.executable, 'manage.py', 'migrate'], capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("错误:", result.stderr)

print("\n启动服务器...")
subprocess.run([sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000'])