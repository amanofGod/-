#!/usr/bin/env python
import os
import sys
import subprocess

# 正确的项目路径
project_dir = r'd:\good job\study\wk\ks\1\warehouse_management_system'
manage_path = os.path.join(project_dir, 'manage.py')

print(f"项目路径: {project_dir}")
print(f"manage.py路径: {manage_path}")
print(f"文件存在: {os.path.exists(manage_path)}")

if not os.path.exists(manage_path):
    print("❌ manage.py文件不存在")
    sys.exit(1)

# 切换工作目录
os.chdir(project_dir)
print(f"当前工作目录: {os.getcwd()}")

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

# 修改settings.py使用SQLite（避免MySQL问题）
settings_file = os.path.join(project_dir, 'warehouse_management_system', 'settings.py')
with open(settings_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 确保使用SQLite
if 'django.db.backends.sqlite3' not in content:
    sqlite_config = '''# 使用SQLite数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}'''
    
    # 找到并替换数据库配置
    start_idx = content.find('DATABASES = {')
    if start_idx != -1:
        end_idx = content.find('}', start_idx) + 1
        new_content = content[:start_idx] + sqlite_config + '\n' + content[end_idx:]
        
        with open(settings_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ 已切换到SQLite数据库")

print("\n=== 启动信息 ===")
print("数据库: SQLite")
print("访问地址:")
print("- 首页: http://127.0.0.1:8000/")
print("- 货物管理: http://127.0.0.1:8000/goods/list/")
print("- 仓库管理: http://127.0.0.1:8000/warehouse/list/")

# 运行迁移
print("\n正在运行数据库迁移...")
try:
    result = subprocess.run([sys.executable, 'manage.py', 'migrate'], 
                          capture_output=True, text=True, cwd=project_dir)
    print(result.stdout)
    if result.stderr:
        print("警告:", result.stderr)
except Exception as e:
    print(f"迁移失败: {e}")

print("\n启动服务器...")
print("按 Ctrl+C 停止服务器\n")

# 启动服务器
try:
    subprocess.run([sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000'], cwd=project_dir)
except KeyboardInterrupt:
    print("\n✅ 服务器已停止")