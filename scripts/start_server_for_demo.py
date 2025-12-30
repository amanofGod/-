import os
import sys
import subprocess
import time
import webbrowser

# 添加项目目录到Python路径
sys.path.append(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.chdir(r'd:\good job\study\wk\ks\1\warehouse_management_system')

print("启动Django仓库管理系统...")
print("系统功能完整，包括用户管理、仓库管理、货物管理和报表分析")
print("系统特点: Bootstrap界面、数据可视化、完整业务逻辑")

# 打印访问地址
print("\n系统访问地址:")
print("-" * 30)
print("根页面: http://127.0.0.1:8000/")
print("仓库列表: http://127.0.0.1:8000/warehouse/list/")
print("货物列表: http://127.0.0.1:8000/goods/")
print("库存报表: http://127.0.0.1:8000/reports/stock/")
print("管理后台: http://127.0.0.1:8000/admin/")
print("\n登录信息: 用户名 admin, 密码 admin123")

# 启动服务器
print("\n正在启动Django服务器...")
server_process = subprocess.Popen(
    [sys.executable, 'manage.py', 'runserver', '8000'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# 等待服务器启动
time.sleep(3)
print("服务器已启动!")

# 打开浏览器
print("正在打开浏览器...")
webbrowser.open('http://127.0.0.1:8000/warehouse/list/')

print("\n系统已启动，浏览器已打开!")
print("按Ctrl+C停止服务器")

# 等待用户中断
try:
    server_process.wait()
except KeyboardInterrupt:
    print("\n正在关闭服务器...")
    server_process.terminate()
    print("服务器已关闭")