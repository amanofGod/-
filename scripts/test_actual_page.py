#!/usr/bin/env python
import os
import sys
import django
import subprocess
import time
import webbrowser

# 添加项目路径
sys.path.append('d:/good job/study/wk/ks/1/warehouse_management_system')

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

from goods.models import Goods
from django.db.models import Sum

print("=== 启动服务器前的数据检查 ===")
goods_list = Goods.objects.all()
total_quantity = goods_list.aggregate(total=Sum('quantity'))['total'] or 0
print(f"实际数据库中的总库存量: {total_quantity}")

print("\n=== 启动Django服务器 ===")
print("服务器将启动在 http://127.0.0.1:8000/")
print("请访问货物列表页面: http://127.0.0.1:8000/goods/")
print("登录信息:")
print("- 用户名: admin")
print("- 密码: admin123")
print("\n按Ctrl+C停止服务器")

# 启动Django服务器
os.chdir('d:/good job/study/wk/ks/1/warehouse_management_system')
try:
    subprocess.run([sys.executable, 'manage.py', 'runserver'], check=True)
except KeyboardInterrupt:
    print("\n服务器已停止")
except subprocess.CalledProcessError as e:
    print(f"启动服务器时出错: {e}")