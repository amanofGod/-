#!/usr/bin/env python
import os
import sys
import subprocess
import webbrowser
import time

# 设置工作目录
project_dir = r'd:\good job\study\wk\ks\1\warehouse_management_system'
os.chdir(project_dir)

# 添加到Python路径
sys.path.insert(0, project_dir)

print(f"工作目录: {os.getcwd()}")
print("启动Django开发服务器...")
print("\n=== 访问地址 ===")
print("- 首页: http://127.0.0.1:8000/")
print("- 货物管理: http://127.0.0.1:8000/goods/list/")
print("- 仓库管理: http://127.0.0.1:8000/warehouse/list/")
print("- 报表分析: http://127.0.0.1:8000/reports/stock/")
print("  ├── 库存报表: http://127.0.0.1:8000/reports/stock/")
print("  ├── 出入库报表: http://127.0.0.1:8000/reports/inbound-outbound/")
print("  └── 仓库报表: http://127.0.0.1:8000/reports/warehouse/")
print("- 用户注册: http://127.0.0.1:8000/users/register/")
print("\n=== 功能特色 ===")
print("✅ 完整的用户注册/登录/权限管理")
print("✅ 货物入库/出库/库存盘点")
print("✅ 实时库存统计和预警")
print("✅ 三种报表类型（库存/出入库/仓库）")
print("✅ 密码复杂度验证和强度指示器")
print("\n按Ctrl+C停止服务器")

# 启动服务器
try:
    subprocess.run([sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000'])
except KeyboardInterrupt:
    print("\n服务器已停止")