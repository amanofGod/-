import os
import sys

# 添加项目目录到Python路径
sys.path.append(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.chdir(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

import django
django.setup()

from django.urls import reverse
from django.test import RequestFactory

# 测试URL反转
try:
    print("测试URL反转:")
    print(f"仓库列表: {reverse('warehouse:warehouse_list')}")
    print(f"货物列表: {reverse('goods:goods_list')}")
    print(f"库存报表: {reverse('reports:stock_report')}")
    print(f"用户登录: {reverse('users:login')}")
    
    # 测试URL解析
    print("\n测试URL解析:")
    from django.urls import resolve
    
    resolved = resolve('/warehouse/')
    print(f"/warehouse/ 解析为: {resolved.namespace}:{resolved.url_name}")
    
    resolved = resolve('/warehouse/list/')
    print(f"/warehouse/list/ 解析为: {resolved.namespace}:{resolved.url_name}")
    
    print("\nURL配置测试完成!")
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()