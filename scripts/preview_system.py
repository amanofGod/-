import os
import sys
import time
import subprocess
import webbrowser

# 添加项目目录到Python路径
sys.path.append(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.chdir(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

import django
django.setup()

print("Django仓库管理系统")
print("=" * 50)
print()
print("系统功能概述:")
print("1. 用户管理 - 注册、登录、个人信息管理")
print("2. 仓库管理 - 仓库的增删改查")
print("3. 货物管理 - 货物信息管理、出入库操作、库存盘点")
print("4. 报表分析 - 库存报表、仓库报表、出入库统计")
print()
print("技术特点:")
print("- Django框架 + SQLite数据库")
print("- Bootstrap 4响应式前端界面")
print("- Chart.js数据可视化")
print("- 完整的CRUD操作和业务逻辑")
print()
print("登录信息:")
print("- 用户名: admin")
print("- 密码: admin123")
print()
print("访问地址:")
print("- 前端页面: http://127.0.0.1:8000/warehouse/")
print("- 管理后台: http://127.0.0.1:8000/admin/")
print()
print("启动服务器中...")

# 启动Django服务器
try:
    server_process = subprocess.Popen(
        [sys.executable, 'manage.py', 'runserver', '8000'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # 等待服务器启动
    time.sleep(3)
    
    # 打开浏览器
    webbrowser.open('http://127.0.0.1:8000/warehouse/')
    
    print("服务器已启动，浏览器已打开！")
    print("按Ctrl+C停止服务器")
    
    # 等待用户中断
    server_process.wait()
except KeyboardInterrupt:
    print("\n正在关闭服务器...")
    server_process.terminate()
    print("服务器已关闭")