#!/usr/bin/env python
import os
import sys
import subprocess

# 切换到项目目录
project_dir = r'd:\good job\study\wk\ks\1\warehouse_management_system'
os.chdir(project_dir)

print(f"当前目录: {os.getcwd()}")

# 修改settings.py使用SQLite
settings_file = os.path.join(project_dir, 'warehouse_management_system', 'settings.py')
settings_content = '''
# 使用SQLite数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

with open(settings_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 替换数据库配置
start_marker = '# 使用MySQL数据库'
end_marker = '# }'
start_idx = content.find(start_marker)
if start_idx != -1:
    end_idx = content.find('# }', start_idx) + len('# }')
    new_content = content[:start_idx] + settings_content + '\n' + content[end_idx:]
    
    with open(settings_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✅ 已切换到SQLite数据库")

# 运行迁移
print("正在运行数据库迁移...")
try:
    result = subprocess.run([sys.executable, 'manage.py', 'migrate'], 
                          capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("警告:", result.stderr)
except Exception as e:
    print(f"迁移失败: {e}")

# 启动服务器
print("\n启动服务器...")
print("访问地址: http://127.0.0.1:8000/goods/list/")
print("按 Ctrl+C 停止服务器\n")

try:
    subprocess.run([sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000'])
except KeyboardInterrupt:
    print("\n✅ 服务器已停止")