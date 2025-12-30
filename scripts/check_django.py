#!/usr/bin/env python
import os
import sys

# 设置项目目录
project_dir = r'd:\good job\study\wk\ks\1\warehouse_management_system'
os.chdir(project_dir)
sys.path.insert(0, project_dir)

print(f"工作目录: {os.getcwd()}")
print(f"Python路径: {sys.path[0]}")

# 检查Django是否可用
try:
    import django
    print(f"Django版本: {django.get_version()}")
except ImportError:
    print("Django未安装")
    sys.exit(1)

# 检查manage.py是否存在
if os.path.exists('manage.py'):
    print("manage.py文件存在")
else:
    print("manage.py文件不存在")
    sys.exit(1)

# 尝试导入Django设置
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

try:
    import django
    django.setup()
    print("Django设置加载成功")
    
    # 检查URL配置
    from django.urls import reverse
    try:
        url = reverse('goods:goods_list')
        print(f"货物列表URL: {url}")
    except Exception as e:
        print(f"URL反转错误: {e}")
        
except Exception as e:
    print(f"Django设置加载失败: {e}")