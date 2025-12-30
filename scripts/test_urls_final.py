import os
import sys

sys.path.append(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.chdir(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

import django
django.setup()

from django.urls import reverse

print("🔍 URL路径测试")
print("=" * 40)

try:
    print("✅ 仓库列表:", reverse('warehouse:warehouse_list'))
    print("✅ 货物列表:", reverse('goods:goods_list'))
    print("✅ 库存报表:", reverse('reports:stock_report'))
    print("✅ 用户登录:", reverse('users:login'))
    
    print("\n📋 完整URL:")
    print("=" * 40)
    print("仓库列表: http://127.0.0.1:8000" + reverse('warehouse:warehouse_list'))
    print("货物列表: http://127.0.0.1:8000" + reverse('goods:goods_list'))
    print("库存报表: http://127.0.0.1:8000" + reverse('reports:stock_report'))
    print("用户登录: http://127.0.0.1:8000" + reverse('users:login'))
    
except Exception as e:
    print(f"❌ URL测试失败: {e}")

print("\n🚀 如果URL正常，请访问:")
print("http://127.0.0.1:8000/ (根页面会自动跳转)")
print("\n登录信息: admin / admin123")